"""
06. 集合Permalink
“paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""

from ch01_05 import letter_n_gram as lng

x = 'paraparaparadise'
y = 'paragraph'

X = set(lng(2, x))
Y = set(lng(2, y))

print('X: ', X)
print('Y: ', Y)
print()

print('----- X | Y -----')
print('union:       ', X | Y)
print()

print('----- X & Y -----')
print('intersection:', X & Y)
print()

print('----- X - Y -----')
print('difference:  ', X - Y)
print()

print('----- Y - X -----')
print('difference:  ', Y - X)
print()

print('----- "se" <= X -----')
print('subset:      ', {'se'} <= X)
print()

print('----- "se" <= Y -----')
print('subset:      ', {'se'} <= Y)
print()

print('----- "se" <= X & "se" <= Y -----')
print('subset:      ', ({'se'} <= X) & ({'se'} <= Y))
print()
