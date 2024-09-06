var contexts = "";
const maxLen = 10;

function processingMessage(message) {
    contexts += "userxxx: "+message+" "
    let lines = contexts.split("userxxx");
    if (lines.length > maxLen) {
        lines = lines.slice(-maxLen);
    }
    contexts = lines.join("userxxx");

    let firstOnclick = document.getElementById("send-button").onclick;
    document.getElementById("send-button").textContent = "processing...";
        document.getElementById("send-button").onclick = null;
    let model_name = document.getElementById("page-char-name").textContent;

    fetch(`/llm_response/?input=${message}&model=${model_name}&contexts=${contexts}`)
        .then(response => response.json())
        .then(data => {
            let botContentNew = document.getElementsByClassName("bot-content");
            botContentNew = botContentNew[botContentNew.length - 1];

            contexts += "charxxx: "+data.response+" "

            let count = 0;
            let response = data.response;
            function botTyping() {
                botContentNew.textContent += response[count];
                count++;
                if (botContentNew.textContent.length < response.length) {
                    setTimeout(botTyping, 10);
                }
                else {
                    document.getElementById("send-button").textContent = "Gửi";
                    document.getElementById("send-button").onclick = firstOnclick;
                }
            }
            botTyping();
        });
};


document.getElementById("send-button").onclick = function () {
    let contentInTextInput = document.getElementById("text-input").value;
    console.log(`bạn đã gửi: ${contentInTextInput}`);
    document.getElementById("text-input").value = "";

    
    if (contentInTextInput != "") {
        document.getElementById("conversations").innerHTML += `<p class='user-content' id='user-content'>${contentInTextInput}</p>`;
        document.getElementById("conversations").innerHTML += `<p class='bot-content' id='bot-content'></p>`;

        processingMessage(contentInTextInput);
    }
    else {
        console.log("CẢNH BÁO: bạn đã nhập 1 khoảng trống, vui lòng nhập lại với chuổi")
    }
};