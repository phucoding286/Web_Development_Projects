// xử lý tin nhắn
function processingMessage(message) {
    if (message.toLowerCase().trim() == "hello") {
        return "Chào bạn, Tôi có thể giúp gì cho bạn hôm nay?";
    }
    else if (message.toLowerCase().trim() == "bạn tên gì") {
        return "Tôi tên là Character, Còn bạn?";
    }
    else {
        return "Tôi không hiểu câu này, Hãy nói lại!";
    }
};

// lắng nghe nhấn click trong nút gửi
document.getElementById("send-button").onclick = function () {
    let contentInTextInput = document.getElementById("text-input").value;
    console.log(`bạn đã gửi: ${contentInTextInput}`);
    // gán lại text input là chuổi rỗng sau khi nhấn gửi
    document.getElementById("text-input").value = "";
    // xử lý nếu text input là chuổi rỗng
    if (contentInTextInput != "") {
        document.getElementById("conversations").innerHTML += `<p class='user-content' id='user-content'>${contentInTextInput}</p>`
        document.getElementById("conversations").innerHTML += `<p class='bot-content' id='bot-content'></p>`

        let botContentNew = document.getElementsByClassName("bot-content");
        botContentNew = botContentNew[botContentNew.length - 1];

        let count = 0;
        let response = processingMessage(contentInTextInput);
        function botTyping() {
            botContentNew.textContent += response[count];
            count++;
            if (botContentNew.textContent.length < response.length) {
                setTimeout(botTyping, 10);
            }
            else { return 0; }
        }
        botTyping();
    }
    else {
        console.log("CẢNH BÁO: bạn đã nhập 1 khoảng trống, vui lòng nhập lại với chuổi")
    }
};