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


const ViewBtn = document.querySelectorAll('.btn-view')
const BuyBtn = document.querySelectorAll('.btn-buy');
BuyBtn.forEach(val => {
    val.style.display = "none"
});
ViewBtn.forEach(val => {
    val.style.display = "none"
})

const SubDet = document.querySelectorAll('.subDet');
const hideSubDet = () => SubDet.forEach(val => {
    let targetValue = val;
    targetValue.style.opacity = "0";
})
hideSubDet();
SubDet.forEach((val) => {
    val.addEventListener("mouseover", (e) => {
        hideSubDet();
        val.style.opacity = "1";
        setTimeout(() => {
            val.children[2].style.display = "block";
            val.children[3].style.display = "block";
        }, 100);

        SubDet.forEach(value => {
            if (value !== val) {
                value.children[2].style.display = "none";
                value.children[3].style.display = "none";
            }
        })
    })
})

let cartTotal = 0;
let orderedMeals = [];

const addOrder = (name, price, img) => {
    orderedMeals.push({
        name,
        price,
        img
    })
    localStorage.setItem("orderedMeals", JSON.stringify(orderedMeals))
}

let numberOfOrdersInCart = 0;
document.querySelector(".countCart").innerHTML = numberOfOrdersInCart;
BuyBtn.forEach(val => {
    val.addEventListener("click", (e) => {
        let price = +(e.target.attributes?.price?.value);
        let name = e.target.attributes?.name?.value;

        cartTotal = cartTotal + +price;

        let foodImg = val.parentElement.parentElement.children[0].src;
        addOrder(name, price, foodImg)

        numberOfOrdersInCart += 1;
        document.querySelector(".countCart").innerHTML = numberOfOrdersInCart;
    })
})

const detailBuy = document.querySelector(".btnBuy");
detailBuy.addEventListener("click", ()=>{
    
    numberOfOrdersInCart += 1;
    document.querySelector(".countCart").innerHTML = numberOfOrdersInCart;
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