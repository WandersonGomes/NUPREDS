from django.shortcuts import render, redirect
from core.models import Calculation

# Create your views here.
def page_calculator(request):
    calculations = Calculation.objects.all().order_by("-id")
    return render(request, "index.html", {'calculations': calculations})

def calc(request):
    expression = request.GET.get('visor')
    
    if expression:
        result = ''

        try:
            result = eval(expression)
        except:
            result = 'invalid'

        Calculation.objects.create(expression=expression, result=result)

    return redirect("/")

def clear_historic(request):
    Calculation.objects.all().delete()
    return redirect("/")