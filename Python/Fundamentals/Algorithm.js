//reverse
function reverse(str){
//declare empty str
  var strreversed = ""; //declare empty str
  for (var i = str.length-1; i >= 0; i--){ //for loop backwords
    console.log(i);
    strreversed += str.charAt(i); //add str to new str from back
  }
  return strreversed; //return new str
}

console.log(reverse("meow"))

function insert(str1, n, str2){
  var str3= ""; //declare empty str
  for (var i = 0; i < n; i++){ //loop index 0 to n-1
    console.log(i);
    str3 += str1.charAt(i); //add strs before index n to empty str
  }
  str3 += str2; //add str2 after empty str
  for (var j = n; j < str1.length; j++){ //loop index n to str1.length
    console.log(j);
    str3 += str1.charAt(j); //add str after n to arr.length-1
  }
  return str3; //return result
}

console.log(insert("something", 2, "meow"));
