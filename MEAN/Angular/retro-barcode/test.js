

function sort (arr, index=arr.length-1){
   if (index === 0){
      console.log(arr);
      return arr;
   }
   else if (arr[index] > arr[index-1]){
      let temp = arr[index];
      arr[index] = arr[index-1];
      arr[index-1] = temp;
      sort (arr, index = arr.length-1)
   }
   else{
      sort (arr, index -1)
   }
}

test = [ 1, 2, 3,4 ,1,1,1,1, 2,3,5,5,1,2,312,3,513,5,3 ,12,312,5,124]
test2 = [ 2,12,4,12,12,31,24,12,5,31,5,1,2,3,123,12,312,3]

sort (test, index=test.length-1);
sort (test2, index=test2.length-1);
