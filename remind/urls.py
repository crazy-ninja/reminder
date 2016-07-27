from django.conf.urls import url, patterns

urlpatterns = patterns(
    'remind.views',
    url(r'^api/remind-me/$', 'remind_me', name='remind-me'),
)
