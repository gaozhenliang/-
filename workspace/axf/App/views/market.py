from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from App.models import *

# Create your views here.

def market(request,categoryid=104749,cid=0,sortid=0):

    leftSlider = FoodTypes.objects.all()
    #此判断实质就是对cid与sortid是否为0进行判断的代码
    if cid == '0':  #当子类别为0时，说明未选择类型
        productList = Goods.objects.filter(categoryid=categoryid)
    else:    ##当子类别为0时，说明选择了类型
        productList = Goods.objects.filter(categoryid=categoryid,childcid=cid)

    #当cid为0或非0时，都会对应这三种情况
    if sortid == '1':
        productList = productList.order_by("productnum")
    elif sortid == '2':
        productList = productList.order_by("price")
    elif sortid == '3':
        productList = productList.order_by("-price")

    group = leftSlider.get(typeid=categoryid)
    childList = []
    childnames = group.childtypenames
    # #全部分类:0#进口水果:103534#国产水果:103533
    arr1 = childnames.split('#')
    for str in arr1:
        arr2 = str.split(':')
        obj = {"childName":arr2[0],"childId":arr2[1]}
        childList.append(obj)


    # 此段代码为之前遗留的bug：该bug原因是因为当跳转到cart界面时，商品数量全为0,不能从库中把购物车商品数量展现到cart界面中
    user = request.user
    cartlist = []       #此列表为购物车的列表
    collectlist = []    #此列表为商品收藏的列表
    if user.is_authenticated:
        cartlist = user.cart_set.all()
        collectlist = request.user.goods.all()
    #此循环为给商品动态添加一个属性，此属性用以在商品栏中显示此商品被添加的数量
    for p in productList:
        for c in cartlist:
            if p.productid == c.goods.productid:
                p.num = c.num
                continue
        #此循环为商品动态添加一个属性，此属性为判断当用户登录时，显示当前商品是否被收藏
        for collect in collectlist:
            if p.productid == collect.productid:
                p.collectChoose = True
                continue


    return render(request,'market.html',{'leftSlider':leftSlider,'productList':productList,'childList':childList,'categoryid':categoryid,'cid':cid})



#用户收藏商品
def collection(req,productid):
    try:
        if req.user.is_favorite(productid):
            req.user.remove_favorite(productid)
        else:
            req.user.add_favorite(productid)
        return JsonResponse({'code':200})
    except Exception as e:
        print(e)
        return JsonResponse({'code':401})

