from django.shortcuts import render
from django.views.generic import TemplateView


class WindowDetailView(TemplateView):
    """Display a windows with mimics"""
    template_name = 'windows/window_detail.html'
