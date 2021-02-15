/**
 * This function will add navigation shadow when user scroll more than 20px
 */
$(window).scroll(function () {
    var scroll = $(window).scrollTop();
    if (scroll > 20) {
        $('#main-nav').addClass('shadow-sm')
    } else {
        $('#main-nav').removeClass('shadow-sm')
    }
})