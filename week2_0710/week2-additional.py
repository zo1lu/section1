#Additional Task 1
def max_product(nums):
    maxProduct=nums[0]*nums[1]
    for i in range(len(nums)-1):
        for j in range (i+1,len(nums)):
            product=nums[i]*nums[j] 
            if(product>maxProduct):
                maxProduct=product
    print(maxProduct)            
print("=====Task1=====")
max_product([5,20,2,6])#print 120
max_product([10,-20,0,3])#print 30
max_product([10,-20,0,-3])#print 60
max_product([-1,2])#print -2
max_product([-1,0,2])#print 0
max_product([5,-1,-2,0])#print 2
max_product([-5,-2])#print 10


#Additional Task 2
def two_sum(nums, target):
    ansIndex = []
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if((nums[i]+nums[j])==target):
                ansIndex.append(i)
                ansIndex.append(j)
                return ansIndex
    if(ansIndex==[]):
        print("None!")

        
print("=====Task2=====")
result=two_sum([2,11,7,15],9)
print(result)