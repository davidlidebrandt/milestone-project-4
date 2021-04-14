let stripeInstance = Stripe("pk_test_51IfQReEg6TzYJMSJUwwscxw3gHeV7IasaIgvyOIGZ2RLgbm5EwmbJe6x6EmlRzqACprHd6mXYVODUl5Mw7HJJ6nw00fKMoxgT4")

$(document).ready(function () { 
    $("#checkout-button").click(function() {
        $.ajax({
            method: "POST",
            headers: {
                'X-CSRFToken': csrf
            },
            url: "/payment/create_checkout/"
        }) .then(function (response) {
            return response.json();
          })
          .then(function (session) {
            return stripeInstance.redirectToCheckout({ sessionId: session.id });
          })
          .then(function (result) {
            if (result.error) {
              alert(result.error.message);
            }
          })
          .catch(function (error) {
            console.error("Error:", error);
          });
    })
});