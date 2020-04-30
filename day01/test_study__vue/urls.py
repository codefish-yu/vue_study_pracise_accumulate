from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^v_cloak$',views.v_cloak)
]