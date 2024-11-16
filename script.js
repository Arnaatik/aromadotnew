function addToWishlist(perfumeId) {
    fetch("/wishlist", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ id: perfumeId }),
    })
        .then((response) => {
            if (response.ok) {
                alert("Added to wishlist!");
            } else {
                alert("Failed to add.");
            }
        })
        .catch((error) => console.error("Error:", error));
}
