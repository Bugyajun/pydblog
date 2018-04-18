from __future__ import absolute_import, unicode_literals

from django.views import generic
from django.http import HttpRequest
from django import forms
from django.contrib.auth import authenticate,login
from blog import models
from django.template import RequestContext



class BlogAbout(generic.TemplateView):
    template_name = "blog/about.html"

    def get_context_data(self, **kwargs):
        context = super(BlogAbout, self).get_context_data(**kwargs)
        # import ipdb; ipdb.set_trace()
        context['about'] = models.About.objects.all().first()
        return context


class BlogIndex(generic.ListView):
    model = models.Entry
    template_name = "blog/index.html"
    paginate_by = 5


class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "blog/post.html"

    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)
        # slug = kwargs.get('slug')
        # context['post'] = models.Entry.objects.get(slug=slug)
        # import ipdb; ipdb.set_trace()
        return context


class BlogGallery(generic.ListView):
    model = models.Entry
    template_name = "blog/gallery.html"


def regist():
    pass









