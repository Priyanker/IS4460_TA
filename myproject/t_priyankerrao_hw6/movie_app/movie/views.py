from django.views import View
from django.shortcuts import render, redirect
from . import db_populate

class HomePageView(View):

    template_name = 'hw6/index.html'

    def get(self, request):
        db_populate.perform_db_operations()
        return render(request, 'hw6/index.html', {})
