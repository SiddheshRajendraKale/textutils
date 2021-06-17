# i have created django file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # variable la template la pathavane
    params = {'name':'siddhesh','place':'USA'}
    return render(request,"index2.html",params)

    # return HttpResponse("<h1>Home<h1>")

def removepunc(request):
    # // text la view madhe aanyasathi get request chya text la access karane
    djparams = request.POST.get('text', 'default')
    print(djparams)
    removpunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    print(removpunc)
    if (removpunc == 'on'):
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*~'''
        analyzed = ""
        for char in djparams:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punction', 'analyzed_text': analyzed}
        return render(request,'analyze.html',params )
    elif (uppercase == 'on'):
        analyzed = ""
        for char in djparams:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Removed Punction', 'analyzed_text': analyzed}
        return render(request,'analyze.html',params )
    elif (spaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djparams):
            if djparams[index] == " " and djparams[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punction', 'analyzed_text': analyzed}
        return render(request,'analyze.html',params )
        


    else:
        return HttpResponse("<h1>Error<h1>")

    

def capfirst(request):
    return HttpResponse("<h1>capfirst<h1>")

def newlineremove(request):
    return HttpResponse("<h1>newlineremove<h1>")

def spaceremover(request):
    return HttpResponse("<h1>Spaceremover<h1>")

def charcount(request):
    return HttpResponse("<h1>Charcount<h1>")

# def about(request):
#     return HttpResponse("About Siddhesh Kale")
    
    