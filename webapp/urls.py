from django.urls import path
from . import views


urlpatterns = [
    path("", views.AllModelsViews.as_view(), name='allmodelsviews'),
]