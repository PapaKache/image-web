from django.urls import path
from django.conf.urls import url
from . import views
from . import search
from . import entry

urlpatterns = [
    #url(r'^sfs$', search.search_form),
    #url(r'^search$', search.search),
    #url(r'^fuck$', search.fuck),
    #path('runoob/', views.runoob),
    #path('sfss/', search.search_form),
    #url(r'^search-post$', search.search_post),
    url(r'^upload$', entry.upload),
    url(r'^entry$', entry.main),
    url(r'^upload_image$', entry.update_image),
    #path(r'^fuck$', search.fuck),
]
