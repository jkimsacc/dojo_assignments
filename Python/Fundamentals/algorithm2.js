// insert
// interate from back, push every number 1 index until index i
// insert new value


function insert(arr, num, index){
  arr.length += 1;
  for (var i = arr.length-1; i > index; i--){
    arr[i] = arr[i-1];
  }
  arr[index] = num;
  return arr;
}

console.log( insert([1,2,3,4,5,6,7,8], 9, 4) );
