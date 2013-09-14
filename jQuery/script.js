//this only affects the div we want it to affect - instead of all divs simultaniously.
$(document).ready(function() {
    $('div').mouseenter(function() {
        $(this).fadeTo('fast', 0);
});
});


$(document).read(function() {
    $('p').mouseenter(function(){
        $(this).fadeOut('fast');
    })
})
