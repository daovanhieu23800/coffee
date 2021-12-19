
const  handleNews = async ()=>{
    const response = await fetch('/getnews/');
    const myJson = await response.json();
    let newJson = [];
    if(myJson.length>6)
        newJson = myJson.slice(0,6);
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
                                    <a href="/newsdetail/${items.id}">More</a>
                                </button>
                            </div>
                        </div>
                    </div>
    `;
                }).join(" ");
    let a = document.querySelector(".news-container");
    a.innerHTML = html;          
};

handleNews();

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
const cancelPromotionPopup = () =>{
    document.querySelector('.promotion_popup-container').style.display = 'none';
}

const clickLogin = ()=>{
    let loginbox = document.querySelector('.popup-login');
    
    loginbox.style.display = loginbox.style.display == "block" ? "none":"block";
}


const closeClickLogin = ()=>{
    let loginbox = document.querySelector('.popup-login');
    
    loginbox.style.display = "none";
}
