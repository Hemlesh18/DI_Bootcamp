let timeout;

function myFunction() {
    timeout = setTimeout(alertFunc, 2000);
}

function alertFunc() {
    alert("Hello world");
}
myFunction();
document.querySelector('button').addEventListener('click', (event) => {
    document.querySelectorAll('p').forEach((paragraph) => {
        paragraph.classList.toggle('pilcrow');
    });


});