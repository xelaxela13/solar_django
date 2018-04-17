jQuery(document).ready(function () {
    // signup form
    const phone_field = $('#id_phone');
    if (phone_field.length > 0) {
        phone_field.mask('+380(99)9999999');
    }

    const form_group = $('.form-group');
    form_group.each(function () {
        if ($(this).children('small').length > 0) {
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

    // messages notification
    const messages = $('.alert'),
        messages_height = messages.outerHeight();
    var pos = messages.position().top;

    $.each(messages, function (index, element) {
        if (index > 0) {
            pos += messages_height + 10;
            $(element).css('top', pos);
        }
    });
    window.setTimeout(function () {
        messages.fadeTo(500, 0).slideUp(500, function () {
            $(this).remove();
        });
    }, 4000);

});