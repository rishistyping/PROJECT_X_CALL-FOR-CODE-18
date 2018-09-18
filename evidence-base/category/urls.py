from django.conf.urls import include, url
from . import views


urlpatterns = [
    url('board/', views.view_category_board, name='board'),
]