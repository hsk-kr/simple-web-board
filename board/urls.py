from django.urls import path
from .views import create_board, get_board, board_render

urlpatterns = [
    path("create_board", create_board),
    path("get_board", get_board),
    path("", board_render),
]
