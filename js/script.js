
// Create a JavaScript Date object using the release date string
var countDownDate = new Date(releaseDate);

// Update the count down every 1 second
var x = setInterval(function() {

  // Get todays date and time
  var now = new Date().getTime();

  // Find the distance between now an the count down date
  var distance = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the result in an element with id="demo"
  document.getElementById("demo").innerHTML = days + "天 " + hours + "小时 "
  + minutes + "分 " + seconds + "秒后";
  // If the count down is finished, write some text
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("demo").innerHTML = "现在已经"
    document.getElementById("demo_div").style.display = 'block';
    document.getElementById("demo_content").innerHTML = releaseContent;
  }
}, 1000);

// typewritter
let typeJsText = document.querySelector(".animatedText");
let stringIndex = 0;
let charIndex = 0;
let isTyping = true;

function typeJs() {
    if (stringIndex < textArray.length) {
        const currentString = textArray[stringIndex];

        if (isTyping) {
            if (charIndex < currentString.length) {
                typeJsText.innerHTML += currentString.charAt(charIndex);
                charIndex++;
            } else {
                isTyping = false;
            }
        } else {
            if (charIndex > 0) {
                typeJsText.innerHTML = currentString.substring(0, charIndex - 1);
                charIndex--;
            } else {
                isTyping = true;
                stringIndex++;

                if (stringIndex >= textArray.length) {
                    stringIndex = 0;
                }

                charIndex = 0;
                typeJsText.innerHTML = "";
            }
        }
    }
}

setInterval(typeJs, 1000);