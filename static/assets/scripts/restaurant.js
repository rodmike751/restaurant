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