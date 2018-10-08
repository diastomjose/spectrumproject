from django .conf.urls import url

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from booking.views import PackagePriceView,BookedUserView,generate_pdf,DownloadView

urlpatterns = [

	url(r'^packageprice/',PackagePriceView.as_view(),name = 'packageprice' ),
	url(r'^booked/',BookedUserView.as_view(),name= 'booked'),
		url(r'^reciept/',generate_pdf,name= 'reciept'),
		url(r'^download/',DownloadView.as_view(),name= 'download'),





]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)