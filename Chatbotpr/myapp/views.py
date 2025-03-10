from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import ChatHistory
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Setup LangChain model
template = '''
answer the question below

here is the conversation history:{context}

Question:{question}

Answer:
'''
model = OllamaLLM(model="gemma:2b") #mistral mera gemma hai so minea gemma diya aap ka mistral hotooo mistral doo.
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def chatbot_view(request):
    return render(request, "index.html")

def chat(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        
        # Retrieve previous context
        history = ChatHistory.objects.all().order_by("-timestamp")[:5]
        context = "\n".join([f"User: {h.user_input}\nLahari: {h.bot_response}" for h in history])

        # Generate response
        result = chain.invoke({"context": context, "question": user_input})
        
        # Save conversation
        ChatHistory.objects.create(user_input=user_input, bot_response=result)

        return JsonResponse({"user_input": user_input, "bot_response": result})
    
def chat_history(request):
    history = ChatHistory.objects.all().order_by("-timestamp")
    return JsonResponse({"history": [{"user": h.user_input, "bot": h.bot_response} for h in history]})
