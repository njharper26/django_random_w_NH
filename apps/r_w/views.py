from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if not 'count' or not 'random' in request.session:
        request.session['count'] = 1
        request.session['random'] = 'Click the Generate buttom to generate a random word'
        return render(request, 'r_w/index.html')
    else:
        request.session['count'] += 1
        request.session['random'] = get_random_string(length=14)
        print request.session['random']
        return render(request, 'r_w/index.html')

def process(request):
    if request.method == 'POST':
        return redirect('/')

def reset(request):
    if request.method == 'POST':
        try:
            del request.session['count']
            del request.session['random']
            return redirect('/')
        except:
            return redirect('/')
