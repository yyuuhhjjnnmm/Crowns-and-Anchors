This project simulates a simplified version of the game that is a mix between "Crown and Anchor" and "Roulette". 

The game consists of a wheel that is spun, landing on a winning slot. 
Each slot will have three symbols from the set {hearts, spades, diamonds, clubs, crowns and anchors}. 
Each player has the chance to bet on none, one or more of the symbols.

The payout of the game is their initial bet plus their initial bet multiplied by the number of times the symbol occurs.

Example: 
Player bets $1 on hearts Hearts does not appear: player loses $1 initial bet 
Hearts appears once: player get back $1 initial bet, plus $1 * 1 = $2 
Hearts appears twice: player gets back $1 initial bet, plus $1 * 2 = $2 
Hearts appears thrice: player gets back $1 initial bet, plus $1 * 3 = $3

Players can bet in increments of $1, $2, $5 or $10. 
Players can skip the betting phase and sit out a round. 
Players can bet on multiple symbols provided they have sufficient amount of money. 
Players begin with $10.

Each round starts with betting of each player. 
Then after the wheel is spun, simulated by a random generation of numbers, and a winning slot is presented. 
Next the payout of each player is printed. 
Finally, the result of the round is printed to the screen and to the output file.

The game starts by asking for the number of players.
The game is looped while at least one player has money to bet.
