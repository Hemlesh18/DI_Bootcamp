//exercise 1
//part1
// function infoAboutMe() {
//     let name = "khavind"
//     let age = 21
//     let hobby = "games "

//     console.log("my name is  " + name + ", i am " + age + "year old" +
//         "my hobby is playing " + hobby)
// }
// infoAboutMe()
//part 2
// function infoAboutPerson(personName, personAge, personFavoriteColor) {
//     console.log("You name is " + personName + ",you are " + personAge + "years old, your favorite color is " + personFavoriteColor)
// }
// infoAboutPerson("David", 45, "blue")
// infoAboutPerson("Josh", 12, "yellow")
//ecercise2
// function calculetorTip() {
//     const bill = Number(prompt("enter bill amount"))
//     if (bill < 50) {
//         tip = 0.2 * bill;
//     } else if (bill > 50 && bill < 200) {
//         tip = 0.15 * bill;
//     } else if (bill > 200) {
//         tip = 0.1 * bill;
//     }
//     console.log("bill:", bill)
//     console.log("tip:", tip)
// }
// calculetorTip()
// function isDivisible() {
//     let sum = 0
//     for (let x = 0; x < 500; x++) {
//         if (x % 23 === 0) {
//             console.log(sum = sum + x)

//         }
//     }
//     console.log("sum:", sum)
// }
// isDivisible()

// function isDivisible(divisor) {
//     let sum = 0
//     for (let x = 0; x < 500; x++) {
//         if (x % divisor === 0) {
//             console.log(sum = sum + x)

//         }
//     }
//     console.log("sum:", sum)
// }
// isDivisible(3)
// isDivisible(45)


//exercise4
// const stock = {
//     "banana": 6,
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry": 1
// }

// const prices = {
//     "banana": 4,
//     "apple": 2,
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry": 10
// }
// const shoppinglist = ["banana", "orange", "apple"]

// function myBill() {}
// myBill()
//exercise5
// function changeEnough(itemPrice, amountOfChange) {
//     console.log("item price:", itemPrice)
//     const sum = claculatesum(amountOfChange)
//     return (sum > itemPrice)
//         // if (sum > itemPrice) {
//         //     return true
//         // } else {
//         //     return false
//         // }

// }

// function claculatesum(arr) {
//     let sum = 0
//     for (let i = 0; i < arr.length; i++) {
//         let coinValue
//         const numberofcoins = arr[i]
//         if (i === 0) { coinValue = 0.25 } else if (i === 1) {
//             coinValue = 0.10
//         } else if (i === 2) { coinValue = 0.05 } else if (i === 3) {
//             coinValue = 0.01
//         }
//         console.log("we have", numberofcoins, "coins that have a value of", coinValue)
//         sum = sum + numberofcoins * coinValue

//     }

//     console.log("you own", sum)
//     return sum
// }
// changeEnough(4.25, [25, 20, 5, 0])
// changeEnough(14.11, [2, 100, 0, 0])
// changeEnough(0.75, [0, 0, 20, 5])