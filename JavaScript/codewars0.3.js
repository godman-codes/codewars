function nextSmaller(n) {
   var arr = n.toString().split("").map(Number);
   console.log(arr);
   let temp2 = [];
   for (var i = arr.length - 1; i >= 0; i--) {
      if (arr[i] < arr[i - 1]) {
         let temp = arr[i - 1];
         console.log(temp);
         temp2 = arr.slice(0, i - 1);
         let mark = iterate2(arr.slice(i - 1, arr.length));
         let john = temp2.concat(mark).join("");
         if (john[0] == 0) {
            console.log(-1);
            return -1;
         } else {
            console.log(parseInt(john));
            return parseInt(john);
         }
      }
   }
   return -1;
}
function iterate2(n) {
   console.log(n);
   let temp = n[0];
   console.log(temp);
   let temp2 = [];
   let temp3 = [];
   for (var i = 0; i < n.length; i++) {
      if (n[i] < temp) {
         n[0] = n[i];
         n[i] = temp;
         temp2 = n.slice(0, i);
         temp3 = n.slice(i, n.length);
         console.log(temp3);
         temp3.reverse();
         return temp2.concat(temp3);
      }
   }
}

nextSmaller(1234567908);
// nextSmaller(2071);
// nextSmaller(1027);
