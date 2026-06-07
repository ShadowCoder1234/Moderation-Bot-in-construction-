

button = document.querySelector(".main")
mesageBtn = document.querySelector(".message")


button.addEventListener("click",() =>{
    location.reload()
    

})


mesageBtn.addEventListener("click", ()=>{
    window.open("https://www.youtube.com")
})


closeBtn = document.querySelector(".close")
display = document.querySelector(".box2")


closeBtn.addEventListener("click", ()=>{
    display.classList.toggle("hidden")
})


darkBtn = document.querySelector(".darkMode")
display1 = document.body


darkBtn.addEventListener("click", ()=>{
    display1.classList.toggle("dark")
    darkBtn.Text = "Light";
})