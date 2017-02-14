from django.conf.urls import url, include

from www.views import IndexView


urlpatterns = (
    url(r'^/$', IndexView.as_view()),
    url(r'^/blog/$', include('blog.urls'))
)
