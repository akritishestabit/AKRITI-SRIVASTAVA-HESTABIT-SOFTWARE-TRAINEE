const grid = document.getElementById("productGrid");
const searchInput = document.getElementById("searchInput");
const sortSelect = document.getElementById("sortSelect");

let products = [];

async function fetchProducts() {
    try {
        const res = await fetch("https://dummyjson.com/products");
        const data = await res.json();
        products = data.products;
        renderProducts(products);
    } catch (error) {
        console.error("Failed to fetch products", error);
    }
}

function renderProducts(list) {
    grid.innerHTML = "";
    list.forEach(product => {
        const card = document.createElement("div");
        card.className = "card";

        card.innerHTML = `
            <img src="${product.thumbnail}" alt="${product.title}">
            <h3>${product.title}</h3>
            <p>$ ${product.price}</p>
        `;

        grid.appendChild(card);
    });
}

searchInput.addEventListener("input", () => {
    const value = searchInput.value.toLowerCase();
    const filtered = products.filter(p =>
        p.title.toLowerCase().includes(value)
    );
    renderProducts(filtered);
});


sortSelect.addEventListener("change", () => {
    let sorted = [...products];

    if (sortSelect.value === "high") {
        sorted.sort((a, b) => b.price - a.price);
    } else if (sortSelect.value === "low") {
        sorted.sort((a, b) => a.price - b.price);
    }

    renderProducts(sorted);
});

fetchProducts();
