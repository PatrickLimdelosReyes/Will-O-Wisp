from django.conf.urls import url
from .views import HomeView, CloudView, JesterView, SunfloweyView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name = 'home'),
    url(r'^heroes/$', HomeView.as_view(), name = 'home'),
    url(r'^hero/cloud$', CloudView.as_view(), name = 'cloud'),
    url(r'^hero/jester$', JesterView.as_view(), name = 'jester'),
    url(r'^hero/sunflowey$', SunfloweyView.as_view(), name = 'sunflowey'),
]

