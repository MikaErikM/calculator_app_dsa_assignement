import unittest
import math
from circle import Circle

class TestCircle(unittest.TestCase):
    """Test case for the Circle class methods."""
    
    def test_initialization(self):
        """Test that Circle objects can be created with valid radius values."""
        # Create a circle with radius 5
        c = Circle(5)
        self.assertEqual(c.radius, 5)
        
        # Verify that invalid radius raises ValueError
        with self.assertRaises(ValueError):
            Circle(-1)
    
    def test_area(self):
        """Test the area calculation method."""
        # Test with a few different radius values
        test_cases = [
            (1, math.pi),           # Circle with radius 1: area = π
            (2, 4 * math.pi),       # Circle with radius 2: area = 4π
            (0.5, 0.25 * math.pi)   # Circle with radius 0.5: area = 0.25π
        ]
        
        for radius, expected_area in test_cases:
            with self.subTest(radius=radius):
                c = Circle(radius)
                self.assertAlmostEqual(c.area(), expected_area)
    
    def test_perimeter(self):
        """Test the perimeter calculation method."""
        # Test with a few different radius values
        test_cases = [
            (1, 2 * math.pi),      # Circle with radius 1: perimeter = 2π
            (2, 4 * math.pi),      # Circle with radius 2: perimeter = 4π
            (0.5, math.pi)         # Circle with radius 0.5: perimeter = π
        ]
        
        for radius, expected_perimeter in test_cases:
            with self.subTest(radius=radius):
                c = Circle(radius)
                self.assertAlmostEqual(c.perimeter(), expected_perimeter)

if __name__ == '__main__':
    unittest.main()