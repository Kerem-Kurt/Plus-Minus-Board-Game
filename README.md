# Plus-Minus-Board-Game

<h3>This is an experimental game where the user solves the puzzle they created.</h3>

<h4>-Main idea of the game is turning the board to its initial position (only "-" signs on the board) after the user has added some "+" signs.</h4>

<br>
Game is played in four stages:<br>
1- The user selects the size of the board (one int value), and an all "-" board is created accordingly.<br>
2- The user selects how many squares they want to turn to "+". <br>
3- The user chooses which boxes in the board are going to be + by their x and y axis positions. <br>
!! The game starts now !!<br>
4- The user selects boxes one by one, and in each selection; the left upper, the right upper, the box itself, the left lower, and the right lower box changes sign if possible.<br>
 - Game continues untill the board turn to its initial position (all "-" signs).

- An example of a size of 5 board is:<br>
&nbsp; 1 2 3 4 5<br>
1 - - - - -<br>
2 - - - - -<br>
3 - - - - -<br>
4 - - - - -<br>
5 - - - - -<br>

- After the inputs of : <br> 2 5 &nbsp;&nbsp; 4 3 &nbsp; &nbsp; 2 3 &nbsp;&nbsp; 2 4 &nbsp; &nbsp; 3 4 &nbsp;&nbsp; 4 5
<br><br>

- The table is turned into: <br>
&nbsp;  1 2 3 4 5 <br>
1 - - - - - <br>
2 - - + + + <br>
3 - - - + - <br>
4 - - + - + <br>
5 - - - - - <br>

- In final phase, if the user chooses 5 2: <br>
&nbsp;  1 2 3 4 5 <br>
1 - - - - - <br>
2 - - + + + <br>
3 - - - + - <br>
4 + - - - + <br>
5 - + - - - <br>

- As you can see 4 3 changed from "+" to "-", by choosing coordinates to change the values untill no "+" sign remains.<br>
 ex. if the user then selects 5 2 and 3 4 the board turns back into<br>
 &nbsp; 1 2 3 4 5<br>
1 - - - - -<br>
2 - - - - -<br>
3 - - - - -<br>
4 - - - - -<br>
5 - - - - -<br>
<br>
- Finally the prompt of "Congratulations, you won!" is shown and the game is over.
