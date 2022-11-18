const signupBtn = document.querySelector("#signupBtn")
const loginBtn = document.querySelector(".loginBtn")

loginBtn.addEventListener("click", (e)=>{
    e.preventDefault();

    localStorage.setItem("isLoggedIn", true);
    document.location.href = "/"
})
// while(true){
    if ((localStorage.getItem("isLoggedIn")) === "true") {
        document.location.href = "/"
    }
// }