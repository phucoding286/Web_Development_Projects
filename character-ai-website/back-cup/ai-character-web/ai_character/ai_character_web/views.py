from django.shortcuts import render, redirect
from django.http import HttpResponse
import threading
from .llm import CharacterAI
# Create your views here.

account_token = "d8a092f270dfc8baa0a2aa9a273b1aec398f7af3"

keqing_token = "pwygUrHOY2vxTzVbyOTUBwuUWeLhNyu67wsKarkWViE"
yae_token = "Dvm_7p9ea1uPKtENq18-tjJqHpFkdmP-nFreeGx00s0"
ganyu_token = "I3OCwWQKKEj12lt3mpLvHRyrBdXgotqVUHg0MzAGmSk"
hutao_token = "UXcPdzizz8tK7x7Gbao4b4zwjewTpJFbT8SYDZJqaK4"
ei_token = "jVHsAJ3BNjtP6llYYEb94t2CMh9RhgCgOopEQ0OeUyY"

# ai_model = None
# char_name = None
# def check_charname():
#     global ai_model
#     while True:
#         if char_name is not None:
#             if char_name == "keqing":
#                 ai_model = CharacterAI(keqing_token, account_token)
#             elif char_name == "ganyu":
#                 ai_model = CharacterAI(ganyu_token, account_token)
#             elif char_name == "hutao":
#                 ai_model = CharacterAI(hutao_token, account_token)
#             elif char_name == "ei":
#                 ai_model = CharacterAI(ei_token, account_token)
#             elif char_name == "yae":
#                 ai_model = CharacterAI(yae_token, account_token)
#             break
            
# threading.Thread(target=check_charname).start()

def home(request):
    return render(request, "ai_character_web/index.html")

def keqing_view(request):
    return render(request, "ai_character_web/keqing.html")

def ganyu_view(request):
    return render(request, "ai_character_web/ganyu.html")

def ei_view(request):
    return render(request, "ai_character_web/ei.html")

def yae_view(request):
    return render(request, "ai_character_web/yae.html")

def hutao_view(request):
    return render(request, "ai_character_web/hutao.html")

# def to_page(request):
#     global char_name
#     page_name = request.GET.get("page_name")
#     page_name = str(page_name).replace("}","").strip().lower()
#     if page_name == "keqing":
#         print("yes")
#         return redirect("keqing_view")
#     elif page_name == "ganyu":
#         return redirect("ganyu_view")
#     elif page_name == "ei":
#         return redirect("ei_view")
#     elif page_name == "yae":
#         char_name = page_name
#         return redirect("yae_view")
#     elif page_name == "hutao":
#         return redirect("hutao_view")