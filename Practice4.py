import random

pc_num = random.randint(0 , 30)

user_num = -1

Numbers = []

while pc_num != user_num:
    
    print('Enter your Number:')
    
    user_num = int(input())

    Numbers.append(user_num)

    if user_num > pc_num:
        print("boro paein")

    elif user_num < pc_num:
        print('boro bala')

    else:
        print('Congratulation!!!')

    

print(len(Numbers))