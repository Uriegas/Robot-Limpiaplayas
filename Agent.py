import enum

# The agent recevies the environment which is a list where 1 means dirty and 0 means clean
# The agent receives the position of the agent in the environment
class Agent:
    def __init__(self, position) -> None:
        self.state = [] # Description of the perceived world state. In which box is the agent. [0, 1, 2]
        self.goal = [0, 0, 0] # Goal of the agent: all rooms clen
        self.position = position # Position of the robot in the rooms
        # self.path_cost = 1 # Cost of moving to a new state
    
    def get_action(self, environment: list, position = int) -> object:
        """
        The agent perceives the environment which is a list
        of 3 elements where 1 means dirty and 0 means clean
        :param percept: The environment perceived by the agent
        :return: sequence of actions to clean the room
        """
        self.state = environment # Update state
        self.position = position # Update position
        seq = self.find_path(environment, self.goal) # Find path to goal
        return seq
    
    def find_path(self, state, goal):
        """
        Finds the path to the goal state
        :param state: The current state of the agent
        :param goal: The goal state
        :return: sequence of actions to clean the room
        """
        seq = [] # Sequence of actions to clean the room
        while state != goal:
            if state[self.position] == 1: # If the agent is in a dirty room
                seq.append(Actions.suck)
                state[self.position] = 0 # Clean the room
            elif state[self.position] == 0: # If the agent is in a clean room
                if self.position == 0:
                    seq.append(Actions.right)
                    self.position += 1
                elif self.position == 1:
                    if state[0] == 1:
                        seq.append(Actions.left)
                        self.position -= 1
                    else:
                        seq.append(Actions.right)
                        self.position += 1
                elif self.position == 2:
                    seq.append(Actions.left)
                    self.position -= 1
        return seq
    
    def apply_path(self, path):
        """
        Applies the path to the environment
        :param path: The path to be applied
        :return: None
        """
        for action in path:
            self.perform_action(action)
    
    def perform_action(self, action):
        """
        Performs the action on the environment
        :param action: The action to be performed
        :return: None
        """
        if action == Actions.left:
            self.position -= 1
        elif action == Actions.right:
            self.position += 1
        elif action == Actions.suck:
            self.state[self.position] = 0

class Actions(enum.Enum):
    left = 0
    right = 1
    suck = 2
