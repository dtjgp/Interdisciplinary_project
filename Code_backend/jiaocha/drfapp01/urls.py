from django.urls import path
from . import views


urlpatterns = [

    path('toGetNum/', views.toGetNum_view),
    path('testjson/', views.json_view, name='json'),
    


]