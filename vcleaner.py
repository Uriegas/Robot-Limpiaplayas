from Agent import Agent
import argparse

def validate_rooms(room):
    """Validate room input is in [0, 1]"""
    room = int(room)
    if room not in [0, 1]:
        raise ValueError("Rooms must be 0 or 1")
    return room

# python vcleaner.py -r <rooms> -p <agent position>
#   -r <rooms> is a list of rooms, where 1 means dirty and 0 means clean, separated by commas.
#   -p <agent position> is the position of the agent in the list of rooms indexed from 0
# Example: python vcleaner.py -r 1, 0, 1 -p 2
parser = argparse.ArgumentParser(description='Vacuum Cleaner Example: python vcleaner.py -r "1, 0, 1" -p 2')
parser.add_argument('-r', '--rooms', metavar="room", type=validate_rooms, help='Rooms to clean, 0 means clean and 1 means dirty', nargs= 3, required=False, default=[1, 1, 1])
parser.add_argument('-p', '--position', type=int, help='Position of the agent in the list of rooms', required=False, default=0)
args = parser.parse_args()

agent = Agent(position=args.position)
seq = agent.get_action(args.rooms, args.position)
[ print(action) for action in seq ]
