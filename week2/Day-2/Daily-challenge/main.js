let sentence = "The movie is  not that bad, I like it";
let wordBad = "bad"
let wordNot = "not"
let wordBad1 = sentence.search("bad");
let wordNot1 = sentence.search("not");

console.log(wordBad1);
console.log(wordNot1);
if (wordNot1 > wordBad1) {
    console.log(sentence = sentence.replace("not that bad ", "good"))
} else if (wordBad1 < wordNot1) {
    console.log(sentence = sentence.replace("not that bad, I like it", "bad"))
} else(console.log(sentence))