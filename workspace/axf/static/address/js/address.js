// 默认地址只能选择一个
function changeaddr(productid) {
    aid =document.getElementById(productid+'cc');
    addrs = document.getElementsByClassName('addrs');
    $.get('/changeaddr/',{'productid':productid},function (data,status) {
        var html = '';
        // 当选中一个，再次选择另外一个的时候，应该将当前的置为True，其余的置为False，后台逻辑由试图搞定，前台展示由此ajax搞定
        if (data.bool){
            html = '√'
            for (var i=0;i<addrs.length;i++) {
                addr = addrs[i]
                if (addr.id == aid.id) {
                    aid.innerHTML = '√';
                }
                addr.innerHTML = '';
            }
        }
        console.log(aid);
        aid.innerHTML = html


    })
}


// 当删除默认自动地址时，优先选择最新添加数据
function delAddr(productid,state) {
    oldId = document.getElementById(productid);
    addrs = document.getElementsByClassName('addrs');
    $.get('/changeaddress/'+state+'/',{'productid':productid},function (data,status) {
        html = '';
        if (data.bool) {
            html = '√';
            aid =document.getElementById(data.newId+'cc');
            for (var i=0;i<addrs.length;i++) {
                addr = addrs[i];
                if (addr.id != aid.id) {
                    addr.innerHTML = '';

                }
                aid.innerHTML = '√';

            }

        }
        oldId.remove()


    })
}