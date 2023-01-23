const fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
console.log(fruits);
fruits.pop(0);
console.log(fruits);
fruits.sort();
console.log(fruits)
fruits.push("kiwi")
console.log(fruits)
const removeApple = fruits.slice(1);
console.log(removeApple);
removeApple.reverse();
console.log(removeApple)
    //exercise 2//
const moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1][1][0]);