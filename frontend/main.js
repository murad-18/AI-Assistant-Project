$(document).ready(function () {
    // Applying textillate animation to elements with class 'text'
    $('.text').textillate({
        loop: true, // Enable looping of the animation
        sync: true, // Synchronize multiple instances of textillate
        in: {
            effect: "bounceIn", // Set the entrance effect to 'bounceIn'
        },
        out: {
            effect: "bounceOut", // Set the exit effect to 'bounceOut'
        },
    });
});
var siriwave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
    style: "ios9",
    amplitude: "1",
    speed: "0.30",
    autostart: true
  });
// Mic button click event
$("#MicBtn").click(function () {
    //Element.playAssistantSound(); // Call playAssistantSound function
    $("#Oval").attr("hidden", true); // Hide Oval section
    $("#SiriWave").attr("hidden", false); // Show SiriWave section
    eel.takecommand(); // Call takecommand function from eel
  });
    