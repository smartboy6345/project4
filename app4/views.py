from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wipro(request):
    return HttpResponse('<h1><marquee>Today i have Attend the interview in Wipro and i have selected for the interview and i got mail from company</h1></marquee>')