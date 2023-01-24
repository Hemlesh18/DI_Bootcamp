//exercise1
let x = 5;
let y = 2;
if (x > y) { console.log(x = "x is the biggest number") }
//exercise2
//1
let newDog = "chihuahua";
//2
let length = newDog.length;
console.log(length);
//3
console.log(newDog = newDog.toLocaleUpperCase());
console.log(newDog = newDog.toLowerCase());
//4
if (newDog == "chihuahua") {
    console.log("I love Chihuahuas, it’s my favorite dog breed ")
} else {
    console.log("I dont care, I prefer cats")
}

//exercise3
let xyz = prompt("enter a number");
xyz = parseInt(xyz)
console.log(xyz)
if (xyz % 2 == 0) {
    console.log(xyz = xyz + " is an even number")
} else {

    console.log(xyz = xyz + "is an odd number ")
};
//exercise4
const users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
console.log("number of user online " + users.length)
if (users == 0) {
    console.log("no one is online")
} else if (users.length == 1) {
    console.log(users + " is 0nline")
} else if (users.length == 2) {
    console.log(users + " is 0nline")
} else if (users.length > 2) {
    console.log(users.splice(0, 2) + "and " + users.length + " are online ")
}