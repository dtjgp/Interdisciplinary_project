"""jiaocha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from drfapp01.views import user_view, cust_cons_total_view
from drfapp01.views import cust_cons_type_comb_view, contract_market_num_view, contract_market_share_view, contract_ms_withoutself_view, contract_ms_withself_view, profit_withoutself_view, profit_withself_view
from drfapp01.views import contract1_usertype_share_view, contract2_usertype_share_view, contract3_usertype_share_view, contract4_usertype_share_view, contract5_usertype_share_view
from drfapp01.views import specific_c1_number_view, specific_c2_number_view, specific_c3_number_view, specific_c4_number_view, specific_c5_number_view
from drfapp01.views import specific_c1_profit_view, specific_c2_profit_view, specific_c3_profit_view, specific_c4_profit_view, specific_c5_profit_view
from drfapp01.views import test_view, json_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("drfapp01/", include("drfapp01.urls")),
    path("togetnum/", cust_cons_type_comb_view, name="your-view"),
    path("test/", test_view, name="your-view"),

    path('user-url/', user_view, name='your-view'),
    path('cust_cons_type_comb/', cust_cons_type_comb_view, name='your-view'),
    path('cust_cons_total/', cust_cons_total_view, name='your-view'),
    path('contract_market_num/', contract_market_num_view, name='your-view'),
    path('contract_market_share/', contract_market_share_view, name='your-view'),
    path('contract_ms_withoutself/', contract_ms_withoutself_view, name='your-view'),
    path('contract_ms_withself/', contract_ms_withself_view, name='your-view'),
    path('profit_withoutself/', profit_withoutself_view, name='your-view'),
    path('profit_withself/', profit_withself_view, name='your-view'),
    path('contract1_usertype_share/', contract1_usertype_share_view, name='your-view'),
    path('contract2_usertype_share/', contract2_usertype_share_view, name='your-view'),
    path('contract3_usertype_share/', contract3_usertype_share_view, name='your-view'),
    path('contract4_usertype_share/', contract4_usertype_share_view, name='your-view'),
    path('contract5_usertype_share/', contract5_usertype_share_view, name='your-view'),
    path('specific_c1_number/', specific_c1_number_view, name='your-view'),
    path('specific_c2_number/', specific_c2_number_view, name='your-view'),
    path('specific_c3_number/', specific_c3_number_view, name='your-view'),
    path('specific_c4_number/', specific_c4_number_view, name='your-view'),
    path('specific_c5_number/', specific_c5_number_view, name='your-view'),
    path('specific_c1_profit/', specific_c1_profit_view, name='your-view'),
    path('specific_c2_profit/', specific_c2_profit_view, name='your-view'),
    path('specific_c3_profit/', specific_c3_profit_view, name='your-view'),
    path('specific_c4_profit/', specific_c4_profit_view, name='your-view'),
    path('specific_c5_profit/', specific_c5_profit_view, name='your-view'),
    
]
