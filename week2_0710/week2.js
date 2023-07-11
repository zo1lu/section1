// =====Task1=====
function findAndPrint(messages){
    // find people who say
    // 1."18 years old" or older than 18 years old.
    // 2."college student"
    // 3."of legal age in Taiwan"
    for (const name in messages){
        let quote = messages[name];
        // issue#1:new RegExp not work
        if (quote.includes("college student")){
            console.log(name);
        }else if (quote.includes("of legal age in Taiwan")){ 
            console.log(name);
        }else if (/([2-9]\d|1[8-9])(-|(\s))years(-|(\s))old/i.test(quote)){
            console.log(name);
        }
    }
}
console.log("===Task1===")
findAndPrint({
"Bob":"My name is Bob. I'm 18 years old.",
"Mary":"Hello, glad to meet you.",
"Copper":"I'm a college student. Nice to meet you.",
"Leslie":"I am of legal age in Taiwan.",
"Vivian":"I will vote for Donald Trump next week",
"Jenny":"Good morning."
});

// =====Task2=====
function calculateSumOfBonus(data){
    // iterate through employees data to calculate each one's bonus than sum up!
    let bonusSum=0
    for (employee of data['employees']){
        let perfRate=0
        let rate=0
        salary = employee['salary']
        perf = employee['performance']
        role = employee['role']

        // data cleaning:
        //1.USD>>NTD
        //2.erase "," 
        //3.string>integer
        typeof(salary)=="string"&&salary.includes("USD")?salary=parseInt(salary.replace("USD",""))*30:
        typeof(salary)=="string"&&salary.includes(",")?salary=parseInt(salary.replace(",","")):
        salary=parseInt(salary)
        
        //base on employee's role, the rate is different
        role==="Engineer"?rate = 0.2:
        role==="CEO"?rate = 0.3:
        rate = 0.2
        
        //perfRate depends on their performance
        perf==="above average"?perfRate=0.5:
        perf==="average"?perfRate=0.3:
        perfRate=0.1
        
        //bonus = salary * rate * perfomaceRate
        bonusSum+= salary*rate*perfRate
    }
    console.log(`Sum of Bonus is:${bonusSum}`);
}
console.log("===Task2===")
calculateSumOfBonus({
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
}); // call calculateSumOfBonus function
// =====Task3=====
function func(...data){
    //compare each name's second word in the data list with rest of the names' second word.
    let count=0
    for (let i in data){
        let name = data[i]
        //each person's second word is assumed unique at begining.
        let unigue = true
        //compare with others' name to check if it's really unique
        for (let j in data){
            //if they are same data, we don't need to compare, pass!
            if (i == j){
                continue
            //if the second word is the same then it is not unique! And we don't need to check it anymore, so break the loop.
            }else if(name[1]==data[j][1]){
                unigue=false
                break
            }
        }
        //after the loop finished and it is still unique then print it! and unique name count is plus by one.
        if(unigue){
            console.log(name)
            count+=1
        }
    }
    //if no one is unique, which means count==0, than print "沒有"!    
    if (count==0){
        console.log("沒有")
    }
}
console.log("===Task3===")
func("彭⼤牆", "王明雅", "吳明"); // print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有

// =====Task4=====
function getNumber(index){
    index%2==0?console.log(parseInt(index/2*3)):
    console.log(parseInt(index+1)/2*3+1)
}
console.log("===Task4===")
getNumber(1); // print 4
getNumber(5); // print 10
getNumber(10); // print 15

// =====Task5=====
function findIndexOfCar(seats, status, number){
    // create an array to record each car's suitability
    // if the car serve passengers for now, than record the number: (available seats number - passenger's number)
    // if it's not serving passenger than it will be recorded -1
    let suitability = [];
    for (let i in seats){
        if (status[i]==1){
            suitability.push(seats[i]-number)
        }else{
            suitability.push(-1)
        }
    }
    // after create the suitability array
    // we need to find the smallest positive number,which means the most suitable!
    // set the best fit index of car -1 means no car is suitable at first! If there is any car suit, than index will be changed.
    let bestFitIndexOfCar=-1
    // set a number bigger than seat number in a car
    let suitabilityMin = 100 
    //iterate through the suitability array to find the minimum.
    for(let j in suitability){
        let suitabilityNum = suitability[j];
        if(suitabilityNum>-1&&suitabilityNum<suitabilityMin){
            bestFitIndexOfCar=j;
            suitabilityMin=suitabilityNum
        }
    }
    console.log(bestFitIndexOfCar)
}
console.log("===Task5===")
findIndexOfCar([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2); // print 4
findIndexOfCar([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1
findIndexOfCar([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2