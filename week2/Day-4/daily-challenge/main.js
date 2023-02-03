const words = prompt("enter words seperated by commas ");
const word = words.split(",")

// function log(wordEnter) {
//     console.log(wordEnter);
// }
// word.forEach(log);
let lengthOfLongestWord = 0;
for (const wordEnter of word) {
    console.log(wordEnter);
    const wordlength = word.length
    if (wordlength > lengthOfLongestWord) {
        lengthOfLongestWord = wordlength;
    }
    console.log("lengthOfLongestWord:", lengthOfLongestWord);
}
const numberOfStarOnfirstRow = lengthOfLongestWord + 4;

const firstRow = createFirstRow()
console.log("firstRow:", firstRow)

function createFirstRow() {
    let row = ""
    for (let i = 0; i < numberOfStarOnfirstRow; i++) { row = row + "*" }
    return row
}