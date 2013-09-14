//this only affects the div we want it to affect - instead of all divs simultaniously.
$(document).ready(function() {
    $('.buttons').mouseenter(function() {
        $(this).fadeTo('fast', 0);
    });
});


$(document).ready(function() {
    $('.wtf').click(function(){
        $(this).fadeOut('3');
    });
});

$(document).ready(function(){
    $(".pull-me").click(function() {
    $(".panel").slideToggle("slow");
    });
});
