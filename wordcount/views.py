from django.http import HttpResponse
#for templates
from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')  #HttpResponse("Hello eggs")

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    wordcount = {}
    for i in wordlist:
        if i in wordcount.keys():
            wordcount[i] += 1
        else:
            wordcount[i] = 1
    return render(request, 'count.html',{'fulltext':fulltext,'wordlist':len(wordlist),'wordcount':wordcount.items()})

def aboutpage(request):
    return render(request, 'aboutpage.html')
