class TreasureHunt:
    def __init__(self):
        self.current_stage = 0
        self.stages = [
            {
                "clue": "It's a protocol that powers the web. (Hint: Starts with 'H' and ends with 'P')",
                "answer": "HTTP"
            },
            {
                "clue": "It's a snake but also a popular programming language.",
                "answer": "PYTHON"
            },
            {
                "clue": "Which technology is used by Bitcoin and many cryptocurrencies?",
                "answer": "BLOCKCHAIN"
            },
            {
                "clue": "It's a gate which gives output true only when both its two inputs are false. (Hint: It's a 3-letter acronym)",
                "answer": "NOR"
            },
            {
                "clue": "An algorithmic problem to find the shortest path between nodes. (Hint: First name of a famous Dutch computer scientist)",
                "answer": "DIJKSTRA"
            }
        ]

    def start(self):
        print("Welcome to the Technical Treasure Hunt!")
        print("Solve the clues to proceed to the next stage.")
        
        while self.current_stage < len(self.stages):
            print("\nClue:", self.stages[self.current_stage]['clue'])
            answer = input("Your answer: ").upper()

            if answer == self.stages[self.current_stage]['answer']:
                print("Correct!")
                self.current_stage += 1
            else:
                print("Try again!")

        print("\nCongratulations! You've completed the treasure hunt!")

if __name__ == "__main__":
    hunt = TreasureHunt()
    hunt.start()