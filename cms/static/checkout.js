$(document).ready(function () {
    $("#place-order-button").click(function (e) {
        e.preventDefault();
        $.LoadingOverlay("show");
        setTimeout(function () {
            $("#checkout-form").submit();
        }, 3000);
    });
});
