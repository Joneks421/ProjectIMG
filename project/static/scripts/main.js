const smoothLinks = document.querySelectorAll('a[href^="#"]');
for (let smoothLink of smoothLinks) {
    smoothLink.addEventListener('click', function (e) {
        e.preventDefault();
        const id = smoothLink.getAttribute('href');

        document.querySelector(id).scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    });
};

const faq_btn = document.querySelector('.faq-p > p');
const prev = document.querySelector('.btn-prev');
prev.addEventListener('click', function (e) {
    if (faq_btn.innerHTML === "Support") {
        faq_btn.innerHTML = "FaQ";}
    else {
        faq_btn.innerHTML = "Support";}
});

const next = document.querySelector('.btn-next');
next.addEventListener('click', function (e) {
    if (faq_btn.innerHTML === "FaQ") {
        faq_btn.innerHTML = "Support";}
    else {
        faq_btn.innerHTML = "FaQ";}
});
