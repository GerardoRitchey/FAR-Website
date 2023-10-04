/*!
* Start Bootstrap - Agency v7.0.12 (https://startbootstrap.com/theme/agency)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-agency/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    //  Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            rootMargin: '0px 0px -40%',
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});



    function isScreenSizeLessThan780() {
        var windowWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
        return windowWidth < 780;
    }
    
    function disableMobileLightbox() {
        if (isScreenSizeLessThan780()) {
            // If we're below 780, bootstrap is going to render images that are mostly the right size.
            // Lightbox is irrelevant, so remove the data-lightbox attribute.
            $('[data-lightbox]').removeAttr('data-lightbox');
        }
    }
    
function preventLinkNavigation() {
    const linkElements = document.querySelectorAll("a.ig-lb-image");
    if (linkElements) {
        linkElements.forEach(linkElement => {
            linkElement.addEventListener("click", function (event) {
                if (isScreenSizeLessThan780()) {
                    // Prevent the default behavior (e.g., navigation)
                    event.preventDefault();
                }
            });
        });
    }
}


lightbox.option({
    'resizeDuration': 100,
    'fadeDuration':200,
    'wrapAround': true,
    'maxWidth': 700,
    showImageNumberLabel: false
    })


document.addEventListener("DOMContentLoaded", function(){
    disableMobileLightbox();
    preventLinkNavigation();
})

