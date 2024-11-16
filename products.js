function toggleLike(productId) {
    const button = document.querySelector(`#${productId} .like-btn`);
    if (button.classList.contains('liked')) {
        button.classList.remove('liked');
        button.style.color = "black";  // Reset color
    } else {
        button.classList.add('liked');
        button.style.color = "red";  // Change color to red
    }
}
