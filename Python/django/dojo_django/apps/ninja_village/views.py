from django.shortcuts import render

# Create your views here.
def ninja_village(request):
    return render(request, 'ninja_village/ninja_village.html')
