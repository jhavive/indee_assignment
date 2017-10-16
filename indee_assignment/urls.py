from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from todo import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.SimpleRouter()
# router.register(r'sales', views.ProductsViewSet, 'base_name')
# urlpatterns = router.urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'indee_assignment.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),

	# url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
  	# url(r'^', include(router.urls)),
    url(r'^$', views.Login.as_view(),name="login"),
    url(r'^category/$', views.Category.as_view(),name="category"),
    url(r'^signup/$', views.CreateUser.as_view(),name="CreateUser"),
    url(r'^logout/$', views.logout_view,name="CreateUser"),
]+ staticfiles_urlpatterns()
# ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
