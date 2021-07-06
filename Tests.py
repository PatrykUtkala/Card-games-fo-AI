import unittest
import Games
import Cards


class Tester(unittest.TestCase):
    def test_Makao_Creation(self):
        makao = Games.Makao([1, 2, 3, 4], None, 0)
        self.assertEqual(len(makao.hands), 4, "Number of hand piles is not equal to number of players")
        for hand in makao.hands:
            self.assertEqual(len(hand), 5, "player starts with wrong number of cards")
        self.assertEqual(len(makao.pile), 1)
        print(makao.pile[0].type + " at top of the pile")
        self.assertIn(makao.pile[0].type, Cards.cards_normal + Cards.jokers)
        self.assertNotIn(makao.pile[0].type, ["2", "3", "4", "Jack", "Queen", "King", "Ace", "Joker"],
                         "wrong card at the top")

    def test_deck_functions(self):
        D = Cards.Deck()
        card = D.deck_list[-1]
        self.assertIn(card, D.deck_list)
        card = D.take_from_top()
        self.assertNotIn(card, D.deck_list)

        D.put_at_bottom(card)
        self.assertEqual(card, D.deck_list[0])
        D.put_at_top(card)
        # m = "card to put " + card.type + card.suit + ",card in deck " + D.deck_list[-1].type + D.deck_list[-1].suit
        # print(m)
        self.assertEqual(card, D.deck_list[-1])
        setD = set(D.deck_list)
        self.assertNotEqual(len(setD), len(D.deck_list))


if __name__ == '__main__':
    unittest.main()
