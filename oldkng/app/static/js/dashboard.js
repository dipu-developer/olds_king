
console.log('i am load')
$('#cat1').change(function(){
    var scat=$('#cat1').val();
    let csf = $('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        type:"POST",
        url: "{% url 'load_mrp' %}",
        data: {
            mrp:scat,
            csrfmiddlewaretoken: csf
        },
        success: function(data){
            x= data.mrp;
            var p=x[0].mrp;
            $('#mrp1').val(p);           
        }    
    });
});

$(document).ready(function() {
    clockUpdate();
    setInterval(clockUpdate, 1000);
  })
  
  function clockUpdate() {
    var date = new Date();
    $('.digital-clock').css({'color': '#fff', 'text-shadow': '0 0 6px #ff0'});
    function addZero(x) {
      if (x < 10) {
        return x = '0' + x;
      } else {
        return x;
      }
    }
  
    function twelveHour(x) {
      if (x > 12) {
        return x = x - 12;
      } else if (x == 0) {
        return x = 12;
      } else {
        return x;
      }
    }
  
    var h = addZero(twelveHour(date.getHours()));
    var m = addZero(date.getMinutes());
    var s = addZero(date.getSeconds());
  
    $('.digital-clock').text(h + ':' + m + ':' + s)
  }