/*
In this program, I write a function that in javascript that checks if a string is a palindrome. 
*/


//Declaring and intializing a variable
function palindrome(str){

  //Lenght of the string
  var length = str.length;

  //To check palindrome, we go through a loop
  for (var i = 0; i < length/2; i++) {
    //str[i] goes through from index 0
    //str[length - 1 - i] goes from index n-1
    if (str[i] !== str[length - 1 - i]) {
      //false if the values don't match
      return false;
    }
  }
  //true if the values match
  return true;
}

//amma is plaindrome
var amma = palindrome("amma");
//javascript is not a palindrome
var js = palindrome("javascript");

console.log(amma);
console.log(js);

