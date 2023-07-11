import re
# =====Task1=====
def find_and_print(messages):
    #find people who say
    #1."18 years old" or older than 18 years old.
    #2."college student"
    #3."of legal age in Taiwan"
    for msg in messages :
        quote = messages[msg]
        validate = re.search("(?i)([2-9]\d|1[8-9])(-|\s)years(-|\s)old",quote)
        if "college student" in quote:
            print(msg)
        elif "of legal age in Taiwan" in quote:
            print (msg)
        elif validate:
            print (msg)


print("===Task1===")
find_and_print({
"Bob":"My name is Bob. I'm 18 years old.",
"Mary":"Hello, glad to meet you.",
"Copper":"I'm a college student. Nice to meet you.",
"Leslie":"I am of legal age in Taiwan.",
"Vivian":"I will vote for Donald Trump next week",
"Jenny":"Good morning."
})

# =====Task2=====
def calculate_sum_of_bonus(data):
    bonusSum = 0
    # iterate through employees data to calculate each one's bonus than sum up!
    for employee in data["employees"]:
        salary = employee['salary']
        perf = employee['performance']
        role = employee['role']
        
        #check if salary string or integer
        try:
            # check if type of salary is integer
            salary= int(salary)
        except:
            #convert USD to NTD then string to integer
            if "USD" in salary:
                salary= int(salary.replace("USD",""))*30
            #convert string with "," to integer
            elif "," in salary:
                salary = int(salary.replace(",",""))

        #base on employee's role, the rate is different
        if role == "Engineer":
            rate = 0.2
        elif role == "CEO":
            rate = 0.3
        elif role == "sales":
            rate = 0.2
        #perfRate depends on their performance
        if perf == "above average" :   
            perfRate = 0.5
        elif perf =="average":
            perfRate = 0.3
        elif perf =="below average":
            perfRate = 0.1
        #bonus = salary * rate * perfomaceRate
        bonusSum+= salary*rate*perfRate
    print("Sum of Bonus is:" + str(int(bonusSum)))    

print("===Task2===")
calculate_sum_of_bonus({
"employees":[
{
"name":"John",
"salary":"1000USD",
"performance":"above average",
"role":"Engineer"
},
{
"name":"Bob",
"salary":60000,
"performance":"average",
"role":"CEO"
},
{
"name":"Jenny",
"salary":"50,000",
"performance":"below average",
"role":"Sales"
}
]
}) # call calculate_sum_of_bonus function

# =====Task3=====
def func(*data):
    # compare each name's second word in the data list with rest of the names' second word.
    count=0
    for name in data:
        key = name[1]
        index = data.index(name)
        # each person's second word is assumed unique at begining.
        unique = True
        dataLen = len(data)
        #compare with others to check if it's really unique
        for i in range(dataLen):
            #if they are same data, we don't need to compare, pass!
            if i == index:
                continue
            #if the second word is the same then it is not unique! And we don't need to check it anymore, so break the loop.
            elif key == data[i][1]:
                unique=False
                break
        #after the loop finished and it is still unique then print it! and unique name count is plus by one.
        if unique:
            print(name)
            count+=1
    #if no one is unique, which means count==0, than print "沒有"!        
    if count==0:        
        print("沒有")

    # print("========")
    # count=0
    # for name in data:
    #     name,*others=data
    #     print(name+"&"+",".join(others))
    #     key = name[1]
    #     unique= True
    #     for other in others:
    #         if key == other[1]:
    #             unique=False
    #             break
    #     if unique:
    #         print(name)
    #         count+=1    
    # if count==0:
    #     print("沒有")
print("===Task3===")
func("彭⼤牆", "王明雅", "吳明") # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有


# =====Task4=====
def get_number(index):
    if index%2==0:
        print(int(index/2*3))
    else:
        print(int((index+1)/2*3+1))

print("===Task4===")
get_number(1) # print 4
get_number(5) # print 10
get_number(10) # print 15



# =====Task5=====
def find_index_of_car(seats, status, number):
    #create an array to record each car's suitability
    #if the car serve passengers for now, than record the number: (available seats number - passenger's number)
    #if it's not serving passenger than it will be recorded -1
    suitability=[]
    carLen = len(seats)
    for i in range(carLen):
        if status[i]==1:
            suitability.append(seats[i]-number)
        else:
            suitability.append(-1)

    #after create the suitability array
    #we need to find the smallest positive number,which means the most suitable!
    #set the best fit index of car -1 means no car is suitable at first! If there is any car suit, than index will be changed.
    bestFitIndexOfCar=-1
    #set a number bigger than seats number of A car.
    suitabilityMin=100
    # iterate through the suitability array to find the minimum.
    for i in range(carLen):
        suitabilityNum=suitability[i]
        if (suitabilityNum>-1) & (suitabilityNum<suitabilityMin):
            bestFitIndexOfCar=i
            suitabilityMin = suitabilityNum

    print(bestFitIndexOfCar)

print("===Task5===")
find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2) # print 4
find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2
