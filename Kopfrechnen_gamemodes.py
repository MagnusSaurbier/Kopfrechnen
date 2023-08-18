import random
class Gamemode:
    title = "Gamemode"
    def makeTask():
        return "calculation exercise", 0 # task, result
    
class TwoDigitSquares(Gamemode):
    title = "2-digit squares"
    def makeTask():
        a = random.randint(10, 99)
        return str(a) + "²", a**2 # task, result
    
class TwoDigitSquaresWith5(Gamemode):
    title = "2-digit squares with 5"
    def makeTask():
        a = 10 * random.randint(1, 9) + 5
        return str(a) + "²", a**2 # task, result
    
class TwoDigitMultiply11(Gamemode):
    title = "2-digit multiply 11"
    def makeTask():
        a = random.randint(10, 99)
        return str(a) + " * 11", a*11 # task, result
    
class TwoDigitMultiply(Gamemode):
    title = "2-digit multiply"
    def makeTask():
        a = random.randint(1, 99)
        b = random.randint(1, 99)
        return str(a) + " * " + str(b), a*b # task, result
    
class ThreeDigitSquaresWith5(Gamemode):
    title = "3-digit squares with 5"
    def makeTask():
        a = 10 * random.randint(10, 99) + 5
        return str(a) + "²", a**2 # task, result
    
gamemodes = [TwoDigitSquares,
             TwoDigitSquaresWith5,
             TwoDigitMultiply11,
             TwoDigitMultiply,
             ThreeDigitSquaresWith5,
            ]