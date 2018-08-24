$(document).ready(function(){
    var alltypebtn = document.getElementById("alltypebtn")
    var showsortbtn = document.getElementById("showsortbtn")

    var typediv = document.getElementById("typediv")
    var sortdiv = document.getElementById("sortdiv")

    typediv.style.display = "none"
    sortdiv.style.display = "none"


    alltypebtn.addEventListener("click", function(){
        typediv.style.display = "block"
        sortdiv.style.display = "none"
    },false)
    showsortbtn.addEventListener("click", function(){
        typediv.style.display = "none"
        sortdiv.style.display = "block"
    },false)
    typediv.addEventListener("click", function(){
        typediv.style.display = "none"
    },false)
    sortdiv.addEventListener("click", function(){
        sortdiv.style.display = "none"
    },false)




    //修改购物车
    var addShoppings = document.getElementsByClassName("addShopping")
    var subShoppings = document.getElementsByClassName("subShopping")

    for (var i = 0; i < addShoppings.length; i++){
        addShopping = addShoppings[i];
        addShopping.addEventListener("click", function(){
            pid = this.getAttribute("ga");
            $.get("/docart/0/",{"productid":pid},function (data,status) {
                // console.log(data.data)
                document.getElementById(pid).innerHTML = data.num;
                if(data.data == -1) {
                    if (confirm("您还没有登录")) {
                        window.location.href = '/login/'
                    }
                }
            })

        })
    }


    for (var i = 0; i < subShoppings.length; i++){
        subShopping = subShoppings[i]
        subShopping.addEventListener("click", function(){
            pid = this.getAttribute("ga")
            $.get("/docart/1/",{"productid":pid},function (data,status) {
                // console.log(data.data)
                document.getElementById(pid).innerHTML = data.num;
                if(data.data == -1) {
                    if (confirm("您还没有登录")) {
                        window.location.href = '/login/'
                    }
                }
            })
        })
    }




});

function favorite(pid) {
    var pnode = $('#'+pid);
    $.get('/collections/'+pid+'/',function (data,status) {
        if (data.code == 200) {
            if (pnode.text().trim() == '收藏') {
                pnode.text('取消收藏')
            }else if (pnode.text().trim() == '取消收藏'){
                pnode.text('收藏')
            }
        }else{
            if (confirm('您还没有登录\n是否前去登录')) {
                window.location.href = '/login/'
            }
        }
    })

}