//POP UP WHEN ERROR OCCURED
$(document).ready(function() {

    setTimeout(
        function(){ 
            $(".testDiv" ).remove()
        }, 

        1000);
 });
//WOW PLUGIN
$(function () {

    //animate on scroll
    new WOW().init();
});
// CAROUSEL AT HOME PAGE
$(function () {
    $("#block-items").owlCarousel({
        items: 3,
        autoplay: true,
        smartSpeed: 700,
        loop: true,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 1
            },
            480: {
                items: 2
            },
            768: {
                 items: 3
            }
        }
    });
});