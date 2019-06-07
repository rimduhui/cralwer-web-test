from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import crawl_test

def index(request):

    titles = crawl_test.get_titles()
    return HttpResponse(titles)
