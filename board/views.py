from datetime import datetime, timedelta

from django import forms
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse
from django.shortcuts import render

from .models import Board


class BoardForm(forms.Form):
    title = forms.CharField(max_length=255)
    content = forms.CharField(max_length=2000)


def create_board(request):
    f = BoardForm(request.POST)
    if not f.is_valid():
        raise HttpResponseBadRequest()
    new_board = Board(title=request.POST["title"], content=request.POST["content"])
    new_board.save()
    return HttpResponse()


def get_board(request):
    a_week_ago = datetime.now() - timedelta(days=7)
    Board.objects.filter(date__lte=a_week_ago).DELETE()
    board = Board.objects.all()
    return JsonResponse({data: board})


def board_render(request):
    return render(request, "board/board.html")
