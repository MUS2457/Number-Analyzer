from datetime import datetime

def percentage(numb) :
    return round(((sum(numb) / sum(numbers)) * 100) ,1 )

number_3 = []
number_5 = []
number_3_5 = []
count_odd = 0
count_even = 0

numbers = list(map(int,input(" your numbers ; ").split()))

now = datetime.now()
time = now.strftime("%Y-%m-%d %H:%M:%S")

for n in numbers :
    if n % 3 == 0 :
        number_3.append(n)
    if n % 5 == 0 :
        number_5.append(n)   
    if n % 3 == 0 and n % 5 == 0 :
        number_3_5.append(n)     
    
    if n % 2 == 0 :
        count_even += 1
    else :
        count_odd += 1   

with open("number analyser.txt", "a") as f :
    f.write(f" all numbers : {numbers} ")
    f.write(f"\nCurrent time : {time}\n\n")
    f.write(" Results : \n\n")
    if number_3 :
        f.write(f" the list of number divisible by 3 : {number_3},with sum of : {sum(number_3)} and a max number :{max(number_3)},percentage : {percentage(number_3)} ")
    if number_5 :
        f.write(f" the list of number divisible by 5 : {number_5},with sum of : {sum(number_5)} and a max number :{max(number_5)}, percentage : {percentage(number_5)}")
    if number_3_5 :    
        f.write(f" the list of number divisible by 5 and 3 : {number_3_5},with sum of : {sum(number_3_5)} and a max number :{max(number_3_5)}, percentage : {percentage(number_3_5)} ")
    f.write(f"the number of odd : {count_odd}") 
    f.write(f" the number of even : {count_even}")   
    f.write("===  Number Analyzer Report ! ===\n")





