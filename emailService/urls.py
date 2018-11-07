from django.conf.urls import patterns, url
from . import views


email_urls = patterns (
    '',
    url(r'^singleEmail/$',views.singleEmail),
    url(r'^bulkEmail/$',views.bulkEmail),
    url(r'^statsApi/$',views.cronApi),
)
