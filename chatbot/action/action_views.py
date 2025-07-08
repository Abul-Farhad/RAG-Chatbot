import json

from langchain_core.messages import HumanMessage, AIMessage
from langgraph.checkpoint.memory import MemorySaver
from rest_framework.views import APIView
from rest_framework.response import Response
from chatbot.LLM.groqLLM import GroqLLM
from chatbot.Graph.graph import Graph
from chatbot.CustomMemorySaver.postgres_memory_saver import PostgresMemorySaver

memory = MemorySaver()
class ChatBotAPIView(APIView):
    def post(self, request, *args, **kwargs):

        if not request.session.session_key:
            request.session.save()

        session_id = request.session.session_key

        graph = Graph().setup_graph(checkpoint=memory)

        user_message = request.data.get('messages', '')
        if not user_message:
            return Response({"error": "No message provided"}, status=400)

        config = {
            "configurable": {
                "thread_id": session_id
            }
        }

        human_message = HumanMessage(content=user_message)
        user = request.user
        user_information = {
            "user_id": user.id,
            "name": user.name,
            "email": user.email
        }
        print("user_information:", user_information)
        response = graph.invoke({"messages": [human_message], "user_information": user_information}, config=config)
        ai_response = response["messages"][-1].content

        print("length of state messages:", len(response["messages"]))
        print("summary: ", response.get("summary", "No summary available"))
        return Response({"messages": ai_response}, status=200)
