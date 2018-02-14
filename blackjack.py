import random


def first_card(dealer_hand, player_hand, card):
	dealer_hand.append(card.pop(0))
	dealer_hand.append(card.pop(0))
	player_hand.append(card.pop(0))
	player_hand.append(card.pop(0))

def point(hand):
	num = 0
	for i in hand:
		if i[1]!=1 & i[1]<10:
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
	

def judg(dealer_point,player_point):
	if dealer_point>21 & player_point>21:
		return 2
	elif delaer_point==21 & player_point>21:
		return 1
	else:
		if dealer_point<player_point:
			return 0
		elif dealer_point>player_point:
			return 1
		else:
			return 2
				


random.shuffle(card)
dealer_hand = []
player_hand = []
first_card(dealer_hand, player_hand, card)
print "dealer hand"
print(dealer_hand)
print(point(dealer_hand))
print "player hand"
print(player_hand)
print(point(player_hand))
