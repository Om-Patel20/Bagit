
from django.conf.urls import include
from django.urls import path
from .views import PursesListView, PursesDetailView, SearchResultsListView, PurseCheckoutView, paymentComplete


urlpatterns = [
    path('', PursesListView.as_view(), name = 'list'),
    path('<int:pk>/', PursesDetailView.as_view(), name = 'detail'),
    path('<int:pk>/checkout/', PurseCheckoutView.as_view(), name = 'checkout'),
    path('complete/', paymentComplete, name = 'complete'),
    path('search/', SearchResultsListView.as_view(), name = 'search_results'),
  
]