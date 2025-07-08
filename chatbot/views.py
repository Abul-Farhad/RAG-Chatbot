from django.shortcuts import render
from django.views import View

class ChatBotView(View):
    def get(self, request):
        """
        Render the chatbot interface.
        This method will return the HTML template for the chatbot.
        """
        return render(request, 'chatbot.html')