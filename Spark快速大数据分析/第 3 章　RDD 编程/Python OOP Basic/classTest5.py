class SelectedColor():

    allowedColor = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

    def __init__(self, color):
        if color in SelectedColor.allowedColor:
            self.color = color
            print("This color is initialized.")
        else:
            print("This color is not in a rainbow.")

red = SelectedColor("red")
black = SelectedColor("black")