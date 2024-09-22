"""
Write a class called Rock_paper_scissors that implements the logic of the game Rockpaper-scissors. 
For this game the user plays against the computer for a certain number of rounds. 
Your class should have fields for the how many rounds there will be, 
the current round number, and the number of wins each player has. 
There should be methods for getting the computer’s choice, finding the winner of a round, 
and checking to see if someone has one the (entire) game. 
You may want more methods.
"""

import random


class Rock_paper_scissor:
    options = ["rock", "paper", "scissors"]

    def __init__(self, num_of_rounds: int) -> None:
        self.num_of_round = num_of_rounds
        self.current_round = 0
        self.record_of_wins = {"player1": 0, "player2": 0}
    
    def computer_play(self):
        return random.choice(self.options)
    
    def play_with_comp(self):
        while self.current_round < self.num_of_round:
            user = input(f"choose between {', '.join(self.options)}:\t")
            comp = self.computer_play()
            if user not in self.options:
                raise ValueError
            if user == comp:
                pass
            elif user == "rock" and comp == "paper":
                self.record_of_wins["player2"] += 1
            elif user == "paper" and comp == "rock":
                self.record_of_wins["player1"] += 1
            elif user == "scissors" and comp == "rock":
                self.record_of_wins["player2"] += 1
            elif user == "rock" and comp == "scissors":
                self.record_of_wins["player1"] += 1
            elif user == "paper" and comp == "scissors":
                self.record_of_wins["player2"] += 1
            elif user == "scissors" and comp == "paper":
                self.record_of_wins["player1"] += 1
            
            self.current_round += 1
        
        if self.current_round == self.num_of_round:
            print("Game ended")
            if self.record_of_wins["player1"] > self.record_of_wins["player2"]:
                print(f"player1 wins with {self.record_of_wins["player1"]} points")
            elif self.record_of_wins["player1"] < self.record_of_wins["player2"]:
                print(f"computer wins with {self.record_of_wins["player2"]} points")
            else:
                print(f"no winner\nplayer1 => {self.record_of_wins["player1"]} points; computer => {self.record_of_wins["player2"]} points")
        
# TEST usage
begin = Rock_paper_scissor(1)
begin.play_with_comp()