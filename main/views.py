from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, "index.html")

def submit(request):
    request.session['name'] = request.POST['name']
    request.session['email'] = request.POST['email']
    request.session['dojo_location'] = request.POST['location']
    request.session['fav_lang'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    request.session['computer'] = request.POST['computer']
    request.session['stack'] = request.POST.getlist('stack')
    return redirect("/result")

def result(request):
    
    return render(request, "result.html")




