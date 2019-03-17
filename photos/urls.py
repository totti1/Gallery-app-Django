from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from gallery import settings

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^photo/(\d+)',views.photo,name ='photo'),
    url(r'^link/(\d+)',views.get_link,name ='get_link')
    # url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    # url(r'^search/', views.search_results, name='search_results'),
    # url(r'^article/(\d+)',views.article,name ='article')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)