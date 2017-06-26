from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.activity_list, name='list'),
    url(r'^availability/$', views.availability_page, name="availability"),
    url(r'(?P<activity_pk>\d+)/(?P<package_pk>\d+)/$', views.package_detail, name='package'),
    url(r'create_activity/$', views.activity_create, name='create_activity'),
    url(r'create_person/$', views.availability_create, name='create_person'),
    url(r'create_package/$', views.package_create, name='create_package'),
    url(r'(?P<pk>\d+)/$', views.activity_detail, name='detail'),
]
