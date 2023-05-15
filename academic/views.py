from django.shortcuts import render


# Create your views here.
def academy(request):
    context = {'academic': 'active'}
    return render(request, 'academic/academics.html',context)
