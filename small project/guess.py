#number guessing game
#point reach 100 - 1

print("=====let's play game=====")

num = int(input("Enter num: "))

ext_num = 101

while num != ext_num:
    num = int(input("Enter again: "))

    if num == ext_num:
        print("you got this")
        break
    
print(num)
