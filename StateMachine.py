import pygame
import States.BaseState

class StateMachine():
    def __init__(self, states):
        if len(states) > 0:
            self.states = states
        else:
            states = {}

        self.empty = States.BaseState.BaseState()
        self.current = self.empty
    
    def change(self, state, params):
        self.current.exit()
        self.current = self.states[state]
        self.current.enter(params)
    
    def update(self):
        self.current.update()

    def render(self):
        self.current.render()