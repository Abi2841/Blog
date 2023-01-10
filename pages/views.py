from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'pages/index.html')

def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    return render(request, 'pages/contact.html')

def thankyou(request):
    return render(request, 'pages/thankyou.html')