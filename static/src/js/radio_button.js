$(function(){
    $("input[name='user_type']").change(function(){
        if (this.value == 1) {
        $("#compny_id").removeClass("d-none");
        $("#currncy_id").removeClass("d-none");

        }
        if (this.value == 8) {
             $("#compny_id").addClass("d-none");
            $("#currncy_id").addClass("d-none");
        }
    });
});