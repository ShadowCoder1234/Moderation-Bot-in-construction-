const island = document.querySelector(".island")
 const music_button = document.querySelector(".musicButton")
 const FaceID_button = document.querySelector(".faceId")
 const CallButton = document.querySelector(".call")
 const MusicUI = document.getElementsByClassName("musicUI")


 island.addEventListener("click", ()=>{
    island.classList.toggle("expand")
 })

 function SetState(state){

    if(island.classList.contains(state)){
        island.classList.remove(state)
        return;         
    }

    island.classList.remove("music","call-state", "timer", "faceid")
    island.classList.add(state)

 }



 music_button.addEventListener("click", ()=>{
    SetState("music")
   
    
 })

 FaceID_button.addEventListener("click",() =>{
    SetState("faceid")
    
 })

 CallButton.addEventListener("click", ()=>{
    SetState("call-state")

 })