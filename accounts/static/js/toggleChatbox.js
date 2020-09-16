function toggleChatStartup() {
  var chatbox = document.getElementById("chatstart-box");
  var toggleBtn = document.getElementById("toggle-chatbox-btn");
  var graphicProfile = document.getElementById("graphic-profile")
  if (chatbox.style.display == "block") {
    chatbox.style.display = "none";
    graphicProfile.style.display = "block";
    toggleBtn.innerHTML = "Apply for Assistance";
  } else {
    chatbox.style.display = "block";
    graphicProfile.style.display = "none"
    toggleBtn.innerHTML = "Close Application";
  }
}
