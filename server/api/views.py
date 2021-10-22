from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import scrape

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        "Get Top Headlines for some country": "/get-top-headlines/:country",
        "Get Top Headlines for some category": "/get-top-headlines/:category/",
        "Get Everything related to search query": "/search/:query/:page/"
    }
    return Response(api_urls)

@api_view(["GET"])
def getTopHeadlinesForCountry(request, country):
    articles = scrape.getTopHeadlinesForCountry(country=country)
    return Response(articles)

@api_view(["GET"])
def getTopHeadlinesForCategory(request, category):
    articles = scrape.getTopHeadlinesForCategory(category=category)
    return Response(articles)

@api_view(['GET'])
def getEverythingRelatedToSearchQuery(request, query, page=1):
    articles = scrape.getEverythingRelatedToSearchQuery(query=query, page=page)
    return Response(articles)