document.addEventListener("DOMContentLoaded", function() {
    console.log('Ok');

    var add_color_element = document.getElementById("tech_link");
    add_color_element.classList.add("active");
    var add_color_element1 = document.getElementById("tech");
    add_color_element1.classList.add("active");

    var toggle_active1 = document.getElementById('tech_link');
    var toggle_active2 = document.getElementById('good_link');
    var toggle_active3 = document.getElementById('perfect_link');

    var toggle_active11 = document.getElementById('tech');
    var toggle_active22 = document.getElementById('good');
    var toggle_active33 = document.getElementById('perfect');

    toggle_active1.addEventListener('click', function(){
        toggle_active3.classList.remove('active');
        toggle_active2.classList.remove('active');
        toggle_active22.classList.remove('active');
        toggle_active33.classList.remove('active');
        toggle_active11.classList.add('active');
        this.classList.add('active');

    });
    toggle_active2.addEventListener('click', function(){
        toggle_active1.classList.remove('active');
        toggle_active3.classList.remove('active');
        toggle_active11.classList.remove('active');
        toggle_active33.classList.remove('active');
        toggle_active22.classList.add('active');
        this.classList.add('active');
    });
    toggle_active3.addEventListener('click', function(){
        toggle_active1.classList.remove('active');
        toggle_active2.classList.remove('active');
        toggle_active11.classList.remove('active');
        toggle_active22.classList.remove('active');
        toggle_active33.classList.add('active');
        this.classList.add('active');
    });




    var fix_menu = document.getElementById("menu_fixed");

    if (screen.width > 1200) {
        window.onscroll = function() {myFunction()};

        var navbar = document.getElementById("menu_fixed");
        var sticky = navbar.offsetTop;
    
        function myFunction() {
        if (window.pageYOffset >= sticky) {
        navbar.classList.add("sticky")
        } else {
        navbar.classList.remove("sticky");
        }
        }

    }
    else {
        window.onscroll = function() {myFunction()};

        var navbar = document.getElementById("menu_fixed");
        var sticky = navbar.offsetTop;
        var div_parent = document.getElementsByClassName('three_left')
    
        function myFunction() {
        if (window.pageYOffset >= sticky) {
        navbar.classList.add("sticky_mobile")
        div_parent[0].classList.add('div_sticky_mobile')
        } else {
        navbar.classList.remove("sticky_mobile");
        div_parent[0].classList.remove('div_sticky_mobile')
        }
        }
    }



    $("a").on('click', function(event) {
        if (this.hash !== "") {
        event.preventDefault();
        var hash = this.hash;
        $('html, body').animate({
            scrollTop: $(hash).offset().top-100
        }, 500, function(){
            window.location.hash = hash;
        });
        } 
    });
});