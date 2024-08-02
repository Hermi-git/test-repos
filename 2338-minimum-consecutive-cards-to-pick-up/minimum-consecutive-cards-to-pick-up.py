class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        card_dict = {}
        min_cards = float('inf')
        for i in range(len(cards)):
            if cards[i] in card_dict:
                cur_cards = i - card_dict[cards[i]] +1
                min_cards = min(min_cards, cur_cards)
            card_dict[cards[i]] = i
        return min_cards if min_cards != float('inf') else -1

       
            


        