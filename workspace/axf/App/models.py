from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Common(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    trackid = models.CharField(max_length=20)

    class Meta:
        abstract = True #抽象类  而不是表的模型

#轮播
class Wheel(Common):
    class Meta:
        db_table = 'axf_wheel'

# 每日必抢
class Nav(Common):
    class Meta:
        db_table = 'axf_nav'
#必买
class MustBuy(Common):
    class Meta:
        db_table = 'axf_mustbuy'

#首页下面的商品
class Shop(Common):
    class Meta:
        db_table = 'axf_shop'


class MainShow(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=200)
    categoryid = models.CharField(max_length=200)
    brandname = models.CharField(max_length=200)

    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=200)
    productid1 = models.CharField(max_length=200)
    longname1 = models.CharField(max_length=200)
    price1 = models.CharField(max_length=20)
    marketprice1 = models.CharField(max_length=200)

    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=200)
    productid2 = models.CharField(max_length=200)
    longname2 = models.CharField(max_length=200)
    price2 = models.CharField(max_length=20)
    marketprice2 = models.CharField(max_length=200)

    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=200)
    productid3 = models.CharField(max_length=200)
    longname3 = models.CharField(max_length=200)
    price3 = models.CharField(max_length=20)
    marketprice3 = models.CharField(max_length=200)

    class Meta:
        db_table='axf_mainshow'


class FoodTypes(models.Model):
    typeid = models.CharField(max_length=7)
    typename = models.CharField(max_length=10)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField()

    class Meta:
        db_table='axf_foodtypes'


class Goods(models.Model):
    # 商品id
    productid = models.CharField(max_length=10)
    # 商品图片
    productimg = models.CharField(max_length=100)
    # 商品名称
    productname = models.CharField(max_length=100)
    # 商品长名称
    productlongname = models.CharField(max_length=100)
    # 是否精选
    isxf = models.BooleanField(default=False)
    # 是否买一赠一
    pmdesc = models.BooleanField(default=False)
    # 规格
    specifics = models.CharField(max_length=20)
    # 价格
    price = models.CharField(max_length=10)
    # 超市价格
    marketprice = models.CharField(max_length=10)
    # 组id
    categoryid = models.CharField(max_length=10)
    # 子类组id
    childcid = models.CharField(max_length=10)
    # 子类组名称
    childcidname = models.CharField(max_length=20)
    # 详情页id
    dealerid = models.CharField(max_length=10)
    # 库存
    storenums = models.CharField(max_length=20)
    # 销量
    productnum = models.CharField(max_length=20)


    class Meta:
        db_table = 'axf_goods'


class User(AbstractUser):
    sex = models.BooleanField(default=True)
    age = models.IntegerField(default=20)
    icon = models.CharField(max_length=70)
    phone = models.CharField(max_length=11)
    isCheckBoxChoose = models.BooleanField(default=True)

    goods = models.ManyToManyField(Goods)  #会自动创建出第三张表，这张表为收藏表     之所以弃用此方法，是因为django模板中的if标签不能调用给方法中传入参数，因此只能手动创建第三张表

    class Meta:
        db_table = 'axf_user'

    '''
这些方法是自动创建第三张表时的写法

    #判断是否收藏此商品
    def is_favorite(self,pid):
        data = self.goods.all()
        for c in data:
            if c.productid == pid:
                return True
            else:
                return False


     #添加收藏
    def add_favorite(self,pid):
        self.goods.add(Goods.objects.get(productid=pid))


    #取消收藏
    def remove_favorite(self,pid):
        self.goods.remove(Goods.objects.get(productid=pid))
'''


    #判断是否收藏此商品
    def is_favorite(self,pid):
        data = self.goods.all()
        for c in data:
            if c.productid == pid:
                return True
        return False


     #添加收藏
    def add_favorite(self,pid):
        self.goods.add(Goods.objects.get(productid=pid))


    #取消收藏
    def remove_favorite(self,pid):
        self.goods.remove(Goods.objects.get(productid=pid))




class Cart(models.Model):
    goods = models.ForeignKey(Goods)
    user = models.ForeignKey(User)
    num = models.IntegerField(default=1)
    isChoose = models.BooleanField(default=True)


    class Meta:
        db_table = 'axf_cart'


class Address(models.Model):
    address = models.CharField(max_length=150)   #地址
    phone = models.CharField(max_length=11)   #手机号
    choose = models.BooleanField(default=False) #默认地址
    name = models.CharField(max_length=20)    #用户名
    user = models.ForeignKey(User)

    class Meta:
        db_table = 'axf_address'

#订单
class Order(models.Model):
    user = models.ForeignKey(User)
    address = models.ForeignKey(Address)
    money = models.DecimalField(max_digits=8,decimal_places=2)
    status = models.IntegerField(default=0) # 0 下订单未付款， 1已付款未发货  2已发货  3 完成订单
    message = models.CharField(max_length=100)  # 卖家留言   备注
    createTime = models.DateTimeField(auto_now_add=True)  #订单创建时间
    orderId = models.CharField(max_length=20)  #生成订单id号

    class Meta:
        db_table = 'axf_order'


#订单详情
class OrderDetail(models.Model):
    order = models.ForeignKey(Order)  #订单id
    goodsImg = models.CharField(max_length=200)
    goodsName = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    num = models.IntegerField(default=1)
    total = models.CharField(max_length=10)   #单个商品的总价格

    class Meta:
        db_table = 'axf_orderdetail'

#
# #商品收藏
# class Collection(models.Model):
#     user = models.ForeignKey(User)
#     product = models.ForeignKey(Goods)
#     isChoose = models.BooleanField(default=False)
#
#     class Meta:
#         db_table = 'axf_collection'