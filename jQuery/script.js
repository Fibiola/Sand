//this only affects the div we want it to affect - instead of all divs simultaniously.
$(document).ready(function() {
    $('.buttons').mouseenter(function() {
        $(this).toggleClass('cool');
    });
});


$(document).ready(function() {
    $('.wtf').click(function(){
        $(this).fadeOut('3');
    });
});

$(document).ready(function() {
    $('.cool').mouseenter(function(){
        $(this).fadeTo('fast', 100);
    });
});

$(document).ready(function() {
    $(".pull-me").click(function() {
    $(".panel").slideToggle("slow");
    });
});

// To -do list
$(document).ready(myClick);

function myAdd(){
    var toAdd = $('input[name=checkListItem]').val();
    $('.list').append('<div class="item">' + toAdd + '</div>');
}

function myClick(){
    $('#button').click(myAdd);
    $(document).on('click', '.item', myRemove);
}

function myRemove(){
    $(this).remove();
}
//aletrnative to do list function
$(document).ready(function() {
    $('button').click(function() {
        var toAdd = $("input[name=message]").val();
        $('#messages').append("<p>"+toAdd+"</p>");
    });
});

//super mario code - to move left right up and down.

$(document).ready(function() {
    $(document).keydown(function(key) {
        switch(parseInt(key.which,10)) {
            case 65:
                $('img').animate({left: "-=10px"}, 'fast');
                break;
            case 83:
                $('img').animate({top: "+=10px"}, 'fast');
                break;
            case 87:
                $('img').animate({top: "-=10px"}, 'fast');
                break;
            case 68:
                $('img').animate({left: "+=10px"}, 'fast');
                break;
            default:
                break;
        }
    });
});

// draggable car - click and move around

$(document).ready(function(){
    $("#car").draggable();
});