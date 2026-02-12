const headers = document.querySelectorAll(".accordion-header");

headers.forEach(header => {
    header.addEventListener("click", () => {

        const content = header.nextElementSibling;
        const icon = header.querySelector(".icon");

        const isOpen = content.style.maxHeight;

        document.querySelectorAll(".accordion-content").forEach(item => {
            item.style.maxHeight = null;
        });

        document.querySelectorAll(".icon").forEach(i => {
            i.textContent = "+";
        });

        if (!isOpen) {
            content.style.maxHeight = content.scrollHeight + "px";
            icon.textContent = "−";
        }
    });
});
