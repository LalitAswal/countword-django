from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):

    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()
    dic = {}
    for word in words:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(words), 'dic': dic.items()})


