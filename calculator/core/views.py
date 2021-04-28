from django.shortcuts import render

# Create your views here.
def page_calculator(request):
    return render(request, "index.html")