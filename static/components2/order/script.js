const  handleMenuTab1 = async ()=>{
    const response = await fetch('https://617bd868d842cf001711c0fe.mockapi.io/item');
    const myJson = await response.json();
    let newJson = [];
    if(myJson.length>12)
        newJson = myJson;
    const html = newJson.map((items) =>{
        // console.log(items);
    return `
    <div class="product-card">
                                <div class="product-card--image">
                                    <img src="./assets/images/coffee1.jpg" alt="">
                                </div>
                                <div class="product-card--info">
                                    <span id="product-name"><b>${items.name}</b></span>
                                    <div class="product-card--footer">
                                        <span>$${items.price}</span>
                                        <div class="product-card--button" onclick="openCardPopup('${items.name}', '${items.description}','${items.price}', '${items.image}')">
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
    const response = await fetch('https://617bd868d842cf001711c0fe.mockapi.io/item2');
    const myJson = await response.json();
    let newJson = [];
    if(myJson.length>12)
        newJson = myJson;
    const html = newJson.map((items) =>{
        // console.log(items);
    return `
    <div class="product-card">
                                <div class="product-card--image">
                                    <img src="./assets/images/coffee2.jpg" alt="">
                                </div>
                                <div class="product-card--info">
                                    <span id="product-name"><b>${items.name}</b></span>
                                    <div class="product-card--footer">
                                        <span>$${items.price}</span>
                                        <div class="product-card--button">
                                            <i class="fas fa-plus"></i>
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
    const response = await fetch('https://617bd868d842cf001711c0fe.mockapi.io/item3');
    const myJson = await response.json();
    let newJson = [];
    if(myJson.length>12)
        newJson = myJson;
    const html = newJson.map((items) =>{
        // console.log(items);
    return `
    <div class="product-card">
                                <div class="product-card--image">
                                    <img src="./assets/images/coffee3.jpg" alt="">
                                </div>
                                <div class="product-card--info">
                                    <span id="product-name"><b>${items.name}</b></span>
                                    <div class="product-card--footer">
                                        <span>$${items.price}</span>
                                        <div class="product-card--button">
                                            <i class="fas fa-plus"></i>
                                        </div>
                                    </div>
                                </div>
                            </div>
    `;
                }).join(" ");
    let a = document.querySelector("#third-menu-tab");
    a.innerHTML = html;          
};

handleMenuTab1();
handleMenuTab2();
handleMenuTab3();

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
    if(size == "m")
        plus = 1;
    if(size == "l")
        plus = 2;

    price = parseFloat(document.querySelector(".price").innerText.slice(1,));
    console.log(plus, " ", price);
    handlesize(plus,price);
}

const increaseQuantity = (a)=>{
    // console.log("a");
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
    if(size == "m")
        plus = 1;
    if(size == "l")
        plus = 2;

    price = parseFloat(document.querySelector(".price").innerText.slice(1,));
    console.log(plus, " ", price);
    handlesize(plus,price);

}

const handlesize = (size, price) =>{
    let addbutton = document.querySelector("#totalPrice");
    let quantity = document.querySelector("#quantityofitem");
    addbutton.innerText = "$" + (price+size) * parseInt(quantity.innerText);
}

const cancelCardPopup = () =>{
    document.querySelector('.card_popup-container').style.display = 'none';
}
const cancelPromotionPopup = () =>{
    document.querySelector('.promotion_popup-container').style.display = 'none';
}

const openCardPopup = (name, description, price,image) =>{
    document.querySelector('.card_popup-container').innerHTML = `
    <div class="card_popup">
            <div class="card_popup_cancel">
                <span><b>Order information</b></span>
                <button onclick="cancelCardPopup()">X</button>
            </div>
            <div class="card_popup-information">
                <img src="./assets/images/coffee1.jpg" alt="">
                <div class="card_popup-title">
                    <b>${name}</b>
                    <div class="description">
                        ${description}
                    </div>
                </div>
            </div>
            <div class="card_popup-quantity">
                <span class="price">$${price}</span>
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
                    <input data-v-381448aa="" type="text" placeholder="Ghi chú thêm cho món này" class="card-product-text"></div>
            </div>
            <div class="title_choices">
                Chon size
            </div>
            <div class="multichoices">
                <div class="multichoice">
                    <input type="radio" id="s" name="msize" onclick="handlesize(0,${price})"   value="s" checked>
                    <label for="s">S (+0)</label>
                </div>
                <div class="multichoice">
                    <input type="radio" id="m" name="msize" onclick="handlesize(1,${price})" value="m">
                    <label for="m">M (+1)</label>
                </div>
                <div class="multichoice">
                    <input type="radio" id="l" name="msize" onclick="handlesize(2,${price})" value="l">
                    <label for="l">L (+2)</label>
                </div>
            </div>
            <div class="addtocard">
                <span id="totalPrice">$12</span>
                <span> - add</span>
            </div>
        </div>`
    document.querySelector('.card_popup-container').style.display = 'block';
}


const handlecoupon = (e)=>{
    let button = document.querySelector('.input-group-prepend');

    if(e!=""){
        button.classList.remove("disabled_button");
    }else{
        button.classList.add("disabled_button");
    }
}

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
        <div class="allcoupon">
            <div class="coupon-container">
                <img src="./assets/images/coupon10.jpg" alt="coupon 105">
                <div class="coupon-information">
                    <div class="coupon-description">Giảm 15% từ 3 sản phẩm Cà phê đóng gói/Lon & nước</div>
                    <span>het han trong 2 ngay</span>
                    <button>Apply</button>
                </div>
            </div>
            <div class="coupon-container">
                <img src="./assets/images/coupon10.jpg" alt="coupon 105">
                <div class="coupon-information">
                    <div class="coupon-description">Giảm 15% từ 3 sản phẩm Cà phê đóng gói/Lon & nước</div>
                    <span>het han trong 2 ngay</span>
                    <button>Apply</button>
                </div>
            </div>
            <div class="coupon-container">
                <img src="./assets/images/coupon10.jpg" alt="coupon 105">
                <div class="coupon-information">
                    <div class="coupon-description">Giảm 15% từ 3 sản phẩm Cà phê đóng gói/Lon & nước</div>
                    <span>het han trong 2 ngay</span>
                    <button>Apply</button>
                </div>
            </div>
            <div class="coupon-container">
                <img src="./assets/images/coupon10.jpg" alt="coupon 105">
                <div class="coupon-information">
                    <div class="coupon-description">Giảm 15% từ 3 sản phẩm Cà phê đóng gói/Lon & nước</div>
                    <span>het han trong 2 ngay</span>
                    <button>Apply</button>
                </div>
            </div>
        </div>
        
    </div>
</div>`+ document.querySelector("body").innerHTML;}
        else {
            document.querySelector(".promotion_popup-container").style.display="block";
        }
}