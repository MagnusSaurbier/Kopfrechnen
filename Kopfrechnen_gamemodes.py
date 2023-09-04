import random
import math

# ==================== Gamemodes ====================
# How to add a new gamemode?
# 1. Create class, inherit from Gamemode or subclass e.g. Multiplication
# 2. Set title
# 3. Implement makeTask() method: return String: task, int: result
# 4. Add class to gamemodes list

# How to add a new category?
# 1. Create class, inherit from Gamemode
# 2. Set category-title
# 3. Add category as dictionary-item to gamemodes list just like "Multiplication"

class Gamemode:
    category = "Gamemode"
    title = "Gamemode"
    def makeTask():
        return "task", 0 # task, result

# ==================== Multiplication ====================

class Multiplication(Gamemode):
    category = "Multiplication"
    title = "Multiplication"
    def makeTask():
        return "calculation exercise", 0 # task, result
    
class TwoDigitSquares(Multiplication):
    title = "2-digit squares"
    def makeTask():
        a = random.randint(10, 99)
        return str(a) + "²", a**2 # task, result
    
class TwoDigitSquaresWith5(Multiplication):
    title = "2-digit squares with 5"
    def makeTask():
        a = 10 * random.randint(1, 9) + 5
        return str(a) + "²", a**2 # task, result
    
class TwoDigitMultiply11(Multiplication):
    title = "2-digit multiply 11"
    def makeTask():
        a = random.randint(10, 99)
        return str(a) + " * 11", a*11 # task, result
    
class TwoDigitMultiply(Multiplication):
    title = "2-digit multiply"
    def makeTask():
        a = random.randint(1, 99)
        b = random.randint(1, 99)
        return str(a) + " * " + str(b), a*b # task, result
    
class TwoDigitMultiplySameTen(Multiplication):
    title = "2-digit multiply same ten-digit"
    def makeTask():
        t = random.randint(1, 9)
        a = 10*t + random.randint(1, 9)
        b = 10*t + random.randint(1, 9)
        return str(a) + " * " + str(b), a*b # task, result
    
class ThreeDigitSquaresWith5(Multiplication):
    title = "3-digit squares with 5"
    def makeTask():
        a = 10 * random.randint(10, 99) + 5
        return str(a) + "²", a**2 # task, result
    
# ==================== Addition ====================

class Addition(Gamemode):
    category = "Addition"
    title = "Addition"
    def makeTask():
        return "calculation exercise", 0 # task, result
    
class TwoDigitAddition(Addition):
    title = "2-digit addition"
    def makeTask():
        a = random.randint(1, 99)
        b = random.randint(1, 99)
        return str(a) + " + " + str(b), a+b # task, result
    
class ThreeDigitAddition(Addition):
    title = "3-digit addition"
    def makeTask():
        a = random.randint(1, 999)
        b = random.randint(1, 999)
        return str(a) + " + " + str(b), a+b # task, result
    
class FourDigitAddition(Addition):
    title = "4-digit addition"
    def makeTask():
        a = random.randint(1, 9999)
        b = random.randint(1, 9999)
        return str(a) + " + " + str(b), a+b # task, result
    
class FiveDigitAddition(Addition):
    title = "5-digit addition"
    def makeTask():
        a = random.randint(1, 99999)
        b = random.randint(1, 99999)
        return str(a) + " + " + str(b), a+b # task, result
    
class RandomizedAddition(Addition):
    title = "Randomized addition"
    def makeTask():
        nNumbers = random.randint(2, 5)
        sizes = [random.randint(1, 5) for i in range(nNumbers)]
        numbers = [random.randint(10**(sizes[i]-1), 10**sizes[i]) for i in range(nNumbers)]
        return " + ".join([str(n) for n in numbers]), sum(numbers) # task, result
    
# ==================== Approximation ====================
class Approximation(Gamemode):
    category = "Approximation"
    title = "Approximation"
    def makeTask():
        return "calculation exercise", 0 # task, result
    
class ApproxMult(Approximation):
    title = "Approximate Multiplication"
    def makeTask():
        nNumbers = random.randint(2, 4)
        sizes = [random.randint(1, 3) for i in range(nNumbers)]
        numbers = [random.randint(10**(sizes[i]-1), 10**sizes[i]) for i in range(nNumbers)]
        p = math.prod(numbers)
        factor = random.random() + 0.5
        comparison = int(p*factor)
        if p <= comparison:
            return (" * ".join([str(n) for n in numbers])) + ">" + str(comparison)+"?", 0 # task, result
        else:
            return (" * ".join([str(n) for n in numbers])) + ">" + str(comparison)+"?", 1 # task, result
        
# ==================== Mixed ===========================

class Mixed(Gamemode):
    category = "Mixed"
    title = "Mixed"
    def randomCategory():
        categories = [c for c in gamemodes.keys() if c != "Mixed"]
        return random.choice(categories)
    def makeTask():
        category = Mixed.randomCategory()
        gamemode = random.choice(gamemodes[category])
        return gamemode.makeTask()

# ==================== Gamemodes list ====================

gamemodes = {
    "Multiplication": [
        TwoDigitSquares,
        TwoDigitSquaresWith5,
        TwoDigitMultiply11,
        TwoDigitMultiplySameTen,
        TwoDigitMultiply,
        ThreeDigitSquaresWith5,
    ],
    "Addition": [
        TwoDigitAddition,
        ThreeDigitAddition,
        FourDigitAddition,
        FiveDigitAddition,
        RandomizedAddition,
    ],
    "Mixed": [
        Mixed,
    ],
    "Approximation": [
        ApproxMult,
    ],
}