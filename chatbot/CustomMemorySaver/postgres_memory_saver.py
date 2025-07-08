# chatbot/vector_db/postgres_memory_saver.py

from langgraph.checkpoint.base import BaseCheckpointSaver
from chatbot.models import ChatMemory


class PostgresMemorySaver(BaseCheckpointSaver):
    """
    A LangGraph-compatible memory saver that uses PostgreSQL via Django ORM.
    """

    def get(self, config: dict) -> dict:
        # Fallback for older usage
        state, _ = self.get_tuple(config)
        return state

    def get_tuple(self, config: dict) -> tuple[dict, str | None]:
        thread_id = config["configurable"]["thread_id"]
        try:
            memory = ChatMemory.objects.get(session_id=thread_id)
            return memory.state_json, memory.updated_at.isoformat()
        except ChatMemory.DoesNotExist:
            return {}, None

    def put(self, config: dict, state: dict) -> None:
        thread_id = config["configurable"]["thread_id"]
        ChatMemory.objects.update_or_create(
            session_id=thread_id,
            defaults={"state_json": state}
        )
