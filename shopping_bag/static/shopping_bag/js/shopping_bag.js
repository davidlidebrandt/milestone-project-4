$(document).ready(function () { 
        let val = parseInt($("#product-quantity-input").val())
        console.log(val)
        if (val === 1) {
            $("#active-minus-button").hide();
        }
        if (val === 10) {
            console.log("here");
            $("#active-plus-button").hide();
            $("#disabled-minus-button").hide()
        }

        else {
            $("#disabled-minus-button").hide()
            $("#disabled-plus-button").hide()
        }
    
});
