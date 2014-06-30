from django.conf.urls import patterns, include, url


#for admin 
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', 'app2.views.hora_actual', name ='hora_actual'),
	url(r'^$', 'app2.views.home', name ='home'),
	url(r'^plus/(\d+)$', 'app2.views.plus', name ='plus'),
	url(r'^minus/(\d+)$', 'app2.views.minus', name ='minus'),
    url(r'^admin/', include(admin.site.urls)), 
 
)
