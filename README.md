# Analyzing Monty Python

This is a quick project to display that if the announcer wouldn't know behind which car is the door (and thus adding the possibility of you losing before getting to the moment you'd choose if you keep or change doors), you'd have 50-50 chances at winning compared to the 66-33 chances of the real game (where he knows where the car is).

## Output for the real game

```
22:43 - grasseh@Grasseh-UMate:~/projects/py/monty  (master)  python montyreal.py 
Amount of situations where the game ended and the player won the car by keeping his door : 
3305
Total amount of games which made it to the end without revealing the car : 
10000
Total amount of games : 
10000
Percent of games that made it to the end that the player won by keeping his door : 
33.05

```

## Output where the first door opened could be a car

```
22:46 - grasseh@Grasseh-UMate:~/projects/py/monty  (master)  python monty.py 
Amount of situations where the game ended and the player won the car by keeping his door : 
3272
Total amount of games which made it to the end without revealing the car : 
6637
Total amount of games : 
10000
Percent of games that made it to the end that the player won by keeping his door : 
49.299382251
```
