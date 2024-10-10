console.log("Sanity check!");

fetch("/config/")
.then((result) => {return result.json(); })
.then((data) => {
    
    const stripe = Stripe("data.publicKey"); 

    let submitBtn = document.querySelector("#submitBtn");
    if (submitBtn !== null) {
        submitBtn.addEventListener("click", () => {
        // get checkout session id
        fetch("/create-checkout-session/")
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

