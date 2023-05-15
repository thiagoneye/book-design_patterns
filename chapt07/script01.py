"""
Command Pattern
"""

# Class

class Wizard():
    def __init__(self, src: str, root_dir: str) -> None:
        self.choices = []
        self.root_dir = root_dir
        self.src = src

    def preferences(self, command: dict) -> None:
        self.choices.append(command)

    def execute(self) -> None:
        for choice in self.choices:
            if list(choice.values())[0]:
                print("Copying binaries --", self.src, "to", self.root_dir)
            else:
                print("No Operation")


# Main

if __name__ == "__main__":
    wizard = Wizard("python3.5.gzip", "/usr/bin/")

    wizard.preferences({"Python": True})
    wizard.preferences({"Java": False})

    wizard.execute()
