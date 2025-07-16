'''
You are given a weekly allowance of ₦2000. Your job is to use Python assignment operators to simulate how you spend and manage your money throughout the week.
---
✅ Instructions:
Write a Python program that performs the following steps and prints the allowance after each one:
You spent ₦400 on books.
You found ₦100 under your bed and added it to your allowance.
You bought snacks worth ₦250.
You gave 25% of your current allowance to your younger sibling.
You used one-third of what’s left to buy data.
You split the remaining balance equally between savings and tithing.
Finally, calculate what remains after removing all complete ₦100 notes using the modulus assignment operator (%=).
'''
print (f"My allowance for the week is 2000")
print("*********************************\n")
weekly_allowance = 2000
weekly_allowance -= 400
print(f"My remaining allowance after buying books is: {weekly_allowance}")

print("*********************************\n")
weekly_allowance += 100
print(f"My balance after finding money under the  bed is: {weekly_allowance}")

print("*********************************\n")
weekly_allowance -= 250
print(f"Balance after buying snacks is: {weekly_allowance}")

print("*********************************\n")
percent = 25/100
percent *= weekly_allowance
weekly_allowance -= percent
print(f"Balance after giving 25% of my money to my siblings: {weekly_allowance}")

print("*********************************\n")
one_third = weekly_allowance /3
weekly_allowance -= one_third
print(f"Balance after buying data: {weekly_allowance}")

print("*********************************\n")
weekly_allowance //= 2
print(f"Balance after spliting the balance between savings and tithes: {weekly_allowance}")

print("*********************************\n")
weekly_allowance %= 100
print(f"total balance of money remaining: {weekly_allowance}")
