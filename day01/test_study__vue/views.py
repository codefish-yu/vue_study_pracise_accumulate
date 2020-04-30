from django.shortcuts import render

# Create your views here.
def v_cloak(request):
    return render(request,'v_cloak.html')