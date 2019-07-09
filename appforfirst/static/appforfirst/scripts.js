$(document).ready(function() {
	console.log("Doc ready");

	let click = $('.hambax').click(function () {
		$('#line1').toggleClass('rotateOn1');
		$('#line1').toggleClass('rotateOff');

		$('#line2').toggleClass('line2');

		$('#menu').toggleClass('rotateOn2');
		$('#menu').toggleClass('rotateOff');

		$('#line3').toggleClass('rotateOn3');
		$('#line3').toggleClass('rotateOff');

		$('.menu').toggleClass('menu_active');

		$('.body_overlay').toggleClass('body_overlay_active');
	})


	$('#body_overlay').click(function () {
		$('#body_overlay').removeClass('body_overlay_active');
		$('#line1').toggleClass('rotateOn1');
		$('#line1').toggleClass('rotateOff');

		$('#line2').toggleClass('line2');

		$('#menu').toggleClass('rotateOn2');
		$('#menu').toggleClass('rotateOff');

		$('#line3').toggleClass('rotateOn3');
		$('#line3').toggleClass('rotateOff');

		$('.menu').toggleClass('menu_active');

	})
})