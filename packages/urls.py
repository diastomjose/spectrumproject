from django .conf.urls import url
# from customer.views import 

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from packages . views import PackagesView,PlaceListView,AddPackagesView,AddPlacesView


urlpatterns = [

	url(r'^packages/',PackagesView.as_view(),name='packages'),
	url(r'^places/',PlaceListView.as_view(),name='places'),
	url(r'^addpackages/',AddPackagesView.as_view(),name='addpackages'),

	url(r'^addplaces/',AddPlacesView.as_view(),name='addplaces'),

]




urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)