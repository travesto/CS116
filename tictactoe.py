def listprinter(tictactoe):
   if type(tictactoe).__name__ != 'list':
       print('You should be using a list!')
       return False
   for element in tictactoe:
       if type(element).__name__ != 'list':
           print('You should be using a list!')
           return False
       for character in element:
           print(character,end=" ")
print()  
       
print('This program formats tic-tac-toe boards.')
tic = input('Enter the board: ')
tac = []
tac = list(tic)
toe = []

toe.append(tac[0:3])
toe.append(tac[3:6])
toe.append(tac[6:])

listprinter(toe)
