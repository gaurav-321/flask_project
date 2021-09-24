function sleepFor(sleepDuration) {
    var now = new Date().getTime();
    while (new Date().getTime() < now + sleepDuration) { /* Do nothing */
    }
}

function slider_animation() {
    let text1 = "Send Complaint ddEasily";
    for (let i = 0; i < text1.length; i++) {
        document.getElementById("animation_text").innerHTML = text1.slice(0, i);
        sleepFor(100);

    }
}

var text = ["Send Complaint Easily","And Quickly"];
var counter = 0;
var elem = $("#animation_text");
var bar = $("#text_typing");
var current_text = 0;
setInterval(change, 200);

function change() {
    if (counter >= text[current_text].length) {
        elem.html(text[current_text]);
        counter = 0;
        sleepFor(1000);
        if (current_text==0){
            current_text=1
        }
        else{
            current_text = 0
        }
    }
    counter++;
    bar.toggle();
    elem.html(text[current_text].slice(0, counter));





}