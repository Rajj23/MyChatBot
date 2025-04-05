function sendMessage() {
    var inputField = document.getElementById("userInput");
    var userMessage = inputField.value;
    if (userMessage.trim() === "") return;
    
   
    var messagesDiv = document.getElementById("messages");
    var userMsgDiv = document.createElement("div");
    userMsgDiv.className = "message user";
    userMsgDiv.textContent = "You: " + userMessage;
    messagesDiv.appendChild(userMsgDiv);
    
   
    inputField.value = "";
    

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMessage })
    })
    .then(response => response.json())
    .then(data => {
        
        var botMsgDiv = document.createElement("div");
        botMsgDiv.className = "message bot";
        botMsgDiv.textContent = "Bot: " + data.reply;
        messagesDiv.appendChild(botMsgDiv);
       
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
    })
    .catch(error => console.error("Error:", error));
}
