import collections

# Card = collections.namedtuple('Card', ['rank', 'suit'])

class Card:
    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit
    def __repr__(self):
        return self.suit+' '+self.rank

class Deck:
    # class property
    ranks=[str(i) for i in range(2,11)] + list('JQKA')
    suits='spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    def __repr__(self):
        return '\n'.join([str(card) for card in self._cards])
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, index): # iterable -> enables: in, slice [::], reversed()
        return self._cards[index]
    def __call__(self,index):
        return self[index]
    # def __setitem__(self,key,value): pass -> deck['D2'] = Card('Diamond','2')
    # def __getitem__(self,key): pass -> print(deck['D2'])
    # def __delitem__(self,key): pass -> del deck['D2']
    # def __iter__(self): pass -> 


deck=Deck()
print('--------Full deck:\n',deck) # __str__
print('--------Deck size:\n',len(deck)) # __len__
print('--------Deck[9]:\n',deck[9]) # __getitem__
print('--------Deck(9):\n',deck(9)) # __call__
print('--------ReveredDeck:\n',[str(i) for i in reversed(deck)]) # __getitem__, __len__
