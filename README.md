# Array_Application_Programming
A tiny programming project mimicking Lotto’s award checking system. 
To play the game, each player is assigned an ID number (1 <= ID number <= n), and could choose 6 distinct integer numbers from a barrel of 45 integer numbers (i.e., between 1 and 45, inclusive) as his /her gamenumbers. 
All players’ game-numbers are stored in a tiny “database” which, in this case, is replaced by an array (or list) lotto[0…n-1][0…5]. That is, for each player with ID number i, his/her game-numbers are stored in lotto[i-1][0…5]. 

Function 1 calculates the total number of winners for each class *, therefore generates a statistic table
* Notes: 
  * A 1st class winner is one whose game-numbers match all 6 winning numbers;  
  * A 2nd class winner is one whose game-numbers match any 5 winning numbers; 
  * A 3rd class winner is one whose game-numbers match any 4 winning numbers; 
  * A 4th class winner is one whose game-numbers match any 3 winning numbers. 
  
Function 2 has an interface where a player can check his/her winning status (i.e., whether or not he/she is a lotto winner, of any class): When the player inputs his ID number, say, k (1 <= k <= n), this function checks whether or not the player wins the lotto, and print the following:                     
   * <Player’s ID: k>, <Game-numbers in sequence in lotto[k-1][ ]> <Message>
  
  where <Message> is as below:   
  If the player’s game-numbers (stored in lotto[k-1][0…5]) match 
  * (a) all 6 winning numbers, <Message> is “You win the game, congratulations!” 
  * (b) any 5 winning numbers, <Message > is “You are a 2nd class winner, congratulations!” 
  * (c) any 4 winning numbers, <Message > is  “You are a 3rd class winner, congratulations!” 
  * (d) any 3 winning numbers, <Message > is  “You are a 4th class winner, congratulations!” 
  * (e) less than 3 winning numbers, <Message> is  “Thanks for playing lotto. Good luck next time!” 
