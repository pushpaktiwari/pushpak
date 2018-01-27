from django.urls import path
from . import views

# from polls.views import index
# from polls import views
# from . import views


urlpatterns = [
	path('', views.index, name="index")
]