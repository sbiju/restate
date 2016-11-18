from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('my_account.urls')),
    url(r'^accounts/', include('allauth.urls')),
    # url('social-auth/', include('social.apps.django_app.urls', namespace='social')),
]