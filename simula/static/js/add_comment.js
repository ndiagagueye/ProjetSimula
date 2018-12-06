$(function() {
    $('#comment-form').on('submit', function(event){
        event.preventDefault();
        add_comment();
    });

    function changePostUpdate() {
        console.log("Change Post Update")
        $.ajax({
            url : "/forum/change_post_update",
            type : "POST",
            data : { id: $('#post_id').val() },
            success : function(json) {
                console.log(json);
            }
        });


    }

    /*setInterval(function () {
        $.ajax({
            url : "/forum/update_post",
            type : "POST",
            data : { id: $('#post_id').val() },
            success : function(json) {
                if(json.update == true) {
                    setTimeout(changePostUpdate,900);

                    $("#new-comment").append(
                    "<li><div class='comment-avatar'><img src='http://i9.photobucket.com/albums/a88/creaticode/avatar_1_zps8e1c80cd.jpg' alt=''></div><div class='comment-box'>"
                                    + "<div class='comment-head content-comm'><h6 class='comment-name by-author'><a href=''>"+json.comment_username+"</a></h6>"
                                      +"<span>hace 10 minutos</span><i class='fa fa-check' style='font-size: 2em; color: #00a65a'></i></div><div class='comment-content content-comm'>"
                                      +json.comment_body+
                                   " </div></div></li>")

                }
            }
        });  

    }, 1000); */



    // AJAX for posting
    function add_comment() {
        console.log("create post is working!")
        $.ajax({
            url : "/forum/add_comment",
            type : "POST",
            data : { body : $('#comment-text').val(), post_id: $('#post_id').val()},
            success : function(json) {
                $('#comment-text').val('');
            },
        });
    };


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});