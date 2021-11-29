var addtocardBtns = document.getElementsByClassName("addtocard")

for (i=0 ; i<addtocardBtns.length;i++){
    addtocardBtns[i].addEventListener('click',function(){
        var action = this.dataset.action
        console.log(action)
    })
}