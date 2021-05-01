// The Stripe docs and another tutorial was uses as the base for this code.
// https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=checkout#redirect-customers
// https://testdriven.io/blog/django-stripe-tutorial/

const stripe = Stripe('pk_test_51IfQReEg6TzYJMSJUwwscxw3gHeV7IasaIgvyOIGZ2RLgbm5EwmbJe6x6EmlRzqACprHd6mXYVODUl5Mw7HJJ6nw00fKMoxgT4');
$(document).ready(function () {
  $("#redirect-checkout").submit(function(e) {
    e.preventDefault();
    
    const request = new Request("/payment/create_checkout/",  {headers: {'X-CSRFToken': CSRF }})
    fetch(request, {
      method: 'POST',
      mode: 'same-origin'
  })
      .then((result) => {
        return result.json();
      })
      .then((data) => {
        
        return stripe.redirectToCheckout({
          sessionId: data.sessionId,
        });
      })
      .then((res) => {
        console.log(res);
      });
  })

});
