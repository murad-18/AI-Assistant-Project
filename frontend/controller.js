// jQuery document ready function
$(document).ready(function () {
    // Expose DisplayMessage function for displaying messages
    Element.expose(DisplayMessage);
  
    function DisplayMessage(message) {
      // Set the message text in the Siri message element
      $(".siri-message li:first").text(message);
      // Start the textillate animation
      $('.siri-message').textillate('start');
    }
  
    // Expose ShowHood function to show the assistant hood
    Element.expose(ShowHood);
  
    function ShowHood() {
      // Show the Oval and hide Siriwave when the hood is displayed
      $("#Oval").attr("hidden", false);
      $("#Siriwave").attr("hidden", true);
    }
  });
  