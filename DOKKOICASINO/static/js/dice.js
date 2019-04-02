$(function(){
   var result1 = $('#dice1').html();
   var result2 = $('#dice2').html();
   var result3 = $('#dice3').html();
    
    $('#start').click(function(){  
    if (result1 == '1') {
      $('.anime1').html('<img src="/static/pic/dice1.gif" width="100%" height="100%" >');
      $('.con1').html('<img src="/static/pic/dice1.png"width="100%" height="100%" >');
　　}else if (result1 == '2') {
      $('.anime1').html('<img src="/static/pic/dice2.gif" width="100%" height="100%" >');
       $('.con1').html('<img src="/static/pic/dice2.png"width="100%" height="100%" >');
   }else if (result1 == '3') {
      $('.anime1').html('<img src="/static/pic/dice3.gif" width="100%" height="100%" >');
        $('.con1').html('<img src="/static/pic/dice3.png"width="100%" height="100%" >');
   }else if (result1 == '4') {
      $('.anime1').html('<img src="/static/pic/dice4.gif" width="100%" height="100%" >');
        $('.con1').html('<img src="/static/pic/dice4.png"width="100%" height="100%" >');
   }else if (result1 == '5') {
      $('.anime1').html('<img src="/static/pic/dice5.gif" width="100%" height="100%" >');
        $('.con1').html('<img src="/static/pic/dice5.png"width="100%" height="100%" >');
   }else{
       $('.anime1').html('<img src="/static/pic/dice6.gif" width="100%" height="100%" >');
        $('.con1').html('<img src="/static/pic/dice6.png"width="100%" height="100%"> ');
   }
    if (result2 == '1') {
      $('.anime2').html('<img src="/static/pic/dice1.gif" width="100%" height="100%" >');
        $('.con2').html('<img src="/static/pic/dice1.png"width="100%" height="100%" >');
　　}else if (result2 == '2') {
      $('.anime2').html('<img src="/static/pic/dice2.gif" width="100%" height="100%" >');
      $('.con2').html('<img src="/static/pic/dice2.png"width="100%" height="100%" >');
   }else if (result2 == '3') {
      $('.anime2').html('<img src="/static/pic/dice3.gif" width="100%" height="100%" >');
       $('.con2').html('<img src="/static/pic/dice3.png"width="100%" height="100%" >');
   }else if (result2 == '4') {
      $('.anime2').html('<img src="/static/pic/dice4.gif" width="100%" height="100%" >');
       $('.con2').html('<img src="/static/pic/dice4.png"width="100%" height="100%" >');
   }else if (result2 == '5') {
      $('.anime2').html('<img src="/static/pic/dice5.gif" width="100%" height="100%" >');
       $('.con2').html('<img src="/static/pic/dice5.png"width="100%" height="100%" >');
   }else{
       $('.anime2').html('<img src="/static/pic/dice6.gif" width="100%" height="100%" >');
       $('.con2').html('<img src="/static/pic/dice6.png"width="100%" height="100%" >');
   }
    if (result3 == '1') {
      $('.anime3').html('<img src="/static/pic/dice1.gif" width="100%" height="100%" >');
        $('.con3').html('<img src="/static/pic/dice1.png"width="100%" height="100%" >');
　　}else if (result3 == '2') {
      $('.anime3').html('<img src="/static/pic/dice2.gif" width="100%" height="100%" >');
      $('.con3').html('<img src="/static/pic/dice2.png"width="100%" height="100%" >');
   }else if (result3 == '3') {
      $('.anime3').html('<img src="/static/pic/dice3.gif" width="100%" height="100%" >');
       $('.con3').html('<img src="/static/pic/dice3.png"width="100%" height="100%" >');
   }else if (result3 == '4') {
      $('.anime3').html('<img src="/static/pic/dice4.gif" width="100%" height="100%" >');
       $('.con3').html('<img src="/static/pic/dice4.png"width="100%" height="100%" >');
   }else if (result3 == '5') {
      $('.anime3').html('<img src="/static/pic/dice5.gif" width="100%" height="100%" >');
       $('.con3').html('<img src="/static/pic/dice5.png"width="100%" height="100%" >');
   }else{
       $('.anime3').html('<img src="/static/pic/dice6.gif" width="100%" height="100%" >');
       $('.con3').html('<img src="/static/pic/dice6.png"width="100%" height="100%" >');
   }
	setTimeout(function(){
		$('#btn').show();
	},2300);

  });
    $('#btn').click(function(){  
        $("#dice").hide();
        $("#results").show();
    });
});