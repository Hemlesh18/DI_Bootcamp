// exercise1 
let favoriteFood = "pizza"
let favoriteMeal = "dinner"
    // let food = "i eat " + favoriteFood + "at every " + favoriteMeal
console.log("i eat " + favoriteFood + " at every " + favoriteMeal)
    //exercise2
    //part1
    //1
const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength = myWatchedSeries
console.log(myWatchedSeriesLength)
    //2
let myWatchedSeriesSentence = "i watched 3 series : " + myWatchedSeries;
console.log(myWatchedSeriesSentence)
    //3
console.log("i watched 3 series : " + myWatchedSeries)
    //part2
    //1
myWatchedSeries.splice(2, 2, "friends")
console.log(myWatchedSeries)
    //2
myWatchedSeries.push("Sao")
console.log(myWatchedSeries)
    //3
myWatchedSeries.unshift("sam")
console.log(myWatchedSeries)
    //4
myWatchedSeries.splice(1, 1, )
console.log(myWatchedSeries)

//exercise3
let temperatureCelsius = 39;
let temperatureFahenheit = (((temperatureCelsius / 5) * 9) + 32)
console.log(temperatureFahenheit)
    //exercise4
let c;
let a = 34;
let b = 21;

console.log(a + b) //first expression
    // Prediction:it will output 55,because a and b  data type is intiger
    // Actual:55

a = 2;

console.log(a + b) //second expression
    // Prediction:it will output 23 ,because a value is 2 and b 21 
    // Actual:23
    //What is the value of c? undefine
console.log(3 + 4 + '5');
//prediction:output will be 75, because 3 + 4= 7 and 5 is set as a string
// actual:75

//exercise5

typeof(15)
// Prediction:number
// Actual:intiger

typeof(5.5)
// Prediction:decimal
// Actual:float

typeof(NaN)
// Prediction:
// Actual:not a number

typeof("hello")
// Prediction:string
// Actual:string

typeof(true)
// Prediction:boolean
// Actual:boolean

typeof(1 != 2)
// Prediction:true
// Actual:boolean

"hamburger" + "s"
// Prediction:hamburgers
// Actual:string addition

"hamburgers" - "s"
// Prediction:nothing will happen...substraction cannot be use with string containing alphabet
// Actual:NaN

"1" + "3"
// Prediction:13
// Actual:13

"1" - "3"
// Prediction:-2
// Actual:-2

"johnny" + 5
// Prediction:
// Actual:johnny5

    "johnny" - 5
    // Prediction:2 different data type
    // Actual:NaN

99 * "hello"
    // Prediction:multiplication should be done with 2 number/ineger/float
    // Actual:NaN

1 != 1
    // Prediction:1 is equal to 1 same data type and same value
    // Actual:false boolean

1 == "1"
    // Prediction:same value
    // Actual:true boolean

1 === "1"
    // Prediction:different data type
    // Actual:false boolean
    //exercise 6
5 + "34"
    // Prediction:it become 534 because 5 is a number and "34"is a string
    // Actual:534

5 - "4"
    // Prediction:string contain an integer value substraction occur
    // Actual:1

10 % 5
    // Prediction:no remainder
    // Actual:0

5 % 10
    // Prediction: divides a variable by the value of the right operand and assigns the remainder to the variable
    // Actual:5

    "Java" + "Script"
    // Prediction:its become one word
    // Actual:JavaScript

" " + " "
// Prediction:2 empty string
// Actual:empty line 

" " + 0
// Prediction: empty string+ integer 0=0
// Actual:0

true + true
    // Prediction:true(1)+true(1)
    // Actual:2

true + false
    // Prediction:true(1)+false(0)=1
    // Actual:

false + true
    // Prediction:false(0)+true(1)=1
    // Actual:1

false - true
    // Prediction:false(0)-true(1)=-1
    // Actual:-1

    !true
    // Prediction:! mean not 
    // Actual:false

3 - 4
    // Prediction:substraction of integer
    // Actual:-1

    "Bob" - "bill"
    // Prediction:not a number
    // Actual:NaN