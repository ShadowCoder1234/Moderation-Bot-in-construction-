const island = document.querySelector(".island")
 const music_button = document.querySelector(".musicButton")
 const FaceID_button = document.querySelector(".faceId")
 const CallButton = document.querySelector(".call")
 const MusicUI = document.getElementsByClassName("musicUI")


 island.addEventListener("click", ()=>{
    SetState("expand")
 })

 function SetState(state){

    if(island.classList.contains(state)){
        island.classList.remove(state)
        return;         
    }

    island.classList.remove("music","call-state", "timer", "faceid", "expand")
    island.classList.add(state)

 }



 music_button.addEventListener("click", ()=>{
    SetState("music")
   
    
 })

 FaceID_button.addEventListener("click",() =>{
    SetState("faceid")
    checked()
    
 })

 CallButton.addEventListener("click", ()=>{
    SetState("call-state")

 })


 const bars = document.querySelectorAll(".visualiser span")

let heights = [12,16,22,30,38,44,38,30,22,16]

let offset = 0;


function animation(){
   bars.forEach((bar, i)=>{
      const h = 25 +
            8 * Math.sin(offset + i * 0.4) +
            6 * Math.sin(offset * 1.7 + i * 0.8) +
            4 * Math.cos(offset * 2.3 + i * 0.2);

      bar.style.height = `${Math.max(8,h)}px`

   })
   offset += 0.05

   requestAnimationFrame(animation)
}

animation();






const ring = document.querySelectorAll(".ring");
const finder = document.querySelector(".finder");
const tick = document.querySelector(".tick")

function checked(){
   ring.forEach(ring=>{
       ring.classList.add("rotate");
   })

   

    setTimeout(()=>{
      ring.forEach(ring=>{
         ring.style.opacity = "0"

      })

        
        finder.style.opacity = "0";


        tick.style.opacity = "1"


    },1000);

    setTimeout(()=>{ 

        island.classList.remove("faceid");
      ring.forEach(ring=>{
         ring.classList.remove("rotate")
        ring.style.opacity = "1";

      })
        finder.style.opacity = "1";

        tick.style.opacity = "0"

      
     

    },1700);

}