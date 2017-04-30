function message(status) {
    document.getElementById("spacer").innerHTML = status;
    $(".spacer").show().delay(2000).fadeOut();
}
var exit = function() {window.location.replace("/")};
var save = function() {
    try { var theme = document.getElementsByClassName("theme selected")[0].id;
          var c1 = theme.split('/')[0];
          var c2 = theme.split('/')[1];
        }
    catch(e) {
        c1 = "";
        c2 = ""
    }
    $.post({
        type: "POST",
        url: "/settings" ,
        data: {"username": $("#username").val(),
                 "password": $("#password").val(),
                 "email": $("#email").val(), 
                 "c1": c1, 
                 "c2": c2},
        success: function(response){
            message(JSON.parse(response)['status'])
        }
    })
};
$(document).ready(function() {
    $(document).on("click", "#exit", exit);
    $(document).on("click", "#save", save);
    $(document).keypress(function(e) {if (e.which === 13) {save()}});
    $(document).on("click", ".theme", function(event){
        var id = event.target.id;
        var colors = id.split('/');
        document.body.style.background = "linear-gradient(to right, "+colors[0]+", "+colors[1]+")";
        $(".theme").each(function(){this.className = "theme"});
        event.target.className = "theme selected";
    })
});