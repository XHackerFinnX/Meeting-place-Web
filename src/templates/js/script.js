document.addEventListener("DOMContentLoaded", function() {
    const links = document.querySelectorAll('nav a');

    links.forEach(link => {
        link.addEventListener('click', function() {
            alert(`Вы перешли на раздел: ${this.textContent}`);
        });
    });
});
