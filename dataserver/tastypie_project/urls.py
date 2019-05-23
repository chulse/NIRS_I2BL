from django.conf.urls import include, url
from django.contrib import admin
from apiengine.models import MessageModel
from apiengine import views
from rest_framework import routers
from rest_framework import serializers
from apiengine.api import MessageModelResource
from apiengine.views import MessageViewSet, MessageList
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import views as auth_views


admin.autodiscover()
message_resource = MessageModelResource()

router = routers.DefaultRouter()
router.register(r'api/messages', MessageViewSet, "base.py")


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^account/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api/data', MessageList.as_view(), name='data'),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^plots/pd1r1/', views.PD1R1, name = 'pd1r1'),
    #url(r'^plots/voutunfiltered/', views.VoutUnfiltered, name = 'voutunfiltered'),
    #url(r'^plots/voutfiltered/', views.VoutFiltered, name = 'voutfiltered'),
    #url(r'^plots/runfiltered/', views.resistanceUnfiltered, name = 'runfiltered'),
    #url(r'^plots/rfiltered/', views.resistanceFiltered, name = 'rfiltered'),
    
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^login/$', auth_views.LoginView.as_view(template_name="login.html"),
        name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(),
        name='logout'),
    url(r'^signup/$', TemplateView.as_view(template_name="signup.html"),
        name='signup'),
    url(r'^accounts/profile/$', RedirectView.as_view(url='/', permanent=True), name='profile-redirect'),
    url(r'^email-verification/$',TemplateView.as_view(template_name="email_verification.html"),name='email-verification'),
    url(r'^password-reset/$',
        TemplateView.as_view(template_name="password_reset.html"),
        name='password-reset'),
    url(r'^password-reset/confirm/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password-reset-confirm'),

    url(r'^user-details/$',
        TemplateView.as_view(template_name="user_details.html"),
        name='user-details'),
    url(r'^password-change/$',
        TemplateView.as_view(template_name="password_change.html"),
        name='password-change'),


    # this url is used to generate email content
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password_reset_confirm'),
]
