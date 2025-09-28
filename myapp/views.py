from django.shortcuts import render
import operator
from .counter import count
def home(request):
    return render(request, "myapp/home.html")   # include app folder name

def result(request):
    article = request.GET.get("article")
    word_count, var_dict = count(article)


    context = {"name": "Ali", "subject": "Math", "marks": 85, "status": "Pass", "article": article, "word_count": word_count, "dict_words": var_dict}
    return render(request, "myapp/result.html", context)
