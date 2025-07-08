from chatbot.vector_db.chat_memory_manager import ChatMemoryManager
from chatbot.vector_db.chroma_db import vector_store
from langchain.tools import tool
from admin_portal.models import Issue
from django.contrib.auth import get_user_model

User = get_user_model()

# @tool
# def retrieve_memory(query: str, session_id: str) -> str:
#     """
#     Retrieve relevant past messages from the vector store.
#
#     Args:
#         query (str): The query to search for in the memory.
#         session_id (str): The session ID to filter messages.
#         k (int): The number of results to return.
#
#     Returns:
#         list: A list of relevant messages.
#     """
#
#     print("--- Retrieving Memory ---")
#     chat_manager = ChatMemoryManager(vector_store=vector_store, session_id=session_id)
#     results = chat_manager.search_memory(query, k=3)
#     result = "\n".join([doc.page_content for doc in results])
#     print("Formatted results: ", result)
#     return result


@tool
def create_issue(user_id: int, title: str, description: str) -> str:
    """
    Create an issue with the given title and description in the admin_portal model named 'Issue'

    Args:
        user_id (int): The ID of the user creating the issue.
        title (str): The title of the issue.
        description (str): The description of the issue.

    Returns:
        str: Confirmation message indicating the issue has been created.
    """
    print("--- Creating Issue ---")
    try:
        # Fetch the user instance
        user = User.objects.get(id=user_id)
        print("User found:", user)

        # Create the issue
        issue = Issue.objects.create(
            issued_by=user,
            title=title,
            description=description
        )

        print(f"Issue created with ID: {issue.id}")
        return f"Issue '{title}' has been successfully created with ID: {issue.id}."
    except User.DoesNotExist:
        print("User not found.")
        return "Error: User not found."
    except Exception as e:
        print(f"An error occurred: {e}")
        return f"Error: {str(e)}"


tools = [create_issue]