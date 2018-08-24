from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect,reverse
from django.urls import reverse
from App.models import Address
import  math

from App.models import Address,Cart,Order,OrderDetail
import random

@login_required(login_url='/login/')
def orderShow(req):
    addressObj = req.user.address_set.filter(choose=True).first()
    cartChoose = req.user.cart_set.filter(isChoose=True)
    money = 0
    count = 0
    if cartChoose.exists():
        for cart in cartChoose:
            money += eval(cart.goods.price) * cart.num
            count += 1
    print('this is o ordershow')
    return render(req,'order.html',{'address':addressObj,'cartslist':cartChoose,'money':money,'count':count})

@login_required(login_url='/login/')
def doOrder(req):
    print('this is a doOrder')
    user = req.user
    address = user.address_set.filter(choose=True).first()
    message = req.POST.get('message')
    money = req.POST.get('money')
    try:
        order = Order(user=user,address=address,money=money,message=message,orderId=random.randrange(1111111,100000000))
        order.save()

        cart = req.user.cart_set.filter(isChoose=True)
        for c in cart:
            OrderDetail(order=order,goodsImg=c.goods.productimg,
                        goodsName=c.goods.productname,
                        price=c.goods.price,
                        num=c.num,
                        total=math.ceil(eval(c.goods.price) * c.num)).save()

        req.user.cart_set.filter(isChoose=True).delete()
    except Exception as e:
        print(e)
    return redirect(reverse('App:cart'))

#增加收货地址
def shipAddress(req):
    if req.method == 'GET':
        return render(req,'shippaddress.html')
    if req.method == 'POST':
        name = req.POST.get('name')
        phone = req.POST.get('phone')
        address = req.POST.get('address')
        choose = req.POST.get('choose')
        try:
            Bool = False
            if choose:
                Bool = True
                Address.objects.all().update(choose=False)
            Address(address=address,phone=phone,name=name,choose=Bool,user=req.user).save()
        except Exception as e:
            print('error is {}'.format(e))
        return redirect(reverse('App:showaddress'))

#展示收货地址
def showAddress(req):
    if req.method == 'GET':
        data = req.user.address_set.all().order_by('-id')
        return render(req,'showaddress.html',{'data':data})


#修改收货地址信息
def changeAddress(req,state):
    state = int(state)
    id = req.GET.get('productid')
    if req.method == 'GET':
        if state == 1:
            data = req.user.address_set.filter(pk=id).first()
            return render(req, 'changeaddress.html', {'data': data})
        if state == 2:
            data = req.user.address_set.filter(pk=id).first()
            if data.choose:
                Bool = True
                data.delete()
                try:
                    updateData = req.user.address_set.all().order_by('-id').first()
                    updateData.choose = Bool
                    updateData.save()
                    newId = updateData.id
                except:
                    newId = data.id

            else:
                Bool = False
                newId = data.id
                data.delete()
            # print('newId is {}'.format(newId))
            return JsonResponse({'bool':Bool,'newId':newId})
    if req.method == 'POST':
        if state == 1:
            id = int(req.POST.get('id'))
            req.user.address_set.filter(pk=id).update(name=req.POST.get('name'),phone=req.POST.get('phone'),address=req.POST.get('address'))
            return redirect(reverse('App:showaddress'))


#修改默认地址
def  changeAddr(req):
    id = int(req.GET.get('productid'))
    data = req.user.address_set.filter(pk=id).first()
    if  data.choose:
        Bool = False
    else:
        Bool = True
        req.user.address_set.all().update(choose=False)
    data.choose=Bool
    data.save()
    return JsonResponse({'bool': Bool})