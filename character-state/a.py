class Character:
    def __init__(self):
        self.position = 0
        self.jump_count = 0
        self.state = "Idle"

    def move_left(self):
        self.position -= 1
        self.state = "Moving Left"
        print(f"Character moved left. Current position: {self.position}")

    def move_right(self):
        self.position += 1
        self.state = "Moving Right"
        print(f"Character moved right. Current position: {self.position}")

    def jump(self):
        if self.jump_count < 2:
            self.position += 2
            self.jump_count += 1
            self.state = "Jumping"
            print(f"Character jumped. Current position: {self.position}. Jump count: {self.jump_count}")
        else:
            print("Character cannot jump more than twice.")

    def reset_jump_count(self):
        self.jump_count = 0
        print("Jump count reset.")

    def get_state(self):
        return self.state

# Testing the class
character = Character()
print(character.get_state())
character.move_right()
character.move_right()
character.jump()
character.jump()
character.jump()
character.reset_jump_count()
character.jump()