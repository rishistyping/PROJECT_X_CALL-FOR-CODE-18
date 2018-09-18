from django.conf.urls import include, url
from .views import AddBoardView

urlpatterns = [
    url('create/', AddBoardView.as_view()),
]