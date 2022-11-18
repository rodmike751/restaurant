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
const addCart = (foodName) => {
    let cartItem = document.createElement("small");
    let removeFood = document.createElement("i");
    removeFood.classList.add("fa fa-times");
    cartItem.append(removeFood);
    cartItem.append(foodName)

    document.querySelector(".allSelected").append(cartItem)
}

const addOrder = (name, price, img) => {
    orderedMeals.push({
        name,
        price,
        img
    })
    localStorage.setItem("orderedMeals", JSON.stringify(orderedMeals))
}
const deleteOrder = (name) => {
    orderedMeals.forEach((val, idx) => {
        return val.name === name && orderedMeals.splice(idx, 1)
    })
}

let numberOfOrdersInCart = 0;
document.querySelector(".countCart").innerHTML = numberOfOrdersInCart;
BuyBtn.forEach(val => {
    val.addEventListener("click", (e) => {
        let price = +(e.target.attributes?.price?.value);
        let name = e.target.attributes?.name?.value;

        cartTotal = cartTotal + +price;
        document.getElementById("totalPrice").innerHTML = `$${cartTotal}`;

        let cartItem = document.createElement("small");
        let removeFood = document.createElement("i");

        removeFood.setAttribute("id", price)

        removeFood.classList.add("fa");
        removeFood.classList.add("fa-times")
        removeFood.classList.add("removeFood")
        cartItem.append(removeFood);
        let foodName = document.createElement("b");
        foodName.append(name)
        cartItem.append(foodName)

        document.querySelector(".allSelected").append(cartItem)
        let foodImg = val.parentElement.parentElement.children[0].src;
        addOrder(name, price, foodImg)

        numberOfOrdersInCart += 1;
        document.querySelector(".countCart").innerHTML = numberOfOrdersInCart;
    })
})


const placeOrder = (e) => {
    e.preventDefault();
    console.log(orderedMeals)
    if (orderedMeals.length === 0) {
        return alert("Please your order list is empty")
    }
    document.getElementById("recentOrders").innerHTML = ""
    orderedMeals = orderedMeals.reverse();
    orderedMeals.forEach((val, idx) => {
        let orderItem = document.createElement("div")
        orderItem.classList.add("orderItem");
        let imgName = document.createElement("aside");
        let foodImgContainer = document.createElement("div")
        foodImgContainer.classList.add("foodImg");
        let foodImg = document.createElement("img")
        foodImg.setAttribute("src", val.img);
        foodImgContainer.append(foodImg)

        let foodTitle = document.createElement("div")
        foodTitle.classList.add("foodTitle");
        let foodName = document.createElement("small")
        foodName.innerText = val.name;

        let orderDate = new Date().toLocaleDateString();
        let orderTime = new Date().toLocaleTimeString();
        const orderTimeDate = document.createElement("small")
        if (orderedMeals[idx]["date"] === undefined) {
            orderedMeals[idx]["date"] = `${orderDate}, ${orderTime}`;
            orderTimeDate.innerText = `${orderDate}, ${orderTime}`;
        } else {
            orderTimeDate.innerText = val.date;
        }



        foodTitle.append(foodName);
        foodTitle.innerHTML += "<br>"
        foodTitle.append(orderTimeDate)

        imgName.append(foodImgContainer);
        imgName.append(foodTitle);

        let priceContainer = document.createElement("div")
        priceContainer.classList.add("price");
        let price = document.createElement("b")
        price.innerText = `$${val.price}`;
        priceContainer.append(price);

        orderItem.append(imgName);
        orderItem.append(priceContainer)
        console.log("pass")
        document.getElementById("recentOrders").append(orderItem)
    })

    document.querySelector(".allSelected").innerHTML = "";

    alert("Total price was $" + cartTotal)
    document.getElementById("totalPrice").innerHTML = "$0"
    cartTotal = 0;
}

const placeOrderBtn = document.querySelector(".placeOrderBtn");
placeOrderBtn.addEventListener("click", (e) => placeOrder(e))




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


const bars = document.querySelector(".fa-bars");
const sideBar = document.querySelector(".sideBar");
let checkSidebar = false;
function checkBar(){
    if(!checkSidebar){
        sideBar.classList.remove("showSidebar")
        bars.classList.remove("fa-times")
        if(!bars.classList.contains("fa-bars")){
            bars.classList.add("fa-bars")
        }
    }else{
        sideBar.classList.add("showSidebar")
        bars.classList.add("fa-times")
        if (bars.classList.contains("fa-bars")) {
            bars.classList.remove("fa-bars")
        }
    }
}
bars.addEventListener("click",()=>{
    checkSidebar = !checkSidebar;
    checkBar();
})