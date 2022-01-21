import enum


class Agent:
    def __init__(self) -> None:
        seq = [] # An action sequence = list of previous actions.
        state = [] # Description of the perceived world state.
        goal = None # The goal of the agent
        problem = None # Problem formulation
        actions = [Actions.left, Actions.right, Actions.suck] # List of actions available to the agent.
    
    def get_action(self, percept: object) -> object:
        pass
    
    def searchAction(self, state: object, action: object) -> object:
        pass
    def formulateGoal(self, state: object) -> object:
        # Given a state, formulate a goal.
        return None
    def formulateProblem(self, state: object, goal: object) -> object:
        # Given a state and a goal, formulate a problem.
        return None
    def updateState(self, state: object, percept: object) -> object:
        # Given a state and an action, update the state.
        return None

class Actions(enum.Enum):
    def __init__(self) -> None:
        self.left = 0
        self.right = 1
        self.suck = 2