function rot13(str) {
   let smallAlphabets = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz";
   let bigAlphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ";
   let newString = [];
   for (let i = 0; i < str.length; i++) {
      if (/[a-z]/.test(str[i])) {
         let found = smallAlphabets.search(str[i]);
         newString.push(smallAlphabets[found + 13]);
      } else if (/[A-Z]/.test(str[i])) {
         let found = bigAlphabets.search(str[i]);
         newString.push(bigAlphabets[found + 13]);
      } else {
         newString.push(str[i]);
      }
   }
   console.log(newString.join(""));
}
rot13("EBG13 rknzcyr.");
