/** function getElementByXpath(path) {
  return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
}
function irA(dir){
location.href = "http://127.0.0.1:8000/schedule/activity"+dir;
}

btn_duplicate =getElementByXpath('//*[@id="activity_form"]/div/div/input[2]');
btn_duplicate.addEventListener('click', function() {
    d_act= document.getElementById('id_description_Activity');
    console.log(d_act.value);
    date= document.getElementById('id_date');
    console.log(date.value);
    start= document.getElementById('id_start_time');
    console.log(start.value);
    alert("Clicked");
    irA('add')
    document.getElementById('id_description_Activity').innerHTML=d_act;
    document.getElementById('id_date').innerHTML=date;
    document.getElementById('id_start_time').innerHTML=start;
});

*/
$(function () {
   $('.submit-row').prepend('<input type="button" value=" Save and Duplicate" name="_duplicate" class="send_activity">');
    $('.send_activity').click(function (event) {
        var form = $('form:first    ').serialize();
        $('.errornote,.errorlist').remove();
        $.each($('.errors'), function(){$(this).removeClass('errors');});
        $.ajax({
            url: '/schedule/ws/schedule/',
            type:'post',
            dataType:'json',
            data: form,
            success: function (data) {
                console.log(Object.keys(data).length,'  ',data);
                if(Object.keys(data).length > 0){
                    $('form div:first').prepend('<p class="errornote">Please correct the errors below.</p>');
                    for( key in data){
                        console.log(key, '  ', key != undefined);
                        if(key != undefined){
                            var nodo = $('.field-'+key+':first');
                            nodo.addClass('errors');
                            nodo.prepend('<ul class="errorlist"><li>This field is required.</li></ul>');
                        }
                    }
                }
                else{
                    for(var nodo in OrderedSelectBox.cache){
                        if(nodo.includes("_to")){
                            var nodo_name = nodo.replace("_to", "_from");
                            var size = OrderedSelectBox.cache[nodo].length;
                            for(var i =0;i < size; i++){
                                OrderedSelectBox.cache[nodo_name].push(OrderedSelectBox.cache[nodo].pop());
                            }
                            OrderedSelectBox.redisplay(nodo_name);
                            OrderedSelectBox.redisplay(nodo);
                        }
                    }
                    alert("Activity Saved");
                }
            }
        })
        $('body,html').stop(true,true).animate({
                        scrollTop: $('#content').offset().top
                    },1000);
    })
});