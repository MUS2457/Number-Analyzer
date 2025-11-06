import json
from datetime import datetime

def percentage(num) :
    return round((sum(num)/sum(numbers)) * 100,1)

number_3 = []
number_5 = []
number_3_5 = []
odd = []
even = []


numbers = list(map(int,input(" your numbers separated by space : ").split()))

now = datetime.now()
time = now.strftime("%Y-%m-%d %H:%M:%S")

for n in numbers :
    if n % 3 == 0 :
        number_3.append(n)
    if n % 5 == 0 :
        number_5.append(n) 
    if n % 3 == 0 and  n % 5 == 0 :
        number_3_5.append(n)     

    if n % 2 != 0 :
        odd.append(n)  
    else :
        even.append(n)      

# data is a dic that include all results ,perpose

data = { "numbers" : numbers, "sum all" : sum(numbers),
    "number d 3" : number_3, "sum" : sum(number_3) if number_3 else 0,"percentage" : percentage(number_3),"max" : max(number_3) if number_3 else None,"min" : min(number_3) if number_3 else None,
    "number d 5" : number_5, "sum" : sum(number_5) if number_5 else 0,"percentage" : percentage(number_5),"max" : max(number_5) if number_5 else None,"min" : min(number_5) if number_5 else None,
    "number d 3 and 5" : number_3, "sum" : sum(number_3) if number_3 else 0,"percentage" : percentage(number_3_5),"max" : max(number_3_5) if number_3_5 else None,"min" : min(number_3_5) if number_3_5 else None,
    "even" : even,"count even" : len(even),"sum" : sum(even) if even else 0,"percentage" : percentage(even),"max" : max(even) if even else None,"min" : min(even) if even else None,
    "odd" : odd,"count odd" : len(odd),"sum" : sum(odd) if odd else 0,"percentage" : percentage(odd),"max" : max(odd) if odd else None,"min" : min(odd) if odd else None
}

# txt is to make it easier for user to read the result

with open("number analyser v3.txt", "w") as f :
    f.write(f" all numbers : {numbers} ")
    f.write(f"\nCurrent time : {time}\n\n")
    f.write(" Results : \n\n")
    if number_3 :
        f.write(f" the list of number divisible by 3 : {number_3},with sum of : {sum(number_3)} and a max number :{max(number_3)} and min number{min(number_3)} ,percentage : {percentage(number_3)} ")
    if number_5 :
        f.write(f" the list of number divisible by 5 : {number_5},with sum of : {sum(number_5)} and a max number :{max(number_5)} and min number {min(number_5)}, percentage : {percentage(number_5)}")
    if number_3_5 :    
        f.write(f" the list of number divisible by 5 and 3 : {number_3_5},with sum of : {sum(number_3_5)} and a max number :{max(number_3_5)} and min number {min(number_3_5)}, percentage : {percentage(number_3_5)} ")
    if odd :    
        f.write(f"list of odd numbers : {odd}, with a max : {max(odd)} and min : {min(odd)}, the number of odd : {len(odd)} ,percentage : {percentage(odd) }") 
    if even :    
        f.write(f"list of even numbers : {even}, with a max : {max(even)} and min : {min(even)}, the number of even : {len(even)} ,percentage : {percentage(even) }") 
    f.write("===  Number Analyzer Report ! ===\n")

with open("number analyser v3.json","w") as j :
    json.dump(data, j, indent=4)
        
print(json.dumps(data, indent=4))     # so it can show in the terminal   

