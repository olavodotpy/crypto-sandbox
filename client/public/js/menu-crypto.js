document.addEventListener("DOMContentLoaded", function() {
    const openMenuCrypto = document.getElementById("menuCrypto");
    const closeMenuCrypto = document.getElementById("ExitMenuCrypto");
    const menuCrypto = document.getElementById("contentMenuCrypto");
    const overlay = document.getElementById("overlay");

    openMenuCrypto.addEventListener("click", function() {
        menuCrypto.classList.add("open");
        overlay.style.display = "block";
    });

    closeMenuCrypto.addEventListener("click", function() {
        menuCrypto.classList.remove("open");
        overlay.style.display = "none";
    });

    overlay.addEventListener("click", function() {
        menuCrypto.classList.remove("open");
        overlay.style.display = "none";
    });
});
