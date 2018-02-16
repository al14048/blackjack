import random

#fisrt card

def first_card(dealer_hand, player_hand, card):
	dealer_hand.append(card.pop(0))
	dealer_hand.append(card.pop(0))
	player_hand.append(card.pop(0))
	player_hand.append(card.pop(0))




def point(hand):
	num = 0
	for i in hand:
		if i[1]!=1 and i[1]<10:
			num += i[1]
		elif i[1]>=10:
			num += 10
		elif i[1]== 1:
			if num>=11:
				num += 1
			elif num<=10:
				num += 11
	return num


card = []
card_mark = ["heart", "spade", "club", "diamond"]
card_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for i in card_mark:
	for j in card_num:
		card.append([i,j])
	

def judge(dealer_point,player_point):
	if dealer_point > 21:
		return 0
	elif player_point > 21:
		return 1
	elif dealer_point == player_point:
		return 2
	elif dealer_point > player_point:
		return 1
	elif dealer_point < player_point:
		return 0
# 0: player win    1: dealer win    2: draw    


def draw_card(hand, card):
	hand.append(card.pop(0))
	if point(hand) > 21:
		return 1
	else:
		return 0


def game(card):
	dealer_hand = []
	player_hand = []
	first_card(dealer_hand, player_hand, card)
	print('dealer hand = ', dealer_hand, 'score = ', point(dealer_hand))
	print('player hand = ', player_hand, 'score = ', point(player_hand))
	while True:
		if point(dealer_hand) < 17:
			print("dealer_point = ", point(dealer_hand))
			print("dealer draw")
			bust = draw_card(dealer_hand, card)
			print(dealer_hand, "dealer point = ", point(dealer_hand))
			if bust == 1:
				print("dealer bust, player win")
				break
		else:
			print("dealer > 16")
		choice = raw_input("need more card? yes or no\n")
		if choice == "yes":
			print("draw card")
			bust = draw_card(player_hand, card)
			print("player_hand = ")
			print(player_hand)
			print(point(player_hand))
			if bust == 1:
				print("player bust, dealer win")
				break
		elif choice == "no":
			if judge(point(dealer_hand), point(player_hand)) == 1:
				print("dealer win")
				break
			elif judge(point(dealer_hand), point(player_hand)) == 2:
				print("draw")
				break
			elif judge(point(dealer_hand), point(player_hand)) == 0:
				if point(dealer_hand) > 16:
					print("player win")
					break

random.shuffle(card)


game(card)
while True:
	new_game = raw_input("restart game? yes or no \n")
	if new_game == "yes":
		game(card)
	else:
		break

