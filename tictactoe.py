"""
tic tac toe
"""
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
       
blerg = []

print("This program formats tic-tac-toe boards.")
board = input("Enter the board: ")
blerg.append([board[:3]])
blerg.append([board[3:6]])
blerg.append([board[6:9]])
        
print(blerg)
listprinter(blerg)

