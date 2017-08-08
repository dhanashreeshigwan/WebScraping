from django.shortcuts import render
from django.views import View
from django.core.cache import cache

# Create your views here.

class IndexView(View):
    template_name = "get_web_details.html"

    def get(self, request):
        html_data = cache.get('nifty_50_table')
        return render(request, self.template_name, {'html': html_data})
