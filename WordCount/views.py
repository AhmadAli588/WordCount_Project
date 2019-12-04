from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,"home.html")
def count(request):
    text=request.GET["fulltext"]
    Wordlist=text.split()
    countWord={}
    for word in Wordlist:
        if word in countWord:
            countWord[word]+=1
        else:
            countWord[word]=1

    return render(request,"count.html",{"text":text,"count":len(Wordlist),"Wordcount":countWord})