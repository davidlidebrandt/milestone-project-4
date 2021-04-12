$(document).ready(function () {
    $("#product-search").submit(function (e) {
        e.preventDefault();
        let search = $("#custom-search-group").val();
        window.location = `/products/?search=${search}`;
    })

    $(".close-message-container").click(function() {
        $(".message-container").hide();
    });
});

