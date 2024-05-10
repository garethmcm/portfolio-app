from django.urls import path
from dj_ango_app import views

app_name = 'dj_ango_app'

urlpatterns = [
	path('', views.index, name='index'),
]