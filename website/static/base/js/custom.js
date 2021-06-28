(function ($) {

    "use strict";

        // PRE LOADER
        $(window).load(function(){
          $('.preloader').delay(1500).fadeOut('slow'); // set duration in brackets    
        });


        // MENU
        $('.navbar-collapse a').on('click',function(){
          $(".navbar-collapse").collapse('hide');
        });
        // $('body').on('click',function(){
        //   console.log("TERCLICK");
        // });

        $(window).scroll(function() {
          // console.log($(".tm-title").offset().top);
          if ($(".navbar").offset().top > 50) {
            $(".navbar-fixed-top").addClass("top-nav-collapse");
              } else {
                $(".navbar-fixed-top").removeClass("top-nav-collapse");
              }
        });

        $('body').scroll(function() {
          // console.log($(".tm-title").offset().top);
          if ($(".tm-title").offset().top < 340) {
            $(".navbar-fixed-top").addClass("top-nav-collapse");
          } else{
            $(".navbar-fixed-top").removeClass("top-nav-collapse");
          }
        });
        


})(jQuery);