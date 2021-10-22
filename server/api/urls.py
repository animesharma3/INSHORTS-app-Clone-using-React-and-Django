from django.urls import path
from . import views

urlpatterns = [
    path("api-overview/", views.apiOverview, name='api-overview'),
    path("get-top-headlines/country/<str:country>/", views.getTopHeadlinesForCountry),
    path("get-top-headlines/category/<str:category>/", views.getTopHeadlinesForCategory),
    path("search/<str:query>/<int:page>/", views.getEverythingRelatedToSearchQuery)
]
