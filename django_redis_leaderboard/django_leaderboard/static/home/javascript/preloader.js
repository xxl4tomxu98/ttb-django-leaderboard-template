$(document).ready(function(){
    //code here

    $('.play-button').click(function(){

        var script = document.createElement('script');
        script.src = 'https://code.jquery.com/jquery-3.4.1.min.js';
        script.type = 'text/javascript';
        document.getElementsByTagName('head')[0].appendChild(script);

        var pk          = $(this).attr("data-id");
        var type        = $(this).attr("type");
        var src         = $(this).attr("src");
        var method      = $(this).attr("method");
        var token       = $("#token").attr("token");
        var button      = $(this);
        button.toggle();

        console.log("token")
        var image  = new Image();
        image.src  = $("#preloader_src").attr("src");
        console.log("img")

        image.setAttribute("style", "background: none; border: none;");
        image.setAttribute("border", "0");
        image.setAttribute("width", "14px");
        image.setAttribute("height", "14px");

        // Insert loading gif into the <td> element
        var td_string = "#td-run-" + type + "-" + pk;
        // 'td_string' example: #td-run-export-1
        $(td_string).append(image);

        // Get name of the report being run
        var td_name_string = "#td-name-" + type + "-" + pk;
        var td_name = $(td_name_string);

        $.ajax({
            type: method,
            url: src,
            headers: { "X-CSRFToken": token },
            data: {
                'pk': pk,
            },
            error: function (data) {
                image.remove();
                button.toggle();
                var d = new Date(); // Get current time
                var msg = $(td_name).text()+" | Error: "+data.status+" | Local Time: "+d.getHours()+":"+d.getMinutes()+":"+d.getSeconds();
                alert(msg);
            },
            success: function( data ) 
            {
                var modal = document.getElementById("myModal");
                var modal_body = document.getElementById("modal-body")
                image.remove();
                button.toggle();
                var d = new Date(); // Get current time
                var msg = $(td_name).text()+" "+data+" Local Time: "+d.getHours()+":"+d.getMinutes()+":"+d.getSeconds();
                modal.style.display = "block";
                $(modal_body).html(msg);
                
                var close = document.getElementById("close");
                close.onclick = function() {
                    modal.style.display = "none";
                }
                
                // When the user clicks anywhere outside of the modal, close it
                window.onclick = function(event) {
                    if (event.target == modal) {
                    modal.style.display = "none";
                    }
                }
                // alert(msg);
            }
        })
    });

});