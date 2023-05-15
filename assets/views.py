from django.shortcuts import render


# Create your views here.
def asset(request):
    context = {'asset': 'active'}
    return render(request, 'assets/myassets.html',context)
