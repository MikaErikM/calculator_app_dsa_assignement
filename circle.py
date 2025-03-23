import math

class Circle:
    """
    A class representing a circle.
    
    Attributes:
        radius (float): The radius of the circle.
    """
    
    def __init__(self, radius):
        """
        Initialize a Circle object with a given radius.
        
        Parameters:
            radius (float): The radius of the circle.
            
        Raises:
            ValueError: If the radius is not a positive number.
        """
        if radius <= 0:
            raise ValueError("Radius must be a positive number")
        
        self.radius = radius
    
    def area(self):
        """
        Calculate the area of the circle.
        
        Returns:
            float: The area of the circle (π × r²).
        """
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.
        
        Returns:
            float: The perimeter of the circle (2π × r).
        """
        return 2 * math.pi * self.radius