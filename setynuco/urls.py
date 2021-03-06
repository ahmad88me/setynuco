"""setynuco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import views
urlpatterns = [
    url('model_add', views.ModelAdd.as_view()),
    url('model_list', views.model_list),
    url('prediction_add', views.PredictionAdd.as_view()),
    url('prediction_list', views.prediction_list),
    url('clusters_for_prediction', views.clusters_for_prediction),
    # url('draw_model', views.draw_model),
    url(r'^admin/', admin.site.urls),
    url('', views.home),
]
