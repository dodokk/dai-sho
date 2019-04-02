var num = 0;
$(".plas").click(function(){
    $(this).data("click", ++num);
    var click = $(this).data("click");
    if(click == 1){
         $('.player3').show();
    }
    if(click == 2){
         $('.player4').show();
    }
    if(click == 3){
         $('.player5').show();
    }
    return false;
});