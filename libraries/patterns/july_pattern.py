"""
July pattern for CircuitPython NeoPixel control
Provides patriotic patterns with red, white, and blue colors
"""

from .base_pattern import BasePattern

class JulyPattern(BasePattern):
    """July pattern with patriotic colors"""
    
    def __init__(self, pixels, num_pixels):
        super().__init__(pixels, num_pixels)
        
    def start(self):
        """
        Start the july pattern - this method is kept for compatibility
        but the actual pattern execution is now handled by the main loop
        """
        # This method is no longer used in the new step-based approach
        # The pattern logic is now in the main loop's run_july_pattern_step function
        pass 