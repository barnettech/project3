// on form submittal present a dialog box to confirm you are ready to checkout.
console.log('here');
function validate(form) {
    cart_items = document.querySelector("#cart-items").textContent;
    cart_total = document.querySelector("#cart-total").textContent;
    return confirm('Your items are ' + cart_items + ', your total is ' + cart_total
    + ' Do you really want to submit the form?');
}