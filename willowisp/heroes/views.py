# from django.shortcuts import render

# def home_page(request):
    # return render(request, 'heroes/home_page.html')

# def cloud(request):
    # return render(request, 'heroes/detail_cloud.html')

# def jester(request):
    # return render(request, 'heroes/detail_jester.html')

# def sunflowey(request):
    # return render(request, 'heroes/detail_sunflowey.html')

from django.views.generic.base import TemplateView

class HomeView(TemplateView):
	template_name = 'home.html'

class CloudView(TemplateView):
	template_name = 'detail_cloud.html'
	
class JesterView(TemplateView):
	template_name = 'detail_jester.html'
	
class SunfloweyView(TemplateView):
	template_name = 'detail_sunflowey.html'