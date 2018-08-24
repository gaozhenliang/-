from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from App.models import Cart,Goods
import math

# Create your views here.

@login_required(login_url='/login/')
def cart(req):
    cartObj = req.user.cart_set.all()
    # print('cartObj IS {}'.format(cartObj))
    cartChoose = req.user.cart_set.all().filter(isChoose=True)
    # print('cartChoose is {}'.format(cartChoose))
    money = 0
    if cartChoose.exists():
        for cart in cartChoose:
            money += eval(cart.goods.price) * cart.num
            # print('cart is {}'.format(cart.isChoose))
    # print(money)

    return render(req,'cart.html',{'cartslist':cartObj,'money':money})


#购物车数量的添加+1  和减少-1
def doCart(req,state):
    if not req.user.is_authenticated:
        return JsonResponse({'data':-1})
    newNum = 0
    user = req.user
    goods = Goods.objects.filter(productid=req.GET.get('productid')).first()
    cartObj = user.cart_set.filter(goods=goods)

    if int(state) == 0:
        #判断 这个商品是否在购物车中
        if cartObj.exists():
            num = cartObj.first().num
            newNum = num+1
            if newNum > int(goods.storenums):
                newNum = int(goods.storenums)
            cartObj.update(num = newNum)
        else:
            Cart(goods=goods,user=user).save()
            newNum = 1

    if int(state) == 1:
        if cartObj.exists():
            num = cartObj.first().num
            newNum = num -1
            if newNum>0:
                cartObj.update(num=newNum)
            else:
                cartObj.delete()



    if cartObj.exists():
        Bool = cartObj.first().isChoose
    else:
        Bool = False
    if int(state) == 2:
        chooseObj = cartObj.first()
        newNum = chooseObj.num
        Bool = True
        if chooseObj.isChoose:
            Bool = False
        cartObj.update(isChoose=Bool)



    money = 0
    cartChoose = req.user.cart_set.filter(isChoose=True)
    if cartChoose.exists():
        for cart in cartChoose:
            money += eval(cart.goods.price) * cart.num


    allCart = req.user.cart_set.all()
    allBool = True
    for onecart in allCart:
        if onecart.isChoose == False:
            allBool = False
    print('allBool is {}'.format(allBool))
    req.user.isCheckBoxChoose = allBool
    req.user.save()

    return JsonResponse({'num': newNum, 'money': math.floor(money), 'Bool': Bool,'allBool':allBool})



def setOrder(req):
    cartChoose = req.user.cart_set.filter(isChoose=True)
    bool = cartChoose.exists()
    return JsonResponse({'bool':bool})


#此方法为全反选
def setAllCheck(req):
    duigou = req.user.isCheckBoxChoose
    Bool = False
    if duigou:
        Bool = False
        req.user.cart_set.filter().update(isChoose=False)
        money = 0

    else:
        Bool = True
        req.user.cart_set.filter().update(isChoose=True)
        money = 0
        cartChoose = req.user.cart_set.filter(isChoose=Bool)
        if cartChoose.exists():
            for cart in cartChoose:
                money += eval(cart.goods.price) * cart.num


    req.user.isCheckBoxChoose=Bool
    req.user.save()

    return JsonResponse({'bool':Bool,'money':money})






