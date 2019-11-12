$(document).ready(function(){
	console.log('DOM załadowany - można się bawić');
});

$(document).ready(function() {
var NavY = $('header').offset().top;

var stickyNav = function(){
var ScrollY = $(window).scrollTop();



if (ScrollY > 530) {
  $('header').addClass('sticky');
} else {
  $('header').removeClass('sticky');
}
};

stickyNav();

$(window).scroll(function() {
  stickyNav();
});
});


/*change border color*/

$("#about-me-color").hover(function() {
  $("#home").toggleClass("slogan-about-me");
  $(".home-open").toggleClass("slogan-about-me");
  $(".home-close").toggleClass("slogan-about-me");
  $("#borderFixed").toggleClass("bfAbout");
});

$("#cooperation-color").hover(function() {
  $("#home").toggleClass("slogan-cooperation");
  $(".home-open").toggleClass("slogan-cooperation");
  $(".home-close").toggleClass("slogan-cooperation");
  $("#borderFixed").toggleClass("bfCoop");
});

$("#my-jobs-color").hover(function() {
  $("#home").toggleClass("slogan-my-jobs");
  $(".home-open").toggleClass("slogan-my-jobs");
  $(".home-close").toggleClass("slogan-my-jobs");
  $("#borderFixed").toggleClass("bfJobs");
});

$("#contact-color").hover(function() {
  $("#home").toggleClass("slogan-contact");
  $(".home-open").toggleClass("slogan-contact");
  $(".home-close").toggleClass("slogan-contact");
  $("#borderFixed").toggleClass("bfCont");
});

/*mustage*/

jQuery(document).ready(setTimeout(function(){
  jQuery(".mustage").addClass("mustage-on");
  }, 2000));

/*smooth moving by id*/


function isIE () {
    var myNav = navigator.userAgent.toLowerCase();
    return (myNav.indexOf('msie') != -1) ? parseInt(myNav.split('msie')[1]) : false;
}

window.isIEOld = isIE() && isIE() < 9; window.isiPad = navigator.userAgent.match(/iPad/i);




/*smoth scrolling*/

jQuery(document).ready(function(){
  // Add smooth scrolling to all links
  jQuery(".internalLink").on('click', function(event) {

    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      jQuery('html, body').animate({
        scrollTop: jQuery(hash).offset().top
      }, 1200, function(){
   
        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });
});








