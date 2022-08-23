

/********************* Menu Js **********************/

function windowScroll() {
  const navbar = document.getElementById("navbar");
  if (
    document.body.scrollTop >= 50 ||
    document.documentElement.scrollTop >= 50
  ) {
    navbar.classList.add("nav-sticky");
  } else {
    navbar.classList.remove("nav-sticky");
  }
}

window.addEventListener('scroll', (ev) => {
  ev.preventDefault();
  windowScroll();
})





//
/********************* light-dark js ************************/
//

const btn = document.getElementById("mode");
btn.addEventListener("click", (e) => {
  let theme = localStorage.getItem("theme");
  if (theme == "light" || theme == "") {
    document.body.setAttribute("data-layout-mode", "dark");
    localStorage.setItem("theme", "dark");
  } else {
    document.body.removeAttribute("data-layout-mode");
    localStorage.setItem("theme", "light");
  }
});



// tiny slide **** home

try {
  var slider = tns({
    container: '.home-slider',
    loop: true,
    autoplay: false,
    mouseDrag: true,
    controls: true,
    navPosition: "bottom",
    nav: false,
    autoplayTimeout: 5000,
    speed: 900,
    center: false,
    animateIn: "fadeIn",
    animateOut: "fadeOut",
    controlsText: ['&#8592;', '&#8594;'],
    autoplayButtonOutput: false,
    gutter: 30,
    responsive: {

      992: {
        gutter: 30,
        items: 1
      },

    }
  });

} catch (error) {

}



// text-animation

try {
  var TxtType = function (el, toRotate, period) {
    this.toRotate = toRotate;
    this.el = el;
    this.loopNum = 0;
    this.period = parseInt(period, 10) || 2000;
    this.txt = '';
    this.tick();
    this.isDeleting = false;
  };

  TxtType.prototype.tick = function () {
    var i = this.loopNum % this.toRotate.length;
    var fullTxt = this.toRotate[i];
    if (this.isDeleting) {
      this.txt = fullTxt.substring(0, this.txt.length - 1);
    } else {
      this.txt = fullTxt.substring(0, this.txt.length + 1);
    }
    this.el.innerHTML = '<span class="wrap">' + this.txt + '</span>';
    var that = this;
    var delta = 200 - Math.random() * 100;
    if (this.isDeleting) { delta /= 2; }
    if (!this.isDeleting && this.txt === fullTxt) {
      delta = this.period;
      this.isDeleting = true;
    } else if (this.isDeleting && this.txt === '') {
      this.isDeleting = false;
      this.loopNum++;
      delta = 500;
    }
    setTimeout(function () {
      that.tick();
    }, delta);
  };

  function typewrite() {
    if (toRotate === 'undefined') {
      changeText()
    }
    else
      var elements = document.getElementsByClassName('typewrite');
    for (var i = 0; i < elements.length; i++) {
      var toRotate = elements[i].getAttribute('data-type');
      var period = elements[i].getAttribute('data-period');
      if (toRotate) {
        new TxtType(elements[i], JSON.parse(toRotate), period);
      }
    }
    // INJECT CSS
    var css = document.createElement("style");
    css.type = "text/css";
    css.innerHTML = ".typewrite > .wrap { border-right: 0.08em solid #ffffff}";
    document.body.appendChild(css);
  };
  typewrite();

} catch (error) {

}



// swiper slider

try {
  new Swiper('.swiper-container', {
    loop: true,
    slidesPerView: 3,
    paginationClickable: true,
    spaceBetween: 20,
    pagination: '.swiper-pagination',
    slidesPerView: 'auto',
    paginationClickable: true,
    spaceBetween: 0,
    centeredSlides: true,
    speed: 1500,
    breakpoints: {
      1920: {
        slidesPerView: 3,
        spaceBetween: 30
      },
      1028: {
        slidesPerView: 2,
        spaceBetween: 30
      },
      768: {
        slidesPerView: 1,
        spaceBetween: 10
      }
    }
  });

} catch (error) {

}



// tiny slide **** home

try {
  var slider = tns({
    container: '.work-slider',
    loop: true,
    autoplay: true,
    mouseDrag: true,
    controls: true,
    navPosition: "bottom",
    nav: false,
    autoplayTimeout: 5000,
    speed: 900,
    center: false,
    animateIn: "fadeIn",
    animateOut: "fadeOut",
    controlsText: ['&#8592;', '&#8594;'],
    autoplayButtonOutput: false,
    gutter: 30,
    responsive: {

      992: {
        gutter: 30,
        items: 3
      },

    }
  });

} catch (error) {

}


try {
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
  })
} catch (error) {

}


// 
// home-5


try {
  var slider = tns({
    container: '.home5-slider',
    loop: true,
    autoplay: true,
    mouseDrag: true,
    controls: false,
    navPosition: "bottom",
    nav: false,
    autoplayTimeout: 5000,
    speed: 900,
    center: false,
    animateIn: "fadeIn",
    animateOut: "fadeOut",
    controlsText: ['&#8592;', '&#8594;'],
    autoplayButtonOutput: false,
    items:2,
    gutter: 30,
    responsive: {

      992: {
        gutter: 30,
        items: 3
      },

      576:{
        gutter: 30,
        items: 2
      }

    }
  });

} catch (error) {

}




// 
// home-5


try {
  var slider = tns({
    container: '.home6-slider',
    loop: true,
    autoplay: true,
    mouseDrag: true,
    controls: false,
    navPosition: "bottom",
    nav: false,
    autoplayTimeout: 5000,
    speed: 900,
    center: false,
    animateIn: "fadeIn",
    animateOut: "fadeOut",
    controlsText: ['&#8592;', '&#8594;'],
    autoplayButtonOutput: false,
    items:2,
    gutter: 30,
    responsive: {

      992: {
        gutter: 30,
        items: 2.5
      },

      576:{
        gutter: 30,
        items: 2
      }

    }
  });

} catch (error) {

}




// Contact Form
function validateForm() {
  var name = document.forms["myForm"]["name"].value;
  var email = document.forms["myForm"]["email"].value;
  var subject = document.forms["myForm"]["subject"].value;
  var comments = document.forms["myForm"]["comments"].value;
  document.getElementById("error-msg").style.opacity = 0;
  document.getElementById('error-msg').innerHTML = "";
  if (name == "" || name == null) {
      document.getElementById('error-msg').innerHTML = "<div class='alert alert-warning'>*Please enter a Name*</div>";
      fadeIn();
      return false;
  }
  if (email == "" || email == null) {
      document.getElementById('error-msg').innerHTML = "<div class='alert alert-warning'>*Please enter a Email*</div>";
      fadeIn();
      return false;
  }
  if (subject == "" || subject == null) {
      document.getElementById('error-msg').innerHTML = "<div class='alert alert-warning'>*Please enter a Subject*</div>";
      fadeIn();
      return false;
  }
  if (comments == "" || comments == null) {
      document.getElementById('error-msg').innerHTML = "<div class='alert alert-warning'>*Please enter a Comments*</div>";
      fadeIn();
      return false;
  }

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
          document.getElementById("simple-msg").innerHTML = this.responseText;
          document.forms["myForm"]["name"].value = "";
          document.forms["myForm"]["email"].value = "";
          document.forms["myForm"]["subject"].value = "";
          document.forms["myForm"]["comments"].value = "";
      }
  };
  xhttp.open("POST", "php/contact.php", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("name=" + name + "&email=" + email + "&subject=" + subject + "&comments=" + comments);
  return false;
}

function fadeIn() {
  var fade = document.getElementById("error-msg");
  var opacity = 0;
  var intervalID = setInterval(function () {
      if (opacity < 1) {
          opacity = opacity + 0.5
          fade.style.opacity = opacity;
      } else {
          clearInterval(intervalID);
      }
  }, 200);
}

