jQuery(document).ready(function () {
    const input_location = $('input[name="location"]');

    function dialog_box() {
        const url = $('form[data-url]').data('url');
        jQuery.get(url)
            .done(function (html) {
                $('body').append(html);
                const choice_location_manual_modal = $('#choiceLocationManualModal'),
                    choice_location_manual_form = $("#choiceLocationManualForm");
                choice_location_manual_modal.modal('show');
                $('input[name="inlineRadioOptions"]').on('change', function () {
                    choice_location_manual_form.submit();
                });
                choice_location_manual_form.submit(function (event) {
                    event.preventDefault();
                    $.ajax({
                        type: "POST",
                        url: $(this).attr('action'),
                        data: {
                            'location': $(this).find('input[name="inlineRadioOptions"]:checked').val()
                        },
                        success: function (data) {
                            input_location.val(data.city);
                            choice_location_manual_modal.modal('hide');
                        }
                    });
                    return false;
                });
            });
    }
    if (!input_location.val()) {
        dialog_box();
    }
});