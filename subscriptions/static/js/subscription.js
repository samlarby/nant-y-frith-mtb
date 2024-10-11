console.log("Sanity check!");

fetch("/stripe_config/")
.then((result) => {return result.json(); })
.then((data) => {
    // Initialize Stripe.js
    var stripe = Stripe('data.publicKey') 

    let submitBtn = document.querySelector("#submitBtn");
    if (submitBtn !== null) {
        submitBtn.addEventListener("click", () => {
        // get checkout session id
        fetch("/create_checkout_session/")
            .then((result) => { return result.json(); })
            .then((data) => {
                console.log(data);
                // redirect to stripe checkout
                return stripe.redirectToCheckout({sessionId: data.sessionId}) 
            })
            .then((res) => {
                console.log(res);
            });
        });
    }
});


