from django.urls import path
from .views import *

urlpatterns = [
    path('',CountryView.as_view(), name = 'country'),
    path('<int:id>/',CountryView.as_view(), name = 'country'),
    path('update/<int:id>/',UpdateCountryView.as_view(), name = 'updatecountry'),

    # State urls
    path('state/<int:id>/',StateView.as_view(), name='state'),
    path('stateupadte/<int:id>/', UpadtestateView.as_view(), name='updatestate'),

    # City urls
    path('city/<int:id>/',CityView.as_view(), name='city'),

]