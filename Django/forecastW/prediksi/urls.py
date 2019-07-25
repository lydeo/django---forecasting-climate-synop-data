from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^temp_rata', views.temp_rata),
    url(r'^temp_max', views.temp_max),
    url(r'^temp_min', views.temp_min),
    url(r'^curah_hujan', views.curah_hujan),
    url(r'^penyinaran_matahari', views.penyinaran_matahari),
    url(r'^tekanan_udara', views.tekanan_udara),
    url(r'^kelembaban', views.kelembaban),
    url(r'^kec_angin', views.kec_angin),

]