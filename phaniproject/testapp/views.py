from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')
def shirts_view(request):
    return render(request,'testapp/shirts.html')
def watches_view(request):
    return render(request,'testapp/watches.html')
def mobiles_view(request):
    return render(request,'testapp/mobiles.html')
def buds_view(request):
    return render(request,'testapp/buds.html')
