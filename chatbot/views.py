from rest_framework.views import APIView
from rest_framework.response import Response
from chatbot.LLM.groqLLM import GroqLLM
from chatbot.Graph.graph import Graph

llm = GroqLLM().get_llm()
graph = Graph(llm).setup_graph()
class ChatBotView(APIView):
    """
    A view to handle chatbot interactions.
    This view will process user messages and return responses.
    """

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to the chatbot endpoint.
        Expects a JSON payload with user input.
        """
        user_message = request.data.get('messages', '')

        if not user_message:
            return Response({"error": "No message provided"}, status=400)


        response = graph.invoke({"messages": [user_message]})
        ai_response = response["messages"][-1].content

        return Response({
            "messages": ai_response
        }, status=200)
