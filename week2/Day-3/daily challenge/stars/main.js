for (let x = 0; x <= 5; ++x) {
    let star = "* ".repeat(x + 1);
    console.log(star);
}

//2 nested for loops
let n = 6;
let star1 = "";
for (let i = 1; i <= n; i++) {
    for (let j = 0; j < i; j++) {
        star1 += "* ";
    }
    star1 += "\n";
}
console.log(star1);