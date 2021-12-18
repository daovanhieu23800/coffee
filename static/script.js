const  handleMenuTab1 = async ()=>{
    const response = await fetch('/items/favourite/');
    const myJson = await response.json();
    let newJson = [];
    if(myJson.length>12)
        newJson = myJson.slice(0,12);
    const html = myJson.map((items) =>{
         console.log(myJson);
    return `
    <div class="product-card">
                                <div class="product-card--image">
                                    <img src="/static/assets/${items.image}" alt="....">
                                    
                                </div>
                                <div class="product-card--info">
                                    <span id="product-name">
                                        <b>${items.name}</b></span>
                                    
                                    <div class="product-card--footer">
                                        <span>${items.price}</span>
                                        <div class="product-card--button" onclick="openCardPopup('${items.id}', '${items.name}', '${items.description}','${items.price}', '${items.image}')">
                                            <i class="fas fa-plus" ></i>
                                        </div>
                                    </div>
                                </div>
                            </div>
    `;
                }).join(" ");
    let a = document.querySelector("#first-menu-tab");
    a.innerHTML = html;          
};

const  handleMenuTab2 = async ()=>{
    const response = await fetch('/items/coffee/');
    const myJson = await response.json();
    let newJson = [];
    if(myJson.length>12)
        newJson = myJson.slice(0,12);
    const html = newJson.map((items) =>{
        // console.log(items);
    return `
    <div class="product-card">
                                <div class="product-card--image">
                                    <img src="/static/assets/${items.image}" alt="">
                                </div>
                                <div class="product-card--info">
                                    <span id="product-name"><b>${items.name}</b></span>
                                    <div class="product-card--footer">
                                        <span>${items.price}d</span>
                                        <div class="product-card--button" onclick="openCardPopup('${items.id}', '${items.name}', '${items.description}','${items.price}', '${items.image}')">
                                            <i class="fas fa-plus" ></i>
                                        </div>
                                    </div>
                                </div>
                            </div>
    `;
                }).join(" ");
    let a = document.querySelector("#second-menu-tab");
    a.innerHTML = html;          
};

const  handleMenuTab3 = async ()=>{
    const response = await fetch('/items/tea/');
    const myJson = await response.json();
    let newJson = [];
    if(myJson.length>12)
        newJson = myJson.slice(0,12);
    const html = newJson.map((items) =>{
        // console.log(items);
    return `
    <div class="product-card">
                                <div class="product-card--image">
                                    <img src="/static/assets/${items.image}" alt="">
                                </div>
                                <div class="product-card--info">
                                    <span id="product-name"><b>${items.name}</b></span>
                                    <div class="product-card--footer">
                                        <span>${items.price}d</span>
                                        <div class="product-card--button" onclick="openCardPopup('${items.id}', '${items.name}', '${items.description}','${items.price}', '${items.image}')">
                                            <i class="fas fa-plus" ></i>
                                        </div>
                                    </div>
                                </div>
                            </div>
    `;
                }).join(" ");
    let a = document.querySelector("#third-menu-tab");
    a.innerHTML = html;          
};
const  handleMenuTab4 = async ()=>{
    const response = await fetch('/items/ice/');
    const myJson = await response.json();
    let newJson = [];
    if(myJson.length>12)
        newJson = myJson.slice(0,12);
    const html = newJson.map((items) =>{
        // console.log(items);
    return `
    <div class="product-card">
                                <div class="product-card--image">
                                    <img src="/static/assets/${items.image}" alt="">
                                </div>
                                <div class="product-card--info">
                                    <span id="product-name"><b>${items.name}</b></span>
                                    <div class="product-card--footer">
                                        <span>${items.price}d</span>
                                        <div class="product-card--button" onclick="openCardPopup('${items.id}', '${items.name}', '${items.description}','${items.price}', '${items.image}')">
                                            <i class="fas fa-plus" ></i>
                                        </div>
                                    </div>
                                </div>
                            </div>
    `;
                }).join(" ");
    let a = document.querySelector("#four-menu-tab");
    a.innerHTML = html;          
};
const  handleNews = async ()=>{
    const response = await fetch('/getnews/');
    const myJson = await response.json();
    let newJson = [];
    if(myJson.length>6)
        newJson = myJson.slice(0,3);
    const html = newJson.map((items) =>{
        // console.log(items);
    return `
    <div class="news-card">
                        <img src="/static/assets/images/${items.avatar}" alt="news1">
                        <div class="news-content">
                            <h5>${items.title}</h5>
                            <p>${items.content}</p>
                            <div class="more-button">
                                <button>
                                    <a href="http://127.0.0.1:8000/newsdetail/${items.id}/">More</a>
                                </button>
                            </div>
                        </div>
                    </div>
    `;
                }).join(" ");
    let a = document.querySelector(".news-container");
    a.innerHTML = html;          
};

handleMenuTab1();
handleMenuTab2();
handleMenuTab3();
handleMenuTab4();
handleNews();

var $li = $('#pills-tab li').click(function() {
    $li.removeClass('selected');
    $(this).addClass('selected');
});

const clickLogin = ()=>{
    let loginbox = document.querySelector('.popup-login');
    
    loginbox.style.display = loginbox.style.display == "block" ? "none":"block";
}


const closeClickLogin = ()=>{
    let loginbox = document.querySelector('.popup-login');
    
    loginbox.style.display = "none";
}

const decreaseQuantity = (a)=>{
    // console.log(a);
    if(parseInt(a.nextElementSibling.innerText)>1){
        a.nextElementSibling.innerText = parseInt(a.nextElementSibling.innerText) - 1;
        if(a.nextElementSibling.innerText==1){
            a.classList.add("disabled_button");
            a.disabled = true;
        }
    }
    else 
    {
        a.classList.add("disabled_button");
        a.disabled = true;
    }
    let size = "";
    let plus = 0;
    let price = 0;
    var radios = document.getElementsByName("msize");
    var found = 1;
    for (var i = 0; i < radios.length; i++) {       
        if (radios[i].checked) {
            size = radios[i].value;
            found = 0;
            break;
        }
    }
    console.log(size);

    if(size ==  "M")
        plus = 5000;
    if(size ==  "L")
        plus = 10000;

    price = parseFloat(document.querySelector(".price").innerText.slice(1,));
    console.log(plus, " ", price);
    handlesize(plus,price);
}

const increaseQuantity = (a)=>{
     console.log("a");
     a.previousElementSibling.innerText = parseInt(a.previousElementSibling.innerText) + 1;
     a.previousElementSibling.previousElementSibling.disabled=false;
     a.previousElementSibling.previousElementSibling.classList.remove("disabled_button");
     let size = "";
     let plus = 0;
     let price = 0;
     var radios = document.getElementsByName("msize");
     var found = 1;
     for (var i = 0; i < radios.length; i++) {       
         if (radios[i].checked) {
             size = radios[i].value;
         found = 0;
             break;
         }
     }
     console.log(size);

     if(size ==  "M")
        plus = 5000;
     if(size == "L")
        plus = 10000;

     price = parseFloat(document.querySelector(".price").innerText.slice(1,));
     console.log(plus, " ", price);
     handlesize(plus,price);
    

}

const handlesize = (size, price) =>{
    let addbutton = document.querySelector("#totalPrice");
    let quantity = document.querySelector("#quantityofitem");
    addbutton.innerText =   (price+size) * parseInt(quantity.innerText)+ "VND" ;
}

const cancelCardPopup = () =>{
    document.querySelector('.card_popup-container').style.display = 'none';
}
const cancelPromotionPopup = () =>{
    document.querySelector('.promotion_popup-container').style.display = 'none';
}



const openCardPopup = (id, name, description, price,image) =>{
    document.querySelector('.card_popup-container').innerHTML = `
    <div class="card_popup">
            <div class="card_popup_cancel">
                <span><b>Order information</b></span>
                <button onclick="cancelCardPopup()">X</button>
            </div>
            <div class="card_popup-information">
                <img src="/static/assets/${image}" alt="">
                <div class="card_popup-title">
                    <b>${name}</b>
                    <div class="description">
                        ${description}
                    </div>
                </div>
            </div>
            <div class="card_popup-quantity">
                <span class="price">${price}VND</span>
                <div class="change_quantity">
                    <button class="decrease disabled_button" onclick="decreaseQuantity(this)" disabled>-</button>
                    <!-- <span contenteditable="true">0</span> -->
                    <span id="quantityofitem">1</span>

                    <button class="increase" onclick="increaseQuantity(this)" >+</button>
                </div>
            </div>
            <div class="card_popup-note">
                <div data-v-381448aa="" class="card-product-note-item">
                    <img data-v-381448aa="" src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMjAiIHZpZXdCb3g9IjAgMCAxOCAyMCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTE3IDIwSDFDMC43MzQ3ODQgMjAgMC40ODA0MyAxOS44OTQ2IDAuMjkyODkzIDE5LjcwNzFDMC4xMDUzNTcgMTkuNTE5NiAwIDE5LjI2NTIgMCAxOVYxQzAgMC43MzQ3ODQgMC4xMDUzNTcgMC40ODA0MyAwLjI5Mjg5MyAwLjI5Mjg5M0MwLjQ4MDQzIDAuMTA1MzU3IDAuNzM0Nzg0IDAgMSAwSDE3QzE3LjI2NTIgMCAxNy41MTk2IDAuMTA1MzU3IDE3LjcwNzEgMC4yOTI4OTNDMTcuODk0NiAwLjQ4MDQzIDE4IDAuNzM0Nzg0IDE4IDFWMTlDMTggMTkuMjY1MiAxNy44OTQ2IDE5LjUxOTYgMTcuNzA3MSAxOS43MDcxQzE3LjUxOTYgMTkuODk0NiAxNy4yNjUyIDIwIDE3IDIwWk01IDVWN0gxM1Y1SDVaTTUgOVYxMUgxM1Y5SDVaTTUgMTNWMTVIMTBWMTNINVoiIGZpbGw9IiNFNEU0RTQiLz4KPC9zdmc+Cg==" 
                    alt="" class="card-product-note-icon"> 
                    <input id ="note" name ="getnote" data-v-381448aa="" type="text" placeholder="Ghi chú thêm cho món này" class="card-product-text"></div>
            </div>
            <div class="title_choices">
                Chon size
            </div>
            <div class="multichoices">
                <div class="multichoice">
                    <input type="radio" id="s" name="msize" onclick="handlesize(0,${price})" value="S" checked>
                    <label for="s">S (+0)</label>
                </div>
                <div class="multichoice">
                    <input type="radio" id="m" name="msize" onclick="handlesize(5000,${price})" value="M">
                    <label for="m">M (+5000)</label>
                </div>
                <div class="multichoice">
                    <input type="radio" id="l" name="msize" onclick="handlesize(10000,${price})" value="L">
                    <label for="l">L (+10000)</label>
                </div>
            </div>
           
            <button data-action="add" onclick="addtocard('${id}', '${name}',${price})" class="addtocard">
                <span id="totalPrice"> ${price} VND </span>
            </button>
            

        </div>`
    document.querySelector('.card_popup-container').style.display = 'block';
}
// --------------
const addtocard = (id,name,price) =>{
    var action = 'add';
    console.log(name,price,id,action);
    let quantity = document.querySelector("#quantityofitem").innerText;
    console.log(quantity);
    var radios = document.getElementsByName("msize");
    var found = 1;
    for (var i = 0; i < radios.length; i++) {       
        if (radios[i].checked) {
            size = radios[i].value;
            found = 0;
            break;
        }
    }
    // -------------
    if(size == "m")
        plus = 1;
    if(size == "l")
        plus = 2;
        console.log(size);
    // -------------
    let note = document.getElementById('note').value;
    console.log(note);
    if (user === 'AnonymousUser'){
        console.log('not logged in')

    }
    else{
        updateUserOrder(id,name,price,action,quantity,size,note);

    }
}
function updateUserOrder(id,name,price,action,quantity,size,note){
    console.log('user is logged in,sending data')

    var url='/update_item/'
    console.log(quantity)
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'itemId':id, 'action':action, 'quantity':quantity,'size':size, 'note':note})
    })
    .then((response) =>{
        return response.json();
    })
    .then((data)=> {
        console.log('Data:',data)
        location.reload()
    });
}
// --------------
const addpromotion = (id) =>{
    var action = 'add';
    console.log(id);
    if (user === 'AnonymousUser'){
        console.log('not logged in')

    }
    else{
        updateintoOrder(id);

    }
}
function updateintoOrder(id){
    console.log('user is logged in,sending data')

    var url='/update_promotion/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'promotionId':id})
    })
    .then((response) =>{
        return response.json();
    })
    .then((data)=> {
        console.log('Data:',data)
        location.reload()
    });
}
const handlecoupon = (e)=>{
    let button = document.querySelector('.input-group-prepend');

    if(e!=""){
        button.classList.remove("disabled_button");
    }else{
        button.classList.add("disabled_button");
    }
}
const  handlePromotion = async ()=>{
    const response = await fetch('/getpromotions/');
    const myJson = await response.json();
    const html = myJson.map((items) =>{
         console.log(myJson);
    return `
    <div class="coupon-container">
        <img src="/static/assets/images/${items.avatar}" alt="coupon 105">
        <div class="coupon-information">
            <div class="coupon-description">${items.content}</div>
            <span>${items.expired}</span>
            <button data-action="add" onclick="addpromotion(${items.id})" class="addpromotion">
                Apply
            </button>
        </div>
    </div>
    `;
    }).join("");
    ///console.log(html);
        let a = document.querySelector(".allcoupon");
        console.log(a);
        a.innerHTML = html;
};

const showPromotion = ()=>{
    if(document.querySelector(".promotion_popup-container")==null){
    document.querySelector("body").innerHTML = `<div class="promotion_popup-container">
    <div class="promotion_popup-card">
        <div class="card_popup_cancel">
            <span>Promotion</span>
            <button onclick="cancelPromotionPopup()">X</button>
        </div>

        <div data-v-5c47adee="" class="
            input-group
            mb-3
            tch-delivery__input
            d-flex
            align-items-center
            promotion_popup-inputcode
          ">
            <img data-v-5c47adee="" 
            src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdCb3g9IjAgMCAxOCAxOCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEyIDBIMThWNUgxNlYySDEyVjBaTTYgMFYySDJWNUgwVjBINlpNMTIgMThWMTZIMTZWMTNIMThWMThIMTJaTTYgMThIMFYxM0gyVjE2SDZWMThaTTAgOEgxOFYxMEgwVjhaIiBmaWxsPSIjRkE4QzE2Ii8+Cjwvc3ZnPgo=" 
            alt="" class="cam-scan input-group-text"> 
            <input data-v-5c47adee="" type="text" placeholder="Nhập mã khuyến mãi" aria-label="" aria-describedby="basic-addon1" class="form-control " oninput="handlecoupon(this.value)"> 
            <div data-v-5c47adee="" class="input-group-prepend disabled_button" >
          <button data-v-5c47adee="" type="button" class="btn  btn--radius-right-4" disabled><span data-v-5c47adee="" class="text-apply" >Áp dụng</span></button></div>
        </div>

        <div class="title_choices">
            Sap het han
        </div>
        <div class="allcoupon" id ="getallcoupon">
        </div>
        
    </div>
</div>`+ document.querySelector("body").innerHTML;
        handlePromotion();}
        else {
            document.querySelector(".promotion_popup-container").style.display="block";
        }
}

// -------------
