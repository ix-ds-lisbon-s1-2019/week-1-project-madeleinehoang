# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:54:29 2019

@author: student
"""

#%%

import random

def game( number_of_players ):
    names =[input( "Please enter your name: ") for i in range( number_of_players ) ]
    cards = [ "A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2" ] * 4
    values = {"2": 2, 
              "3": 3, 
              "4": 4, 
              "5": 5, 
              "6": 6, 
              "7": 7, 
              "8": 8, 
              "9": 9, 
              "10": 10, 
              "J": 11,
              "Q": 12,
              "K": 13,
              "A": 14}
    
    hand = {}
    ordered_hand = {}
    
    for name in names:
        hand[ name ] = []
        ordered_hand[ name ] = []
        for i in range ( 0, 5 ):
            choice = random.choice( cards )
            hand[ name ] += [ choice ]
            
            value = values.get( choice )
            ordered_hand[ name ] += [ value ]
            cards.remove( choice )
            
        print("{}'s hand is {}, {}, {}, {}, {}.".format(
                name,
                hand[name][0],
                hand[name][1],
                hand[name][2],
                hand[name][3],
                hand[name][4]))
            
        ordered_hand[name].sort( reverse = True ) 

    compare = {}
    for name, value in ordered_hand.items():
        if not compare:
            compare[name] = value
            continue
        for i in range( 0, 5 ):
            if value[ i ] == list( compare.values() )[ 0 ][ i ]:
                continue
            elif value[ i ] > list( compare.values() )[ 0 ][ i ]:
                compare = { name: value }
                break
            break
    
    result = "The winner is {}.".format( list( compare.keys()) [ 0 ] )

    return result

game( 8 )