/*-----------------Daily Challenge: Not Bad------------*/

/*q1 Create a variable called sentence. The value of the variable should be a string that contains the words “not” and “bad”. For example, “The movie is not that bad, I like it”.*/

let sentence = "The game we watched is not that bad, I liked it.";

/*q2 Create a variable called wordNot where it’s value is the first appearance of the substring “not” (from the sentence variable).*/

let wordNot = sentence.search("not");

/*q3 Create a variable called wordBad where it’s value is the first appearance of the substring “bad” (from the sentence variable).*/

let wordBad = sentence.search("bad");

/*q4 If the word “bad” comes after the word “not”, you should replace the whole “not…bad” substring with “good”, then console.log the result.*/

if (wordNot < wordBad) {
    let newSentence = sentence.replace(/not|bad/gi, "good")
    console.log(newSentence);
} /*q5 If the word “bad” does not come after “not” or the words are not in the sentence, console.log the original sentence.*/ else {
    console.log(sentence);
};


