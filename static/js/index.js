window.onload=function(){
  document.getElementById("stripeform").style.display = 'none';
  // on form submittal present a dialog box to confirm you are ready to checkout.
  document.querySelector('#my-checkout-button').addEventListener('click', function (event) {
    document.getElementById("stripeform").style.display = 'block';
	validate();
  }, false);

  function validate() {
    cart_items = document.querySelector("#cart-items").textContent;
    cart_total = document.querySelector("#cart-total").textContent;
    return confirm('Your items are ' + cart_items + ' Your total is ' + cart_total
    + ' Do you really want to submit the form?');
  }
}