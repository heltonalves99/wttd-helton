from django.conf.urls import url

from .views import subscribe
from .views import detailSubscribe

urlpatterns = [
    url(r'^$', subscribe, name='create-inscription'),
    url(r'^(?P<pk>\d+)/$', detailSubscribe, name='detail-inscription'),
]