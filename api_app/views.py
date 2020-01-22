from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

def index(request):
    return render(request, 'index.html')

@api_view(['POST'])
@csrf_exempt
def api_req(request):
    post_data = request.data["text"]
    post_data_no_spaces = post_data.replace(" ","")
    words = post_data.split(" ")
    word_count = 0
    for i in words:
        if i:
            word_count += 1
    char_count = {}
    for ch in sorted(list(post_data_no_spaces)):
        if ch.isalpha():
            try:
                char_count[ch] += 1
            except KeyError:
                char_count[ch] = 1
    char_count_list = []
    for key in char_count:
        char_count_list.append({key:char_count[key]})
    if request.method == "POST":
        return Response({"textLength":
                            {"withSpaces": len(post_data),
                             "withoutSpaces": len(post_data_no_spaces)},
                         "wordCount": word_count,
                          "characterCount": char_count_list})
    else:
        return render("API Root")
