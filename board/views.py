from datetime import datetime, timedelta

from django import forms
from django.utils import timezone
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from .models import Board


class BoardForm(forms.Form):
    title = forms.CharField(max_length=255)
    content = forms.CharField(max_length=2000)


@csrf_exempt
def create_board(request):
    print(request.POST)
    f = BoardForm(request.POST)
    if not f.is_valid():
        return HttpResponseBadRequest()
    new_board = Board(title=request.POST["title"], content=request.POST["content"])
    new_board.save()
    return HttpResponse()


@csrf_exempt
def get_board(request):
    a_week_ago = timezone.localtime() - timedelta(days=7)
    Board.objects.filter(date__lte=a_week_ago).delete()
    board = Board.objects.order_by("-date")
    return JsonResponse({"data": list(board.values())})


def board_render(request):
    return render(request, "board/board.html")
