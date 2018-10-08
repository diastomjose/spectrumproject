from django .conf.urls import url
# from customer.views import 

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from customer.views import index,RegisterCustomer,LoginView

urlpatterns = [
	url(r'^index/',index.as_view(),name='index'),

	url(r'^customer/',index.as_view(),name='customer'),

	url(r'^$',index.as_view(),name='home'),

	url(r'^register/',RegisterCustomer.as_view(),name = 'register'),

	url(r'^login/',LoginView.as_view(),name = 'login'),

]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)