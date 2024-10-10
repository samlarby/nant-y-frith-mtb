console.log("It works!");

fetch("/config/")
.then((result) => {return result.json(); })
.then((data) => {
    const stripe = Stripe(data.publicKey)
});