from django.urls import path
from google_places import views

urlpatterns = [
    path('search/', views.PlacesTextSearchView.as_view(), name='places-search-list'),
]
