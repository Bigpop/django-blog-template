from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View
from .models import Trans

from website.settings import BASE_DIR


class TransListView(ListView):
    model = Trans
    paginate_by = 10
    template_name = 'translation/translation_list.html'
    context_object_name = 'translations'


