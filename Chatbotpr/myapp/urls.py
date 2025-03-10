from django.urls import path
from .views import chatbot_view,chat,chat_history

urlpatterns=[
    path("",chatbot_view,name="Chatbot"),
    path("chat/",chat, name="chat"),
    path("history/",chat_history,name="history")
]