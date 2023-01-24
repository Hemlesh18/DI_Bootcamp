let age = prompt("how old are you");
age = parseInt(age)
console.log(typeof(age))
if (age > 18) {
    alert("Powering On. Enjoy the ride!")
} else if (age < 18) {
    alert("you are too young to drive")
} else if (age === 18) {
    alert("Congratulations on your first year of driving.Enjoy the ride!");
} //  else { alert("enter your age") }