from django.shortcuts import render

# Create your views here.
def home(request):
    template = 'school/home.html'
    context = {}
    return render(request,template,context)