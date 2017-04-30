function message(status) {
    document.getElementById("spacer").innerHTML = status;
    $(".spacer").show().delay(2000).fadeOut();
    $(".loginbox").effect("shake", {direction: "right", times: 2, distance: 8}, 250);
}
var login = function() {
    $.post({
        type: "POST",
        url: "/" ,
        data: {"username": $("#username").val(), 
               "password": $("#password").val()},
        success: function(response){
            var status = JSON.parse(response)['status'];
            if (status === 'Login successful') {location.reload()}
            else {message(status)}}
    })
}
$(document).ready(function() {
    $(document).on("click", "#login", login);
    $(document).keypress(function(e) {if(e.which === 13) {login()}});
    $(document).on("click", "#register", function() {
        $.post({
            type: "POST",
            url: "/register" ,
            data: {"username": $("#username").val(), 
                    "password": $("#password").val(), 
                    "email"  : $("#email").val()},
            success: function(response) {
                var status = JSON.parse(response)['status'];
                if (status === 'Register successful') {location.reload()}
                else {message(status)}
            }
        })
    })
});