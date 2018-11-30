from state_machine import AbstractState, StateMachine
import math


class MenuState(AbstractState):
    def execute(self):
        print('Menu')
        print('1. Show squares')
        print('2. Show Pi')
        print('3. Sub menu')
        print('4. Quit')
        value = input('Enter your choice: ')
        if value == '1':
            self.next_state = SquareState()
        elif value == '2':
            self.next_state = PiState()
        elif value == '3':
            self.next_state = SubMenuState()
        elif value == '4':
            self.next_state = QuitState()
        else:
            print('Invalid input')
            self.next_state = MenuState()


class QuitState(AbstractState):
    def execute(self):
        print('Quitting')


class SquareState(AbstractState):
    def execute(self):
        print([x ** 2 for x in range(10)])
        input('Press enter...')
        self.next_state = MenuState()


class PiState(AbstractState):
    def execute(self):
        print(f'Value of pi: {math.pi}')
        input('Press enter...')
        self.next_state = MenuState()


class SubMenuState(AbstractState):
    def execute(self):
        print('1. Area of rectangle')
        print('2. Area of circle')
        print('3. Back to main menu')
        value = input('Enter your choice: ')
        if value == '1':
            self.next_state = RectangleState()
        elif value == '2':
            self.next_state = CircleState()
        elif value == '3':
            self.next_state = MenuState()
        else:
            print('Invalid input')
            self.next_state = SubMenuState()


class RectangleState(AbstractState):
    def execute(self):
        try:
            width = float(input('Enter width: '))
            height = float(input('Enter height: '))
            print(f'Area: {width*height}')
        except:
            print('Error')

        self.next_state = SubMenuState()


class CircleState(AbstractState):
    def execute(self):
        try:
            radius = float(input('Enter radius: '))
            print(f'{math.pi * r**2}')
        except:
            print('Error')

        self.next_state = SubMenuState()


if __name__ == '__main__':
    state_machine = StateMachine(MenuState())
    while state_machine.has_state():
        print('-' * 20)
        state_machine.execute()
        state_machine.transition()
