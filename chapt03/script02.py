"""
Method Factory Pattern
"""

# Imports

from abc import ABCMeta, abstractmethod


# Class

class Section(metaclass = ABCMeta):
    """
    Superclass
    """
    @abstractmethod
    def describe(self):
        pass

class PersonalSection(Section):
    """
    Subclass
    """
    def describe(self):
        print("Personal Section")

class AlbumSection(Section):
    """
    Subclass
    """
    def describe(self):
        print("Album Section")

class PatentSection(Section):
    """
    Subclass
    """
    def describe(self):
        print("Patent Section")

class PublicationSection(Section):
    """
    Subclass
    """
    def describe(self):
        print("Publication Section")

class Profile(metaclass = ABCMeta):
    """
    Superclass
    """
    def __init__(self):
        self.sections = []
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        pass

    def get_sections(self):
        return self.sections

    def add_sections(self, section):
        self.sections.append(section)

class Linkedin(Profile):
    """
    Subclass
    """
    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(PatentSection())
        self.add_sections(PublicationSection())

class Facebook(Profile):
    """
    Subclass
    """
    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(AlbumSection())


# Main

if __name__ == '__main__':
    profile_type = input("Which Profile you'd like to create? [LinkedIn or Facebook]")

    profile = eval(profile_type.title())()
    print("Creating Profile..", type(profile).__name__)
    print("Profile has sections --", profile.get_sections())
