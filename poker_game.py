# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:54:29 2019

@author: student
"""

def poker( number_of_players ):
    
    import random
    
    number_choices = [ "A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2" ]
    suit_choices = [ "clubs" ,"spades", "hearts", "diamonds" ]
    
    number_of_players = int( number_of_players )
    
    cards = []
    for i in range( 0, number_of_players ):
        hand = ""
        
        for j in range( 0, 5 ):
            number = random.choice( number_choices )
            suit = random.choice( suit_choices )
            card = number + " " + suit
            hand = hand + card + " "
        
        cards.append( hand )
    
    print( cards )
            
    
    #%%%
    
    import random

    def poker( number_of_players ):
        number_choices = [ "A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2" ]
        suit_choices = [ "clubs" ,"spades", "hearts", "diamonds" ]
        
        cards_all = []
        
        for i in range ( 0, number_of_players ):
            hand = ""
            nbr = []
            
            for j in range( 0, 5 ):
                number = random.choice( number_choices )
                nbr.append( number )
                suit = random.choice( suit_choices )
                card = number + " " + suit
                
                duplicate = True
                while duplicate:
                    if card in hand:
                        number = random.choice( number_choices )
                        suit = random.choice( suit_choices )
                        card = number + " " + suit
                    
                    else:
                        duplicate = False
                
                hand = hand + card + " "
                
            print( hand )
        
            cards_all.append( hand ) 
        
        string_cards_all = ", ".join( cards_all )
        
        

        

poker( 3 )
    
    

#%%

class Poker:
    import random
    
    def init( self, number_of_players ):
        self.players = number_of_players
        self.names = names = [input( "Please enter your name: ") for i in range( self.players ) ]
        self.cards = [ "A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2" ] * 4

    
    def name( self ):
        names = [input( "Please enter your name: ") for i in range( self.players ) ]

    
    def cards( self ):
        number_choices = [ "A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2" ]
        suit_choices = [ "clubs" ,"spades", "hearts", "diamonds" ]
        
        cards_all = ""
        
        for i in range ( 0, players ):
            hand = ""
            nbr = []
            
            for j in range( 0, 5 ):
                number = random.choice( number_choices )
                nbr.append( number )
                suit = random.choice( suit_choices )
                card = number + " " + suit
                
                duplicate = True
                while duplicate:
                    if card in hand:
                        number = random.choice( number_choices )
                        suit = random.choice( suit_choices )
                        card = number + " " + suit
                    
                    else:
                        duplicate = False
                
                hand = hand + card + " "
                
            print( hand )
        
            cards_all.append( hand ) 
    
    def winner( self ):
        to_compare = {"2":2, 
                      "3":3, 
                      "4":4, 
                      "5":5, 
                      "6":6, 
                      "7":7, 
                      "8": 8, 
                      "9":9, 
                      "10":10, 
                      "J":11,
                      "Q":12,
                      "K":13,
                      "A":14}
        
        


game = Poker(number_of_players=3)
game.cards()
        
for x in names:
    dict[ x ] = []
    for i in range( 5 ):
        choice = random.choice( cards )
        values = values.get( choice )
        dict[ x ] += [ values ]
        cards.remove( choice )
    dict[ x ].sort( reverse = True )
    

#%%
    
import random

def game( number_of_players ):
    names =[input( "Please enter your name: ") for i in range( number_of_players ) ]
    cards = [ "A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2" ] * 4
    dict = {}
    values = {"2":2, 
              "3":3, 
              "4":4, 
              "5":5, 
              "6":6, 
              "7":7, 
              "8":8, 
              "9":9, 
              "10":10, 
              "J":11,
              "Q":12,
              "K":13,
              "A":14}
    
    for x in names:
        dict[ x ] = []
        for i in range( 0, 5 ):
            choice = random.choice( cards )
            value = values.get( choice )
            dict[ x ] += [ value ]
            cards.remove( choice )
        dict[ x ].sort( reverse = True )
    
    print( dict )
    for key, value in dict.items():
        print(key)
        print(value)
    
    hand = []
    for y in range( 0, number_of_players ):
        y = dict[ names[ y ] ]
        hand.append( y )
    
   
            
    

    
print(game(3))
    
    #%%
    
    max_list = []
    
    for hand in player_values:
        maximum_ind = max( hand )
        max_list.append( maximum_ind )
    
    maximum = max( max_list )    
    index_max = max_list.index( maximum )
    
    nbr_occurances = max_list.count( maximum )
    
    if nbr_occurances == 1:
        winner = names[ index_max ]
    else:
        pass
            
    
    

#%%

game( 3 )


#%%

