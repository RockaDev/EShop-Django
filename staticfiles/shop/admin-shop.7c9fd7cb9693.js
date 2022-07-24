const new_product = document.getElementById('add_product')
const show_form = document.getElementById('product-form')
const close = document.getElementById('close-product')
new_product.addEventListener("click", () => {
    show_form.style.display = "block";
});
close.addEventListener("click", () => {
    show_form.style.display = "none";
});