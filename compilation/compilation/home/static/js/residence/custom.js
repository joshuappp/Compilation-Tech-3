//POP UP WHEN ERROR OCCURED
$(document).ready(function() {

    setTimeout(
    	function(){ 
    		$(".testDiv" ).remove()
    	}, 

    	7000);
 });
//WOW PLUGIN
$(function () {

    //animate on scroll
    new WOW().init();
});