from django.conf.urls import url

import blog.urls
from www.views import IndexView


urlpatterns = (
    url('^/$', IndexView.as_view()),
    url('^/blog/$', blog.urls)
)
