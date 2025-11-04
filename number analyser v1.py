from datetime import datetime

number_3 = []
number_5 = []
number_3_5 = []

numbers = list(map(int,input(" your numbers with space after each one : ").split()))

now = datetime.now()
time = now.strftime("%Y-%m-%d %H:%M:%S")


for n in numbers :
    if n % 3 == 0 :
        number_3.append(n)
    if n % 5 == 0 :
        number_5.append(n)    
    if n % 3 == 0 and n % 5 == 0 :
        number_3_5.append(n)

# i like to keep my code optimazed so i will make call in        

with open("number_analyser_3_5.txt","a") as d :


    d.write(f"the list of numbers : {numbers} \n")
    d.write(f"\nCurrent time : {time}\n\n")
    d.write(" Results : \n\n")
    if number_3 :
        d.write(f" the list of number divisible by 3 : {number_3},with sum of : {sum(number_3)} and a max number :{max(number_3)} ")
    if number_5 :
        d.write(f" the list of number divisible by 5 : {number_5},with sum of : {sum(number_5)} and a max number :{max(number_5)} ")
    if number_3_5 :    
        d.write(f" the list of number divisible by 5 and 3 : {number_3_5},with sum of : {sum(number_3_5)} and a max number :{max(number_3_5)} ")
    d.write("===  Number Analyzer Report ! ===\n")
         

