from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from . import models

def index(request):
    if 'dict' not in request.session:
        request.session['dict'] = []
    return render(request, 'session_words_app/index.html')

def process(request):

    pWord = request.POST['word']
    pTime = strftime("%I:%M:%S%p, %B %d, %Y", gmtime())
    pColor = request.POST["color"]
    pFont = request.POST["font"]

    temp_list = request.session['dict']
    temp_list.insert(0, {'word': pWord, 'time': pTime, 'color': pColor, 'font': pFont})
    request.session['dict'] = temp_list

    return redirect('/')

def reset(request):
    if 'dict'in request.session:
        request.session.clear()
    return redirect('/')