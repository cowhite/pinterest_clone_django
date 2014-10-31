$(function() {
    $("#avatar-block").hover(

        function() {
            $("#change-avatar").slideDown();
        },
        function() {
            $("#change-avatar").slideUp();
        }
    );
});