$(document).ready(function () { 
    $("#update-quantity-form").click(function(event){
        event.preventDefault()
    })
    currentvalue = parseInt($("#update-quantity-input").val())
    $("#increase-bag-quantity").click(function() {
        $("#update-quantity-input").val(currentvalue + 1)
        id = parseInt($("#product-id").text())
        console.log(id)
        $.ajax({
            url: `/bag/update_bag/${id}/${$("#update-quantity-input").val()}/`,
            method: "POST"
        }).done(function() {
            window.location = "/bag/"
        })
        console.log($("#update-quantity-input").val())
    })
    
});