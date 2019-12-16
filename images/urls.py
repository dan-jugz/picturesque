from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,re_path
from . import views

urlpatterns = [
  path('',views.home,name='home'),
  re_path('^search_results$',views.search_results,name='search'),
]
if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)