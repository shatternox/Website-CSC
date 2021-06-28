(function ($) {

  "use strict";

  // Owl Carousel
  var owl = $("#owl-team")
    owl.owlCarousel({
      autoPlay: 6000,
      items : 4,
      itemsDesktop : [1199,3],
      itemsDesktopSmall : [979,3],
      itemsTablet: [768,2],
      itemsTabletSmall: false,
      itemsMobile : [479,1],
      Speedfast: 200,
  });

})(jQuery);