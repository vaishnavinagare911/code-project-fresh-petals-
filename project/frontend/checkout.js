// const BASE_URL = "http://127.0.0.1:5000/api";

function getToken(){
  return localStorage.getItem("token");
}

async function loadCheckout(){

const res = await fetch(BASE_URL + "/cart",{
headers:{ Authorization:"Bearer "+getToken() }
});

const data = await res.json();

if(!data.items || data.items.length === 0){

document.getElementById("checkoutContainer").innerHTML =
"<h2>Your cart is empty</h2>";

return;
}

let subtotal = 0;

data.items.forEach(item=>{
subtotal += item.price * item.quantity;
});

let itemsHTML = "";

data.items.forEach(item=>{

itemsHTML += `
<div class="checkout-item">
<span>${item.name}</span>
<span>Qty: ${item.quantity}</span>
<span>₹${item.price * item.quantity}</span>
</div>
`;

});

const html = `

<div class="checkout-layout">

<div class="checkout-left">

<h3>Shipping Address</h3>

<input id="name" placeholder="Full Name">
<input id="phone" placeholder="Phone">
<input id="address" placeholder="Address">
<input id="city" placeholder="City">
<input id="pincode" placeholder="Pincode">

<h3>Payment Method</h3>

<label>
<input type="radio" name="payment" value="upi">
UPI / Net Banking
</label>

<label>
<input type="radio" name="payment" value="cod">
Cash on Delivery
</label>

<div id="upiQRSection" style="display:none;">

<h3>Scan to Pay</h3>

<img id="upiQRImage" style="width:200px">

<p id="upiAmount"></p>

</div>

<button onclick="placeOrder()">Place Order</button>

</div>


<div class="checkout-right">

<h3>Order Summary</h3>

${itemsHTML}

<hr>

<h2>Total ₹${subtotal.toFixed(2)}</h2>

</div>

</div>

`;

document.getElementById("checkoutContainer").innerHTML = html;

setupPaymentListeners();

}


function setupPaymentListeners(){

const radios = document.querySelectorAll('input[name="payment"]');

radios.forEach(radio=>{

radio.addEventListener("change",function(){

if(this.value === "upi"){
loadUPIQR();
}else{
document.getElementById("upiQRSection").style.display="none";
}

});

});

}


async function loadUPIQR(){

const res = await fetch(BASE_URL + "/cart/get_qr",{
headers:{ Authorization:"Bearer "+getToken() }
});

const data = await res.json();

if(!res.ok){
alert(data.message);
return;
}

document.getElementById("upiQRImage").src =
"data:image/png;base64," + data.qr_code;

document.getElementById("upiAmount").innerText =
"Amount to pay: ₹" + data.total_amount;

document.getElementById("upiQRSection").style.display="block";

}


async function placeOrder(){

const name = document.getElementById("name").value.trim();
const phone = document.getElementById("phone").value.trim();
const address = document.getElementById("address").value.trim();
const city = document.getElementById("city").value.trim();
const pincode = document.getElementById("pincode").value.trim();

const payment = document.querySelector('input[name="payment"]:checked');

if(!name || !phone || !address || !city || !pincode){
alert("Please fill all shipping details");
return;
}

if(!/^[0-9]{10}$/.test(phone)){
alert("Enter valid 10 digit phone");
return;
}

if(!/^[0-9]{6}$/.test(pincode)){
alert("Enter valid 6 digit pincode");
return;
}

if(!payment){
alert("Please select payment method");
return;
}

try{
const cartRes = await fetch(BASE_URL + "/cart",{
headers:{ Authorization:"Bearer "+getToken() }
});
const cartData = await cartRes.json();
if(!cartData.items || cartData.items.length === 0){
alert("Your cart is empty.");
return;
}
}catch(e){
alert("Could not verify cart. Please try again.");
return;
}

try{

const res = await fetch(BASE_URL + "/payment",{
method:"POST",
headers:{
Authorization:"Bearer "+getToken(),
"Content-Type":"application/json"
},
body:JSON.stringify({
name,
phone,
address,
city,
pincode,
payment_method:payment.value
})
});

const data = await res.json();

if(!res.ok){
alert(data.message || "Order failed");
return;
}

showBillModal(data.order, data.bill_qr_code);

}catch(err){

alert("Something went wrong");

}

function showBillModal(order, billQrCode){
  if(!order) return;

  const modal = document.getElementById("billModal");
  if(modal) modal.style.display = "flex";

  const idEl = document.getElementById("billOrderId");
  if(idEl) idEl.textContent = (order._id || "").slice(-8);

  const createdEl = document.getElementById("billCreatedAt");
  if(createdEl){
    createdEl.textContent = order.created_at ? String(order.created_at).replace("T"," ").replace(/\.000Z$/,"") : "";
  }

  const pmEl = document.getElementById("billPaymentMethod");
  if(pmEl) pmEl.textContent = order.payment_method || "";

  const psEl = document.getElementById("billPaymentStatus");
  if(psEl) psEl.textContent = order.payment_status || "";

  const osEl = document.getElementById("billOrderStatus");
  if(osEl) osEl.textContent = order.order_status || "";

  const ship = order.shipping || {};
  const shipEl = document.getElementById("billShipping");
  if(shipEl){
    shipEl.innerHTML =
      escapeHtml(ship.name || "") + "<br>" +
      escapeHtml(ship.phone || "") + "<br>" +
      escapeHtml(ship.address || "") + "<br>" +
      escapeHtml(ship.city || "") + " - " + escapeHtml(ship.pincode || "");
  }

  const itemsRowsEl = document.getElementById("billItemsRows");
  const items = order.items || [];
  if(itemsRowsEl){
    itemsRowsEl.innerHTML = items.map((i)=>{
      const qty = Number(i.quantity || 0);
      const price = Number(i.price || 0);
      const subtotal = Number(i.subtotal || (price * qty));
      return `
        <tr>
          <td>${escapeHtml(i.name || "")}</td>
          <td class="text-right">${qty}</td>
          <td class="text-right">₹ ${price.toFixed(2)}</td>
          <td class="text-right">₹ ${subtotal.toFixed(2)}</td>
        </tr>
      `;
    }).join("");
  }

  const total = Number(order.total_amount || 0).toFixed(2);
  const billAmountEl = document.getElementById("billAmount");
  const billTotalEl = document.getElementById("billTotal");
  if(billAmountEl) billAmountEl.textContent = "₹ " + total;
  if(billTotalEl) billTotalEl.textContent = "₹ " + total;

  const qrImg = document.getElementById("billQrImage");
  if(qrImg && billQrCode){
    qrImg.src = "data:image/png;base64," + billQrCode;
  }
}

function closeBillModal(){
  const modal = document.getElementById("billModal");
  if(modal) modal.style.display = "none";
}

function printBill(){
  const billSection = document.querySelector("#billModal .bill-section");
  if(!billSection){
    window.print();
    return;
  }

  const printWindow = window.open("", "_blank");
  if(!printWindow){
    window.print();
    return;
  }

  const modal = document.getElementById("billModal");
  if(modal) modal.style.display = "flex";

  const billHtml = billSection.outerHTML;
  printWindow.document.open();
  printWindow.document.write(`
    <html>
      <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Print Bill</title>
        <link rel="stylesheet" href="styles.css" />
      </head>
      <body>
        ${billHtml}
      </body>
    </html>
  `);
  printWindow.document.close();
  printWindow.focus();

  setTimeout(() => {
    printWindow.print();
  }, 300);
}

function escapeHtml(s){
  const div = document.createElement("div");
  div.textContent = s == null ? "" : String(s);
  return div.innerHTML;
}

window.showBillModal = showBillModal;
window.closeBillModal = closeBillModal;
window.printBill = printBill;

}