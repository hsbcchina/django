from django.conf.urls import url
from users import views
from django.views.generic import TemplateView
urlpatterns = [

    url('^$', TemplateView.as_view(template_name='index.html'),name='index'),
    url(r'^login/$', views.login,name='login'),
]