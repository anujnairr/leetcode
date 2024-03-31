// Given an integer array arr and a mapping function fn, return a new array with a transformation applied to each element.

// The returned array should be created such that returnedArray[i] = fn(arr[i], i).

// Please solve it without the built-in Array.map method.

arr = [1, 2, 3];
fn = function plusone(n) {
    return n + 1;
};

arr = [10, 20, 30];
fn = function constant() {
    return 42;
};

var map = (arr, fn) => {
    let temparr = [];
    for (let i = 0; i < arr.length; i++) {
        temparr.push(fn(arr[i], i));
    };
    return temparr;
};

console.log(map(arr, fn));