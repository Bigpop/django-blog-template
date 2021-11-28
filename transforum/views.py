from django.shortcuts import render
from .models import TransTreeNode
# Create your views here.


class TransTree():
    model = TransTreeNode
    
    template_name = 'transforum/trans_tree.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.order_by('-c_time')


def trans_tree(request):
    ctx = {}
    trans_objs = TransTreeNode.objects.order_by('-likes')
    for obj in trans_objs:
        if obj.parent_id==-1 and obj
        if obj.id in ctx:
            ctx[obj.id].append()

    return render(request, 'article/about.html',template_name=ctx)
