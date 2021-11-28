from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View

from .models import Whisper

from website.settings import BASE_DIR


class WhisperList(ListView):
    model = Whisper
    paginate_by = 10
    template_name = 'whisper/whisper_list.html'
    context_object_name = 'whispers'

    def get_queryset(self):
        return Whisper.objects.order_by('-c_time')


def test(request):
    obj = Whisper.objects.order_by('-c_time')
    print(len(obj))
    return render(request, 'whisper/whisper_test.html', context={'whispers':obj})
