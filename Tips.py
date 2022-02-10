from unittest import result


bill = int(input("The bill you have to give : $ "))
tips = int(input("Tips you want to Give : %"))
bill_tips = tips * bill / 100 + bill
people = int(input("Money you want to split between : $ "))
result = bill_tips / people
print(f"You have to give : $ {result}")
