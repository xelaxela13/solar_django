jQuery(document).ready(function () {
    // signup form
    $('#id_phone').mask('+380(99)9999999');
    const form_group = $('.form-group');
    form_group.each(function () {
        if($(this).children('small').length > 0){
            $(this).append('<span class="help-tooltip">?</span>');
        }

    });

    const help_tooltip = $('.help-tooltip');
    help_tooltip.mouseover(function (e) {
        $(this).prev('small').fadeIn(100);
    });
    help_tooltip.mouseout(function (e) {
        $(this).prev('small').fadeOut();
    });


});