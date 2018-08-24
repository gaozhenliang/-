from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^home/$',home.home,name='home'),
    #多个路由可以指向同一个路由，切记是可以这样用的
    url(r'^market/$',market.market,name='market'),
    url(r'^market/(\d+)/(\d+)/(\d+)/$', market.market, name='marketArg'),
    url(r'^collections/(\d+)/$',market.collection,name='collections'),


    url(r'^cart/$', cart.cart, name='cart'),
    url(r'^mine/$', mine.mine, name='mine'),
    url(r'^showcollections/$',mine.showCollections,name='showcollections'),
    url(r'^test/$',home.test,name='test'),

    url(r'^login/$',user.Login,name='login'),
    url(r'^logout/$',user.Logout,name='logout'),
    url(r'^register/$',user.register,name='register'),

    url(r'^docart/(\d+)/$',cart.doCart,name='docart'),
    url(r'^setallcheck/$',cart.setAllCheck,name='setallcheck'),
    url(r'^setorder/$',cart.setOrder,name='setorder'),
    url(r'^ordershow/$',order.orderShow,name='ordershow'),
    url(r'^doorder/$',order.doOrder,name='doorder'),

    url(r'^shippaddress/$',order.shipAddress,name='shippaddress'),
    url(r'^showaddress/$',order.showAddress,name='showaddress'),
    url(r'^changeaddress/(\d+)/$',order.changeAddress,name='changeaddress'),
    url(r'^changeaddr/$',order.changeAddr,name='changeaddr'),



]