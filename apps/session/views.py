from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if 'logs' not in request.session:
        request.session['logs'] = []
    return render(request, 'session/index.html')

def add_new(request):
    if 'font' not in request.POST:
        font = 'False'
    else:
        font = request.POST['font']
    if 'colors' not in request.POST:
        color = 'black'
    else:
        color = request.POST['colors']
    style = {
        'word' : request.POST['word'],
        'colors' : color,
        'font' : font
    }
    logs = request.session['logs']
    logs.append(style)
    request.session['logs'] = logs 
    return redirect("/session_word")

def reset(request):
    return redirect("/")