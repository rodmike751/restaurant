// Setting current date and time
setInterval(() => {
    const full_date = new Date().toLocaleDateString(); //Date String
    const full_time = new Date().toLocaleTimeString(); // Time String

    document.querySelector(".todayDate").innerText = `${full_date}, ${full_time}`
}, 1000);



let isLoggedIn = false;
while (true) {
    isLoggedIn = (localStorage.getItem("isLoggedIn"))
    if (isLoggedIn === "false") {
        document.location.href = "/assets/login.html";
    }
    break
}

document.querySelector(".logout").addEventListener("click", (e) => {
    e.preventDefault();
    localStorage.setItem("isLoggedIn", false);
    document.location.href = "/assets/login.html"
})


// ##################################################################################################################################
const cartBtn = document.querySelector(".cartBtn");
const closeCart = document.querySelector(".closeCart")

let checkCart = 0;

function toggleCart() {
    if (checkCart === 1) {
        document.querySelector(".cart").style.display = "block";
        checkCart = 0;
    } else {
        checkCart = 1;
        document.querySelector(".cart").style.display = "none"
    }
}
cartBtn.addEventListener("click", () => toggleCart())
closeCart.addEventListener("click", () => toggleCart())

toggleCart();