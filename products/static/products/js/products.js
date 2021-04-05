$(document).ready(function () {
    $("#increase-quantity").click(function () {
        currentValue = parseInt($("#quantity-input").val())
        if (currentValue > 0 && currentValue < 10) {
            $("#quantity-input").val(currentValue + 1)
        }
    });

    $("#decrease-quantity").click(function () {
        currentValue = parseInt($("#quantity-input").val())
        if (currentValue > 1) {
            $("#quantity-input").val(currentValue - 1)
        }
    });
})
