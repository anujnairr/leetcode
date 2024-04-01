// Filter Elements from Array
// Given an integer array arr and a filtering function fn, return a filtered array filteredArr.

// The fn function takes one or two arguments:

// arr[i] - number from the arr
// i - index of arr[i]
// filteredArr should only contain the elements from the arr for which the expression fn(arr[i], i) evaluates to a truthy value.
// A truthy value is a value where Boolean(value) returns true.

// Please solve it without the built-in Array.filter method.


var filter = function (arr, fn) {
    // This is imperative programming
    let filteredArr = [];
    // for (const i in arr) {                   i in arr will provide the index, but as a string so convert to Number.
    //     if (fn(arr[i], Number(i))) {         i of arr will provide the element but not index.
    //         filteredArr.push(arr[i]);
    //     };
    // };

    for (let i = 0; i < arr.length; i++) {
        if (fn(arr[i], i)) {
            filteredArr.push(arr[i]);
        };
    };
    return filteredArr;

    // This is declarative programming
    // return arr.filter((n, i) => { return n > 10; })
    // return arr.filter(fn);

};

// Input1:
arr = [0, 10, 20, 30]
fn = function greaterThan10(n) {
    return n > 10;
}

console.log(filter(arr, fn));

// Input2:
// arr = [1, 2, 3]
// fn = function firstIndex(n, i) {
//     return i === 0;
// }

