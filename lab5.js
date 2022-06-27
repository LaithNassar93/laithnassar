console.log(sum([3, 12, 50, 90, 22]));
console.log(getNewArray(['asdsads', 'aaaasd', 'HHHAAA', 'Laith', 'Nassar']));

function sum(arr) {
    return arr.filter(temp => temp > 20).reduce((accu, current) => accu + current, 0);
}

const getNewArray = function(arr) {
    return arr.filter(temp => temp.includes('a')).filter(temp => temp.length >= 5);
}