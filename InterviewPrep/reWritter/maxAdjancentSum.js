/* 
Dado un array de numeros enteros, 
Devuelve la suma mas grande 
entre dos numero adyacentes.
*/ 

const array = [2, 4, 1, 5, 6, 3]

function maxAdjacentSum(array){
    let maxSum = -Infinity
    const { length } = array 

    for (let i = 0; i < length - 1; i++){
        const sum = array[i] + array[i +1];
        // maxSum = Math.max(maxSum, sum)
        if (sum > maxSum){
            maxSum = sum;
        }
    }
    return maxSum;
}