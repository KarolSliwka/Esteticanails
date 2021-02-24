/**
 * This function will add navigation shadow when user scroll more than 20px
 */
$(window).scroll(function () {
    var scroll = $(window).scrollTop();
    if (scroll > 20) {
        $('#main-nav').addClass('shadow')
    } else {
        $('#main-nav').removeClass('shadow')
    }
})

/**
 * This function will display enlarge image when clicked on Zoom + icon
 */
$(function () {
    $('.pop').on('click', function () {
        $('.imagepreview').attr('src', $(this).closest('.image-box').find('img').attr('src'));
        $('#imagemodal').modal('show');
    });
});

/**
 * This fucntion will close modal window on click 
 */
$('#close-button').click(function () {
    $('#imagemodal').modal('hide');
})

/**
 * This function will show previous image when clicked on modal
 */
$('.carousel-control-prev').on('click', function () {
    let thisImage = $(this).parent('div').find('img').attr('src');
    $('.gallery .image-box img').each(function () {
        if ($(this).attr("src") === thisImage) {
            let prevImage = $(this).parent().parent().prev().find('img').attr('src');
            $('.imagepreview').attr('src', prevImage);
            $('#imagemodal').modal('show');
        }
    });
});

/**
 * This function will show next image when clicked on modal
 */
$('.carousel-control-next').on('click', function () {
    let thisImage = $(this).parent('div').find('img').attr('src');
    $('.gallery .image-box img').each(function () {
        if ($(this).attr("src") === thisImage) {
            let nextImage = $(this).parent().parent().next().find('img').attr('src');
            $('.imagepreview').attr('src', nextImage);
            $('#imagemodal').modal('show');
        }
    });
});