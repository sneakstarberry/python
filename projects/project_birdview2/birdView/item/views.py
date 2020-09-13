from django.shortcuts import render
from .models import Item, ItemCategory
import requests
import json
from django.http import HttpResponse
from .pagination import ItemPagination

from .serializers import ItemSerializer
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django_filters import rest_framework as filters
import django_filters
# Create your views here.
def item_post(req):
    # sleep(2)
    data_url = "https://grepp-programmers-challenges.s3.ap-northeast-2.amazonaws.com/2020-birdview/item-data.json"
    post_res = requests.get(data_url)
    post_res = post_res.content.decode('utf-8')
    datas = json.loads(post_res)
    insert_cnt = 0

    for data in datas:
        item = Item.objects.filter(id=data["id"])
        new_itemFeature = Item()
        new_itemFeature.id = data["id"]
        new_itemFeature.imageId = data["imageId"]
        new_itemFeature.name = data["name"]
        new_itemFeature.price = data["price"]
        new_itemFeature.gender = data["gender"]
        new_itemFeature.category = data["category"]
        new_itemFeature.ingredients.set([ItemCategory(name=data["ingredients"])])
        new_itemFeature.monthlySales = data["monthlySales"]
        new_itemFeature.save()
    if insert_cnt > 0:
        message = str(insert_cnt)+'개의 데이터를 정상적으로 추가하였습니다.'
    else:
        message = "추가된 데이터가 없습니다."
    result_res = { 'message': message}
    result_res = json.dumps(result_res)
    return HttpResponse(result_res)



def itemCategory_post(req):
    data_url = "https://grepp-programmers-challenges.s3.ap-northeast-2.amazonaws.com/2020-birdview/ingredient-data.json"
    post_res = requests.get(data_url)
    post_res = post_res.content.decode('utf-8')
    datas = json.loads(post_res)
    insert_cnt = 0

    for data in datas:
        # item = ItemCategory.objects.filter(day=data["name"])
        new_itemcategory = ItemCategory()
        new_itemcategory.name = data["name"]
        new_itemcategory.oily = data["oily"]
        new_itemcategory.sensitive = data["sensitive"]
        new_itemcategory.dry = data["dry"]
        new_itemcategory.save()
    if insert_cnt > 0:
        message = str(insert_cnt)+'개의 데이터를 정상적으로 추가하였습니다.'
    else:
        message = "추가된 데이터가 없습니다."
    result_res = { 'message': message}
    result_res = json.dumps(result_res)
    return HttpResponse(result_res)


class MyfilterSet(FilterSet):
    include_ing = django_filters.CharFilter(field_name='ingredients', lookup_expr='icontains' )
    exclude_ing = django_filters.CharFilter(field_name='ingredients', lookup_expr='icontains', exclude=True)

    class Meta:
        model = Item
        fields = ['category', 'include_ing', 'exclude_ing']

class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = ItemPagination

    filter_backends = (DjangoFilterBackend,)
    filterset_class = MyfilterSet