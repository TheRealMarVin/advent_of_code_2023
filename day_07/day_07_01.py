import re

import numpy as np


def get_hand_and_bid(input_string):
    pattern = re.compile(r'\b\d+\b')
    hand = input_string[:5]
    number = ""
    for match in pattern.findall(input_string[5:]):
        number += match

    return hand, int(number)


def is_five_of_a_kind(hand):
    return len(set(hand)) == 1


def is_four_of_a_kind(hand):
    return any(hand.count(card) == 4 for card in set(hand))


def is_full_house(hand):
    counts = [hand.count(card) for card in set(hand)]
    return set(counts) == {2, 3}


def is_three_of_a_kind(hand):
    return any(hand.count(card) == 3 for card in set(hand))


def is_two_pair(hand):
    counts = [hand.count(card) for card in set(hand)]
    return counts.count(2) == 2 and counts.count(1) == 1


def is_one_pair(hand):
    counts = [hand.count(card) for card in set(hand)]
    return counts.count(2) == 1 and counts.count(1) == 3


def is_high_card(hand):
    return len(set(hand)) == 5


def hands_sort(items):
    n = len(items)

    for i in range(n):
        for j in range(0, n-i-1):
            if compare_hands(items[j], items[j+1]) < 0:
                items[j], items[j+1] = items[j+1], items[j]

    items.reverse()
    return items


def compare_hands(hand1, hand2):
    card_list = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    card_to_value = {value: position for position, value in enumerate(card_list)}

    cards1, _ = hand1
    cards2, _ = hand2

    for card1, card2 in zip(cards1, cards2):
        if card_to_value[card2] > card_to_value[card1]:
            return 1
        elif card_to_value[card2] < card_to_value[card1]:
            return -1

    return 0  # Hands are equal


def main():
    # Read input data from a file
    with open('data.txt', 'r') as file:
        input_data = file.readlines()

    hands = [get_hand_and_bid(curr) for curr in input_data]

    hand_order = ["Five of a Kind", "Four of a Kind", "Full House", "Three of a Kind", "Two Pair", "One Pair",
                  "High Card"]
    hands_in_group = {k: [] for k in hand_order}
    for i, hand in enumerate(hands):
        card, _ = hand
        if is_five_of_a_kind(card):
            hands_in_group[hand_order[0]].append(hand)
        elif is_four_of_a_kind(card):
            hands_in_group[hand_order[1]].append(hand)
        elif is_full_house(card):
            hands_in_group[hand_order[2]].append(hand)
        elif is_three_of_a_kind(card):
            hands_in_group[hand_order[3]].append(hand)
        elif is_two_pair(card):
            hands_in_group[hand_order[4]].append(hand)
        elif is_one_pair(card):
            hands_in_group[hand_order[5]].append(hand)
        elif is_high_card(card):
            hands_in_group[hand_order[6]].append(hand)
        else:
            raise Exception("Error")

    for k, v in hands_in_group.items():
        hands_in_group[k] = hands_sort(v)

    rank = 1
    hand_order.reverse()

    res = []
    for hand in hand_order:
        for curr in hands_in_group[hand]:
            _, value = curr
            res.append(value * rank)
            rank += 1

    res = np.array(res).sum()
    print(res)


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
