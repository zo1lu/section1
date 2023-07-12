//Additional Task 1
function maxProduct(nums){
    let maxProduct = nums[0]*nums[1];
    for (let i=0; i<nums.length-1;i++){
        for (let j=i+1;j<nums.length;j++){
            let product= nums[i]*nums[j]
            if(product>maxProduct){
                maxProduct=product
            }
        }
    }
    console.log(maxProduct)
}
console.log("=====Task1=====")
maxProduct([10,-20,0,3])//print 30
maxProduct([10,-20,0,-3])//print 60
maxProduct([5,20,2,6])//print 120
maxProduct([-1,2])//print -2
maxProduct([-1,0,2])//print 0
maxProduct([5,-1,-2,0])//print 2
maxProduct([-5,-2])//print 10


//Additional Task 2
function twoSum(nums,target){
    let ansIndex=[]
    for (let i=0; i<nums.length-1;i++){
        for (let j=i+1;j<nums.length;j++){
            if(nums[i]+nums[j]==target){
                ansIndex.push(i);
                ansIndex.push(j);
                return ansIndex
            }
        }
    }
    if(ansIndex==[]){
        console.log("None")
    }
}
console.log("=====Task2=====")
let result = twoSum([2,11,7,15],9);
console.log(result);