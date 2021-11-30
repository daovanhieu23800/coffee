var addtocardBtns = document.getElementsByClassName("addtocard")

for (i=0 ; i<addtocardBtns.length;i++){
    addtocardBtns[i].addEventListener('click',function(){
        var name = this.dataset.name
        var action = this.dataset.action
        console.log(name, action)
    })
}