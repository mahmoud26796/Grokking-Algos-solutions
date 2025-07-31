function sum(arr){
    if(arr.length === 1) return arr[0];
    return arr[0] + sum(arr.slice(1, arr.length));
};

// console.log(sum([2, 4, 6]));


function countItems(arr) {
    if(arr.length === 1) return [arr[0]].length;
    return [arr[0]].length + countItems(arr.slice(1, arr.length));
};


// console.log(countItems([2, 4, 6]));


/////////////////////////////////////////////////

// write a recursive function that finds the maximum number in alist

function max_recur(arr){
    let sortedArr = arr.sort((a, b) => a - b);
    if(sortedArr.length === 1) return sortedArr[0];
    return max_recur(sortedArr.slice(1, sortedArr.length));
};

// console.log(max_recur([2, 4, 6]));
// console.log(max_recur([5, 3, 10, 35, 20]));


// recursive binary search approach 
function binarySearchRecur(arr, i, low = 0, heigh = arr.length - 1){
    let mid = Math.floor((low + heigh) / 2);    
    if(low >= heigh) return -1;
    if(arr[mid] === i){
        return mid;
    } else if(arr[mid] < i){
        return binarySearchRecur(arr, i, mid + 1, heigh);
    } else{
        return binarySearchRecur(arr, i, low, mid - 1);
    }
};

console.log(binarySearchRecur([1, 3, 5, 7, 9], 7));