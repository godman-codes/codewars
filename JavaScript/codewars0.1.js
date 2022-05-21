// Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

// All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

// Examples
// * With input "10.0.0.0", "10.0.0.50"  => return   50
// * With input "10.0.0.0", "10.0.1.0"   => return  256
// * With input "20.0.0.10", "20.0.1.0"  => return  246

function ipsBetween(start, end) {
   //TODO
   let splitStart = start.split(".");
   let splitEnd = end.split(".");
   let firstDifference = splitEnd[0] - splitStart[0];
   let secondDifference = splitEnd[1] - splitStart[1];
   let thirdDifference = splitEnd[2] - splitStart[2];
   let fourthDifference = splitEnd[3] - splitStart[3];
   console.log(
      firstDifference * 256 * 256 * 256 +
         secondDifference * 256 * 256 +
         thirdDifference * 256 +
         fourthDifference
   );
}
ipsBetween("10.11.12.13", "10.11.13.0");
ipsBetween("150.0.0.0", "150.0.0.1");
ipsBetween("10.0.0.0", "10.0.0.50");
ipsBetween("20.0.0.10", "20.0.1.0");
ipsBetween("10.11.12.13", "10.11.13.0");
ipsBetween("160.0.0.0", "160.0.1.0");
ipsBetween("170.0.0.0", "170.1.0.0");
ipsBetween("50.0.0.0", "50.1.1.1");
ipsBetween("180.0.0.0", "181.0.0.0");
ipsBetween("1.2.3.4", "5.6.7.8");
ipsBetween("0.0.0.0", "255.255.255.255");
