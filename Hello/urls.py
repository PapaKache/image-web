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
    #url(r'^update_next$', entry.update_next),
    #url(r'^update_pre$', entry.update_pre),
    url(r'^type_get$', entry.type_get),
    url(r'^type_add$', entry.type_add),
    url(r'^login$', entry.login),
    url(r'^register$', entry.register),
    url(r'^upload$', entry.upload),
    url(r'^entry$', entry.main),
    url(r'^update_image$', entry.update_image),
    #path(r'^fuck$', search.fuck),
]
