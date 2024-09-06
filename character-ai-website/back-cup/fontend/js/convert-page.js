// chuyển trang
function ganyuPage() {
    window.location.href="ganyu.html";
}
function keqingPage() {
    window.location.href="keqing.html";
}
function eiPage() {
    window.location.href="ei.html";
}
function yaePage() {
    window.location.href="yae.html";
}
function hutaoPage() {
    window.location.href="hutao.html";
}

// click
document.getElementById("img-char-select-ganyu").onclick = function() {
    ganyuPage();
}
document.getElementById("img-char-select-keqing").onclick = function() {
    keqingPage();
}
document.getElementById("img-char-select-ei").onclick = function() {
    eiPage();
}
document.getElementById("img-char-select-yae").onclick = function() {
    yaePage();
}
document.getElementById("img-char-select-hutao").onclick = function() {
    hutaoPage();
}