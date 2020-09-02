function toggleChatStartup() {
  var chatbox = document.getElementById("chatstart-box");
  var toggleBtn = document.getElementById("toggle-chatbox-btn");
  if (chatbox.style.display == "block") {
    chatbox.style.display = "none";
    toggleBtn.innerHTML = "Apply for Assistance";
  } else {
    chatbox.style.display = "block";
    toggleBtn.innerHTML = "Close Application";
  }
}
