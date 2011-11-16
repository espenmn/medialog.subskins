$(document).ready(function(){
    $('.newsImageContainer').click(function() {
        $(".newsImageContainer").height(0);
        $("#kml-content-viewlet").height(300);
       });

     $('#kml-content-viewlet').click(function() {
        $(".newsImageContainer").height(300);
        $("#kml-content-viewlet").height(0);
       });
})(jQuery);