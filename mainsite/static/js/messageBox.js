jQuery(document).ready(function ($) {
  "use strict";

  // CSRF TOKEN FOR AJAX
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  const csrftoken = getCookie("csrftoken");

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
  }
  $.ajaxSetup({
    beforeSend: function (xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    },
  });

  // Scroll to the input box
  if (document.getElementById("chatBox")) {
    $("html, body").animate(
      {
        scrollTop: $("#chatBox")[0].scrollHeight,
      },
      1000
    );
  }

  // Message Box
  $("form.messageBox").submit(function () {
    console.log(this);
    var action = $(this).attr("action");
    var id = $(this).attr("id");
    console.log(id);
    if (!action) {
      console.log("performed action");
      action = "/messageinput/";
    }
    var userInput = $("#message").val();
    console.log(userInput);
    $.ajax({
      type: "POST",
      url: action,
      data: {
        message: userInput,
        chat: id,
      },
      success: function (data) {
        window.location.href = "";
      },
    });
    return false;
  });
});
