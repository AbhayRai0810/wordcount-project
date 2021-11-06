from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def eggs(request):
    return HttpResponse('<h1>eggs are good for health</h1>')

def count(request):
    fulltext1 = request.GET['fulltext']
    wordlist = fulltext1.split()

    worddictionary = {}



    for word in wordlist:
        if word in worddictionary:
            #increse
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedword = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse = True)

    return render(request, 'count.html', {'fulltext': fulltext1, 'count': len(wordlist),'sortedword': sortedword})
