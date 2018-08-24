function doCartNum(productid,state) {
    $.get('/docart/'+state+'/',{'productid':productid},function (data,status) {
        if (data.num == 0){
            window.location.href='/cart/'
        }
        //此判断为单选
        var html = '';
        if(data.Bool){
            html =  '√';
        }

        //此判断为全反选
        var allHtml = '';
        if(data.allBool){
            allHtml = '√';
        }

        allcheck = document.getElementById('allcheck').innerHTML = allHtml;
        // 修改按钮的对勾
        document.getElementById(productid+'x').innerHTML = html;
        // 修改商品的数量
        document.getElementById(productid).innerHTML = data.num;
        document.getElementById('totalmoney').innerHTML = '总价 ： '+ data.money
    })
}

function orderShow() {
    if (confirm('是否下订单')){
         $.get('/setorder/',function (data,status) {
            if (data.bool) {
                window.location.href='/ordershow/'
            } else{
                alert('您还没有选择任何商品')
            }
         });

    }

}

//此方法为全反选
function allCheck() {
    allcheck = document.getElementById('allcheck')
    childcheck = document.getElementsByClassName('duigou')
    $.get('/setallcheck/',function (data,status) {
        alert(data.bool)
        html = ''
        if (data.bool) {
            html='√'
        }
        for(var i=0;i<childcheck.length;i++) {
            onechild = childcheck[i]
            onechild.innerHTML = html
        }
        allcheck.innerHTML=html
        document.getElementById('totalmoney').innerHTML = '总价 ： '+ data.money
    })

}




