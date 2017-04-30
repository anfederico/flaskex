$(document).ready(function() {
    var hoverIn = function(e) {
        var id = e.target.id;
        var text = document.getElementById(id+"-text");
        text.style.visibility = "visible";
    };
    var hoverOut = function(e) {
        var id = e.target.id;
        var text = document.getElementById(id+"-text");
        text.style.visibility = "hidden";
    };
    $(".navcon").hover(hoverIn, hoverOut)
});