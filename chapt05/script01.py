"""
Proxy Pattern
"""

# Classes

class Actor(object):
    """
    Object
    """
    def __init__(self):
        self.is_busy = True

    def occupied(self):
        """
        Sets the busy state.
        """
        self.is_busy = True
        print(type(self).__name__, "is occupied with current movie.")

    def available(self):
        """
        Sets the available state.
        """
        self.is_busy = False
        print(type(self).__name__, "is free for the movie.")

    def get_status(self):
        """
        Return the state.
        """
        return self.is_busy

class Agent(object):
    """
    The Proxy Class
    """
    def __init__(self):
        self.actor = None

    def work(self):
        """
        Checks the state of the actor.
        """
        self.actor = Actor()

        if self.actor.get_status():
            self.actor.occupied()
        else:
            self.actor.available()

# Main

if __name__ == "__main__":
    r = Agent()
    r.work()
