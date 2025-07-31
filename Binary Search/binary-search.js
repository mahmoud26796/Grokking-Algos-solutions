const binarySearch =(arr, item) =>{
    let low = 0;
    let high = arr.length - 1;
    while(low <= high){
        guess = Math.floor((low + high ) / 2);
        if(item == arr[guess]) 
            return guess;
        else if (item < arr[guess])
            high = guess - 1;
        else 
            low = guess + 1;
    }
    return null; 
};

console.log(binarySearch([1, 3, 5, 7, 9], 7))
console.log(binarySearch([1, 3, 5, 7, 9], 8))
console.log(binarySearch([1, 3, 5, 7, 9], 3))
console.log(binarySearch([1, 3, 5, 7, 9], 9))
