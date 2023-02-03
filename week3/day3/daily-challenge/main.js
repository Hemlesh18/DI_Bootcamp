const input = document.querySelector("#letter");
const letter_ALLOWED_STRING_REGEXP = (/[^A-Za-z]+$/);
input.addEventListener("keydown", event => {
    if (letter_ALLOWED_STRING_REGEXP.test(event.key)) {
        event.preventDefault();
    }
});


// function checkKey(key) {
//     return (key >= 'a' && key <= 'z') || (key >= 'A' && key <= 'Z') || ['Backspace'].includes(key);
// }