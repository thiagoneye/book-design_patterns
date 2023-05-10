"""
Facade Patterns
"""

# Classes

class EventManager(object):
    """
    Facade Class
    """
    def __init__(self) -> None:
        print("Event Manager: Let me talk to the folks\n")
        self.hotelier = None
        self.florist = None
        self.caterer = None
        self.musician = None

    def arrange(self):
        """
        Function to organize the event.
        """
        self.hotelier = Hotelier()
        self.hotelier.book_hotel()

        self.florist = Florist()
        self.florist.set_flower_requirements()

        self.caterer = Caterer()
        self.caterer.set_cuisine()

        self.musician = Musician()
        self.musician.set_music_type()

class Hotelier(object):
    """
    Subsystem Class
    """
    def __init__(self) -> None:
        print("Arranging the Hotel for Marriage? --")

    def __is_available(self):
        print("Is the Hotel free for the event on given day?")
        return True

    def book_hotel(self):
        """
        Function to book the hotel.
        """
        if self.__is_available():
            print("Registered the Booking\n\n")

class Florist(object):
    """
    Subsystem Class
    """
    def __init__(self) -> None:
        print("Flower Decorations for the Event? --")

    def set_flower_requirements(self):
        """
        Function to define flower requirements.
        """
        print("Carnations, Roses and Lilies would be used for Decorations\n\n")

class Caterer(object):
    """
    Subsystem Class
    """
    def __init__(self) -> None:
        print("Food Arrangements for the Event --")

    def set_cuisine(self):
        """
        Function to define the cuisine.
        """
        print("Chinese & Continental Cuisine to be served\n\n")

class Musician(object):
    """
    Subsystem Class
    """
    def __init__(self) -> None:
        print("Musical Arrangements for the Marriage --")

    def set_music_type(self):
        """
        Function to define the music type.
        """
        print("Jazz and Classical will by played\n\n")

class You(object):
    """
    Client Class
    """
    def __init__(self) -> None:
        print("You: Whoa! Marriage Arrangements?!!!")

    def ask_event_manager(self):
        """
        Function to contact the event manager.
        """
        print("You: Let's Contact the Event Manager\n\n")

        event_manager = EventManager()
        event_manager.arrange()

    def __del__(self):
        print("You: Thanks to Event Manager, all preparations done! Phew!")


# Main

if __name__ == '__main__':
    you = You()
    you.ask_event_manager()
