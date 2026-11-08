from random import sample as sp

card_num = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
card_color = ["♣️","♦️","♥️","♠️"]

all_card = []

#making card 
while True:
    for i in card_color:
        for j in card_num:
            all_card.append(f"{i}  {j}")


    #while True:
    user = sp(all_card,k=3)
    comp = sp(all_card,k=3)
    print(f"user choice: {user}")
    print(f"comp choice: {comp}")

    #asking user want to play
    inp = input("Enter want to exit [yes/ok]: ")

    if "ok" in inp:
        break

# print(all_card)
# print(len(all_card))
