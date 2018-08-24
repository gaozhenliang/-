from django.shortcuts import render,HttpResponse

# Create your views here.

def mine(req):
    return render(req,'mine.html')


#商品展示
def showCollections(req):
    if req.method == 'GET':
        data = req.user.goods.all()
        # for i in data:
        #     print(i.productname,i.price,i.productimg)
        return render(req,'goodscollection.html',{'data':data})