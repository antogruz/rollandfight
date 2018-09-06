class SurviveOrWin():
    def get(self, difficulty):
        return "SurviveOrWin " + str(difficulty)

class MultipleWays():
    def __init__(self, extraWays):
        self.ways = 1 + extraWays
    def get(self, difficulty):
        return str(self.ways) + " Ways " + str(difficulty)
