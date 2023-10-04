class Rectangle:
    def __init__(self,lenght,witdh,color):
        self.lenght = lenght
        self.width = witdh
        self.color = color
        
        
        
rect1 = Rectangle(5,3, "red")
rect2 = Rectangle(5,3,"blue") 
rect3 = Rectangle(4,6, color ="pink")

print("Le rectangle numéro 1 est de longueur",rect1.lenght,", de largeur", rect1.width,"et de couleur", rect1.color)
print("Le rectangle numéro 2 est de longueur",rect2.lenght,", de largeur", rect2.width,"et de couleur", rect2.color)
print("Le rectangle numéro 3 est de longueur",rect3.lenght,", de largeur", rect3.width,"et de couleur", rect3.color)