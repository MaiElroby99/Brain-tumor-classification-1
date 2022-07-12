const actualbtn=document.querySelector("#actual-btn")
const custombtn=document.querySelector("#custom-btn")
const image=document.querySelector("#prev-image")
function uploadfile(){
    actualbtn.addEventListener("change",function(){
        const file=this.files[0]
        if(file){
            const reader=new FileReader()
            reader.onload =function(){
                const result=reader.result
                image.src=result

            }
            reader.readAsDataURL(file)
        }
    })
}