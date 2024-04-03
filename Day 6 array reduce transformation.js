nums = [1, 2, 3, 4]
fn = function sum(accum, curr) {
    return accum + curr;
}
init = 0

var reduce = function (nums, fn, init) {

    if (nums.length === 0) {
        return init;
    };
    for (const i in nums) {
        init = fn(init, nums[Number(i)]);
    };
    // We can also use the forEach function which would take each element and then it is passed to the fn.
    // Reduce method: array.reduce(fn, initialValue);
    // nums.forEach((element) => {
    //     init = fn(init, element)
    // });
    return init;
};

console.log(reduce(nums, fn, init))
