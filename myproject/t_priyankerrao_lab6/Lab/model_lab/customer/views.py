from django.views import View
from django.shortcuts import render, redirect
from . import scratch

class HomePageView(View):

    template_name = 'lab6/index.html'

    def get(self, request):
        scratch.perform_db_operations()
        return render(request, 'lab6/index.html', {})
