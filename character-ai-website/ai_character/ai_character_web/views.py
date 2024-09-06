from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .llm import CharacterAI
import threading

MODELS = ["keqing", "yae", "ganyu", "hutao", "ei"]

def home(request):
    return render(request, "ai_character_web/index.html")

def to_page(request):
    page_name = request.GET.get("page_name", "").strip().lower()
    if page_name in MODELS:
        return render(request, f"ai_character_web/{page_name}.html")
    else:
        return HttpResponse("đã có lỗi! vui lòng chọn tên mô hình khả dụng")

def llm_response(request):
    global llm_model_name
    global llm_model
    inp = request.GET.get("input")
    model = request.GET.get("model")
    contexts = request.GET.get("contexts")
    print(contexts)
    if not inp or not model:
        return JsonResponse({"error": "Missing input or model parameter"}, status=400)
    
    if model in "keqing":
        llm_model = CharacterAI("d8a092f270dfc8baa0a2aa9a273b1aec398f7af3", "pwygUrHOY2vxTzVbyOTUBwuUWeLhNyu67wsKarkWViE")
        contexts = contexts.replace("charxxx", "Context Output").replace("userxxx", "Context Input")
        response = llm_model.send_message(contexts +" Current Input: "+inp)
        return JsonResponse({"response": response})
    
    elif model in "yae":
        llm_model = CharacterAI("d8a092f270dfc8baa0a2aa9a273b1aec398f7af3", "Dvm_7p9ea1uPKtENq18-tjJqHpFkdmP-nFreeGx00s0")
        contexts = contexts.replace("charxxx", "Context Output").replace("userxxx", "Context Input")
        response = llm_model.send_message(contexts +" "+inp)
        return JsonResponse({"response": response})
    
    elif model in "ganyu":
        llm_model = CharacterAI("d8a092f270dfc8baa0a2aa9a273b1aec398f7af3", "I3OCwWQKKEj12lt3mpLvHRyrBdXgotqVUHg0MzAGmSk")
        contexts = contexts.replace("charxxx", "Context Output").replace("userxxx", "Context Input")
        response = llm_model.send_message(contexts +" "+inp)
        return JsonResponse({"response": response})
    
    elif model in "hutao":
        llm_model = CharacterAI("d8a092f270dfc8baa0a2aa9a273b1aec398f7af3", "UXcPdzizz8tK7x7Gbao4b4zwjewTpJFbT8SYDZJqaK4")
        contexts = contexts.replace("charxxx", "Context Output").replace("userxxx", "Context Input")
        response = llm_model.send_message(contexts +" "+inp)
        return JsonResponse({"response": response})

    elif model in "ei":
        llm_model = CharacterAI("d8a092f270dfc8baa0a2aa9a273b1aec398f7af3", "jVHsAJ3BNjtP6llYYEb94t2CMh9RhgCgOopEQ0OeUyY")
        contexts = contexts.replace("charxxx", "Context Output").replace("userxxx", "Context Input")
        response = llm_model.send_message(contexts +" "+inp)
        return JsonResponse({"response": response})

    else:
        return HttpResponse("Đã có lỗi!")