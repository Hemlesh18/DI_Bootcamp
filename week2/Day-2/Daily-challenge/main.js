 let sentence = "This dinner is bad !"
     // let sentence = "This movie is not so bad"
     // let sentence = "This dinner is not that bad ! You cook well"

 let wordBad1 = sentence.search("bad");
 let wordNot1 = sentence.search("not");

 console.log(wordBad1);
 console.log(wordNot1);


 if (wordNot1 === -1) { console.log(sentence) } else if (wordNot1 < wordBad1) {
     console.log((sentence = sentence.slice(0, wordNot1, ) + "good !"))
 }