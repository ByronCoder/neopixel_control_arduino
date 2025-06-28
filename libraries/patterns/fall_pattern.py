"""
Fall pattern for CircuitPython NeoPixel control
Provides autumn-themed patterns with red, yellow, and orange colors
"""

from .base_pattern import BasePattern

class FallPattern(BasePattern):
    """Fall pattern with autumn colors"""
    
    def __init__(self, pixels, num_pixels):
        super().__init__(pixels, num_pixels)
        
    def start(self):
        """
        Start the fall pattern - this method is kept for compatibility
        but the actual pattern execution is now handled by the main loop
        """
        # This method is no longer used in the new step-based approach
        # The pattern logic is now in the main loop's run_fall_pattern_step function
        pass 