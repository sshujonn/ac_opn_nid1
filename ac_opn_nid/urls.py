"""ac_opn_nid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ac_openning import views as acopn_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', acopn_views.NIDCardScriptLand.as_view(), name='card_script'),
    path('show-data/', acopn_views.ShowAllData.as_view(), name='show_data'),
    path('form-fillup/', acopn_views.FormFillup.as_view(), name='form_fillup'),
]
