from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mypoject.views.home', name='home'),
    url(r'^articles/get/(?P<product_id>\d+)/$', 'article.views.article'),
    url(r'^articles/get_category/(?P<category_id>\d+)/$', 'article.views.categorys_product_display'),
    url(r'^contacts/$', 'article.views.get_contacts_page'),
    url(r'^delivery/$', 'article.views.get_delivery_page'),
    url(r'^discounts/$', 'article.views.get_discounts_page'),
    url(r'^$', 'article.views.articles'),
    )+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
