import random

class Colors():
    def __init__(self):
        self.colors = ["blue", "white", "red", "green", "yellow", "black"]
        self.count = 0
        random.shuffle(self.colors)

    def get(self):
        color = self.colors[self.count]
        self.count = (self.count + 1) % len(self.colors)
        if self.count == 0:
            random.shuffle(self.colors)

        return color

g_colors = Colors()

class SurviveOrWin():
    def get(self, difficulty):
        n = self.roll_colors_count()
        colors = [ g_colors.get() for i in range(n) ]
        return self.display(colors, self.pick_easy(difficulty, n), self.pick_hard(difficulty, n))

    def roll_colors_count(self):
        draw = random.randint(1, 6)
        if draw <= 3 :
            return 2
        if draw <= 5 :
            return 3
        return 1

    def pick_easy(self, d, colors_count):
        return int(max(1, (colors_count * d) / 6))

    def pick_hard(self, d, colors_count):
        return int((3 * colors_count * d) / 12)

    def display(self, colors, easy, hard):
        s = ""
        for c in colors:
            s += c + " "
        s += str(easy) + " - " + str(hard)
        return s


class MultipleWays():
    def __init__(self, extraWays):
        self.ways = 1 + extraWays
    def get(self, difficulty):
        return str(self.ways) + " Ways " + str(difficulty)






