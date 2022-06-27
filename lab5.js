console.log(sum([1, 50, 80, 80, 2]));
console.log(getNewArray(['asdsads', 'aaaasd', 'HHHAAA', 'Laith', 'Nassar']));

function sum(arr) {
    return arr.filter(elem => elem > 20).reduce((accu, current) => accu + current, 0);
}

const getNewArray = function(arr) {
    // return arr.filter(elem => elem.includes('a') && elem.length >= 5);
    return arr.filter(elem => elem.includes('a')).filter(elem => elem.length >= 5);
}