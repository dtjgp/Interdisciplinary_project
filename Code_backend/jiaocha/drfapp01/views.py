from django.shortcuts import render
from .models import Publish
from django.http import JsonResponse
from .models import auth_user
from .models import cust_cons_type_comb, cust_cons_total
from .models import contract_market_num , contract_market_share
from .models import contract_ms_withoutself, contract_ms_withself, profit_withoutself, profit_withself
from .models import contract1_usertype_share, contract2_usertype_share, contract3_usertype_share, contract4_usertype_share, contract5_usertype_share
from .models import specific_c1_number, specific_c2_number, specific_c3_number, specific_c4_number, specific_c5_number
from .models import specific_c1_profit, specific_c2_profit, specific_c3_profit, specific_c4_profit, specific_c5_profit
from .models import test_test
import json
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime

class CustomJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)
    
def toGetNum_view(request):
    return render(request, 'togetnum.html')

# from rest_framework import serializers
# from rest_framework.generics import GenericAPIView
# from rest_framework.response import Response

# class PublishSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Publish
#         fields = "__all__" 

def user_view(request):
    user_data = auth_user.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(user_data),cls=CustomJSONEncoder)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False)

def cust_cons_type_comb_view(request):
    cust_cons_type_comb_data = cust_cons_type_comb.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(cust_cons_type_comb_data),)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False)

def cust_cons_total_view(request):
    cust_cons_total_data = cust_cons_total.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(cust_cons_total_data),)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False)

def contract_market_num_view(request):
    contract_market_num_data = contract_market_num.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(contract_market_num_data),)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False)

def contract_market_share_view(request):
    contract_market_share_data = contract_market_share.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(contract_market_share_data),)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False)

def contract_ms_withoutself_view(request):
    contract_ms_withoutself_data = contract_ms_withoutself.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(contract_ms_withoutself_data),)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False)

def contract_ms_withself_view(request):
    contract_ms_withself_data = contract_ms_withself.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(contract_ms_withself_data),)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False)

def profit_withoutself_view(request):
    profit_withoutself_data = profit_withoutself.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(profit_withoutself_data),)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False)

def profit_withself_view(request):
    profit_withself_data = profit_withself.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(profit_withself_data),)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False)

def contract1_usertype_share_view(request):
    contract1_usertype_share_data = contract1_usertype_share.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(contract1_usertype_share_data),)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False)

def contract2_usertype_share_view(request):
    contract2_usertype_share_data = contract2_usertype_share.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(contract2_usertype_share_data),)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False)

def contract3_usertype_share_view(request):
    contract3_usertype_share_data = contract3_usertype_share.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(contract3_usertype_share_data),)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False)

def contract4_usertype_share_view(request):
    contract4_usertype_share_data = contract4_usertype_share.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(contract4_usertype_share_data),)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False)

def contract5_usertype_share_view(request):
    contract5_usertype_share_data = contract5_usertype_share.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(contract5_usertype_share_data),)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False)

def specific_c1_number_view(request):
    specific_c1_number_data = specific_c1_number.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(specific_c1_number_data),)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False)

def specific_c2_number_view(request):
    specific_c2_number_data = specific_c2_number.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(specific_c2_number_data),)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False)

def specific_c3_number_view(request):
    specific_c3_number_data = specific_c3_number.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(specific_c3_number_data),)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False)

def specific_c4_number_view(request):
    specific_c4_number_data = specific_c4_number.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(specific_c4_number_data),)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False)

def specific_c5_number_view(request):
    specific_c5_number_data = specific_c5_number.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(specific_c5_number_data),)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False)

def specific_c1_profit_view(request):
    specific_c1_profit_data = specific_c1_profit.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(specific_c1_profit_data),)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False)

def specific_c2_profit_view(request):
    specific_c2_profit_data = specific_c2_profit.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(specific_c2_profit_data),)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False)

def specific_c3_profit_view(request):
    specific_c3_profit_data = specific_c3_profit.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(specific_c3_profit_data),)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False)

def specific_c4_profit_view(request):
    specific_c4_profit_data = specific_c4_profit.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(specific_c4_profit_data), indent=4)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False, json_dumps_params={'ensure_ascii': False})

def specific_c5_profit_view(request):
    specific_c5_profit_data = specific_c5_profit.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(specific_c5_profit_data),)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False)

def test_view(request):
    test1_data = test_test.objects.all().values()  # 获取数据库数据
    json_data = json.dumps(list(test1_data), indent=4)  # 将数据转换为 JSON 字符串
    return JsonResponse(json_data, safe=False, json_dumps_params={'ensure_ascii': False})

def json_view(request):
    with open('testdata.json', 'r') as file:
        json_data = json.load(file)
    
    response = JsonResponse(json_data, safe=False)
    response['Access-Control-Allow-Origin'] = '*'
    return response
