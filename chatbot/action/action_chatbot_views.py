import json
import os

from langchain_core.messages import HumanMessage, AIMessage
from langgraph.checkpoint.memory import MemorySaver
from rest_framework.views import APIView
from rest_framework.response import Response
from chatbot.Graph.graph import Graph
from chatbot.CustomMemorySaver.postgres_memory_saver import PostgresMemorySaver
from chatbot.Tools.tools import retrieve_smartphone_data, create_issue, get_smartphone_data

memory = MemorySaver()
# class ChatBotAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#
#         if not request.session.session_key:
#             request.session.save()
#
#         session_id = request.session.session_key
#
#         graph = Graph().setup_graph(checkpoint=memory)
#
#         user_message = request.data.get('messages', '')
#         if not user_message:
#             return Response({"error": "No message provided"}, status=400)
#
#         config = {
#             "configurable": {
#                 "thread_id": session_id
#             }
#         }
#
#         human_message = HumanMessage(content=user_message)
#         user = request.user
#         user_information = {
#             "user_id": user.id,
#             "name": user.name,
#             "email": user.email
#         }
#         # print("user_information:", user_information)
#         response = graph.invoke({"messages": [human_message], "user_information": user_information}, config=config)
#         ai_response = response["messages"][-1].content
#         print("AI response: ", response["messages"][-1])
#
#         # print("length of state messages:", len(response["messages"]))
#         # print("summary: ", response.get("summary", "No summary available"))
#         return Response({"messages": ai_response}, status=200)


from RAGnificentAI import AgentParams, ChatAI
rag = ChatAI()
class ChatBotAPIView(APIView):
    def post(self, request, *args, **kwargs):

        if not request.session.session_key:
            request.session.save()

        session_id = request.session.session_key
        user_message = request.data.get('messages', '')
        if not user_message:
            return Response({"error": "No message provided"}, status=400)

        user = request.user
        user_information = {
            "user_id": user.id,
            "name": user.name,
            "email": user.email
        }
        system_prompt = f"""You are Shoppio, an AI assistant designed to help users with their shopping-related needs.
- Always follow the instructions carefully. You can use tools when appropriate.
- When the user asks about smartphones, use the `retrieve_smartphone_data` tool. Note that all smartphone prices are in BDT (Bangladeshi Taka).
- Only create an issue if the user explicitly requests it.
- If the user encounters a problem or you don’t have the necessary access to complete a task, politely ask if they would like to create an issue for it.
- If an issue has already been created, apologize for the inconvenience and confirm that the issue has been successfully submitted. Be sure to mention the issue title in your response."""

        summary_prompt = f"""You are a summarizer that condenses the conversation into a concise summary."""
        tools = [create_issue, get_smartphone_data]
        agentParams = AgentParams(
            model="gemini-2.0-flash-lite",
            api_key=os.getenv("GEMINI_API_KEY"),
            base_url=os.getenv("GEMINI_API_BASE_URL"),
            system_prompt=system_prompt,
            summary_prompt=summary_prompt,
            thread_id=session_id,
            tools=tools,
            user_information=user_information
        )
        shoppio = rag.initiate_chatbot(params=agentParams)
        # print("user_information:", user_information)
        response = shoppio.run(messages=user_message)
        print("AI response: ", response)

        # print("length of state messages:", len(response["messages"]))
        # print("summary: ", response.get("summary", "No summary available"))
        return Response({"messages": response}, status=200)
