class Character:
    def __init__(self):
        self.position = 0
        self.jump_count = 0
        self.state = 'Idle'

    def move_left(self):
        self.position -= 1
        self.state = 'Moving Left'
        print(f'Character moved left. Current position: {self.position}')

    def move_right(self):
        self.position += 1
        self.state = 'Moving Right'
        print(f'Character moved right. Current position: {self.position}')

    def jump(self):
        if self.jump_count < 2:
            self.position += 2
            self.jump_count += 1
            self.state = 'Jumping'
            print(f'Character jumped. Current position: {self.position}. Jump count: {self.jump_count}')
        else:
            print('Character cannot jump more than twice in a row.')

    def reset_jump(self):
        self.jump_count = 0
        print('Jump count reset.')

    def get_state(self):
        return self.state

# Test the class
character = Character()
print(character.get_state())  # Output: Idle
character.move_right()  # Output: Character moved right. Current position: 1
character.move_right()  # Output: Character moved right. Current position: 2
character.jump()  # Output: Character jumped. Current position: 4. Jump count: 1
character.jump()  # Output: Character jumped. Current position: 6. Jump count: 2
character.jump()  # Output: Character cannot jump more than twice in a row.
character.reset_jump()  # Output: Jump count reset.
character.jump()  # Output: Character jumped. Current position: 8. Jump count: 1
character.move_left()  # Output: Character moved left. Current position: 7
print(character.get_state())  # Output: Moving Left