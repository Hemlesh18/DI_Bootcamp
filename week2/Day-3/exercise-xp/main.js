// ex-1 list people
// const people = ["Greg", "Mary", "Devon", "James"];
// Q1
// const x = people.shift()
// console.log(people);
//q2
// people.splice(2, 3, "Jason")
// console.log(people);
//q3
// people.push("khavind")
// console.log(people);
// q4
// console.log(people.indexOf("Mary"));
//q5
// console.log(people.slice(1, 3));
//q6
// console.log(people.indexOf("foo"));
//Why does it return -1 ?it is because the value is not found in the array.
// let last = console.log(people[-1]);
//part2
//q1
// people.forEach(item => { console.log(item); });
//q2
// people.forEach(item => {
//     console.log(item);
//     // people.brake("Jason");
// });
// for (let i = 0; i < people.length; i++) {
//     console.log(people);
//     if (people[i] === "Jason") { brake; }
// }
//
//exercise2

// const colors = ["purple", "black", "blue", "orange", "white"];
// //2
// for (let i = 0; i < colors.length; i++) {
//     console.log("my " + "#" + (i + 1) + " choice " + "is " + colors[i])
// }

//
//exercise 3

//const h = (prompt("enter a number"));
//const number = Number(h)
//while (h < 10) { h = prompt("number should be higher") }
//exercise4
// const building = {
//     numberOfFloors: 4,
//     numberOfAptByFloor: {
//         firstFloor: 3,
//         secondFloor: 4,
//         thirdFloor: 9,
//         fourthFloor: 2,
//     },
//     nameOfTenants: ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent: {
//         sarah: [3, 990],
//         dan: [4, 1000],
//         david: [1, 500],
//     },
// }
// console.log(building.numberOfFloors)
// console.log(building.numberOfAptByFloor.firstfloor)
// console.log(building.numberOfAptByFloor.thirdfloor)
// console.log(building.nameOfTenants[1] + " number of room: " + building.numberOfRoomsAndRent["dan"][0])
// if (building.numberOfRoomsAndRent["sarah"][1] + building.numberOfRoomsAndRent["david"][1] > 1000) { building.numberOfRoom };
// console.log(building.numberOfRoomsAndRent);
//exercise6
// const details = {
//     my: 'name',
//     is: 'Rudolf',
//     the: 'raindeer'
// }
// let x = "";
// for (let sentence in details) {
//     x = x + sentence + " " + details[sentence] + " ";
// }
// console.log(x);
//exercise 7
// const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
// let Y = ""
// const sortedArray = names.sort()
// for (const name of sortedArray) {
//     console.log(name)
//     Y = Y + name[0]
// };
// console.log(Y)

//ex 5
// const family = {
//     dad: "sam",
//     mom: "nid",
//     child: "ben"
// }
// for (const key in family) {
//     console.log("key", key)
// }
// for (const key in family) {
//     console.log("value", family[key])
// }