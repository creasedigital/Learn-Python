# from random import choice

class Card:
   
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
        # if s is not in suit:
        #     raise ValueError("invalid instance value")
        
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"




class Deck:
    # count = 52;
     
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "k"]

        self.cards = [Card(value, suit) for suit in suits for value in values]
        print(self.cards)
                
                
Deck()
    