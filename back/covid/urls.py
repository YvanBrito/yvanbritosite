from django.urls import include, path, re_path
from covid import views


urlpatterns = [
    path('global', views.globalCases, name='cases'),
    path('brasil', views.brasilCases, name='brasilCases'),
    path('para', views.globalCases, name='cases'),
    path('worldregions', views.worldregions, name='worldregions'),
    path('toptenconfirmed', views.toptenconfirmed, name='toptenconfirmed'),
    path('updateDate', views.updateDate, name='updateDate'),
]