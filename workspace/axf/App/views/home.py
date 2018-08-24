from django.shortcuts import render,HttpResponse
from App.models import *
from django.db import connection

# Create your views here.

def home(req):
    wheel = Wheel.objects.all()
    nav = Nav.objects.all()
    mustbuy = MustBuy.objects.all()
    shop = Shop.objects.all()
    shop1 = shop[0]
    shop2 = shop[1:3]
    shop3 = shop[3:7]
    shop4 = shop[7:11]
    mainShow = MainShow.objects.all()
    return render(req,'home.html',{'wheel':wheel,'nav':nav,'mustbuy':mustbuy,'shop1':shop1,'shop2':shop2,'shop3':shop3,'shop4':shop4,'mainShow':mainShow})




def test(req):
    # data = req.user.goods.all()
    # print(data)
    # print(req.user.is_favorite(11951))
    # goods = Goods.objects.all()
    # for good in goods:
    #     good.

    '''

        #这是手动创建的表
    # u1 = User.objects.get(pk=2)
    # p1 = Goods.objects.first()
    # # p2 = Goods.objects.get(pk=2)
    # Collection(user=u1,product=p1).save()
    # req.user.collection_set(product=p1).save()
    #查询此用户收藏了哪些商品
    # data = req.user.collection_set.filter(user=req.user).all()
    # data = req.user.collection_set.all()
    # for c in data:
    #     print(c.product.productname)

    #查询此商品属于那个用户
    # p1 = Goods.objects.first()
    # data = req.user.collection_set.filter(product=p1).all()
    # print(data[0].user.username)
    '''
    #一个用户收藏多个商品
    # u1 = req.user
    # p1 = Goods.objects.get(pk=1)
    # p2 = Goods.objects.get(pk=2)
    # u1.goods.add(p1,p2)

    # #一个商品被多个用户收藏
    # u1 = req.user
    # u2 = User.objects.get(pk=2)
    # p1 = Goods.objects.get(pk=1)
    # p1.user_set.add(u1,u2)

    #哟农户取消一条商品收藏
    # u1 = req.user
    # p1 = Goods.objects.get(pk=1)
    # u1.goods.remove(p1)

    #查询当前用户的商品

    # data = req.user.goods.all()  #将用户所属的商品给查找出来
    # print(data)
    # for i in data:
    #     print(i.productname)
    # # print(connection.queries)
    #转换成原始sql为先将good表与第三章表进行联合查询，然后过滤条件为当前用户的id
    '''
    SELECT `axf_goods`.`id`, `axf_goods`.`productid`, `axf_goods`.`productimg`, `axf_goods`.`productname`, `axf_goods`.`productlongname`, `axf_goods`.`isxf`, `axf_goods`.`pmdesc`, `axf_goods`.`specifics`, `axf_goods`.`price`, `axf_goods`.`marketprice`, `axf_goods`.`categoryid`, `axf_goods`.`childcid`, `axf_goods`.`childcidname`, `axf_goods`.`dealerid`, `axf_goods`.`storenums`, `axf_goods`.`productnum` FROM `axf_goods` INNER JOIN `axf_user_goods` ON (`axf_goods`.`id` = `axf_user_goods`.`goods_id`) WHERE `axf_user_goods`.`user_id` = 1'
    '''
    return HttpResponse('ok')