// Helper function to find the smallest number in the array 
const findSmallest = (arr) => {
    let smallest = arr[0];
    let smallestIdx = 0;
    for(let i = 1; i < arr.length; i++){
        if(arr[i] < smallest){
            smallest = arr[i];
            smallestIdx = i;
        }
    }
    return smallestIdx;
};

// Selection Sort Implementation
const selectionSort = (arr) => {
    let newArr = [];
    let smallestIdx;
    while(arr.length){
        smallestIdx = findSmallest(arr);
        newArr.push(arr[smallestIdx]);
        arr.splice(smallestIdx, 1);
    }
    return newArr;
};


// console.log(findSmallest([5, 3, 6, 2, 10]));
// console.log('\n###############################\n');
console.log(selectionSort([5, 3, 6, 2, 10]));