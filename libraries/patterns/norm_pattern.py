"""
Normal pattern for CircuitPython NeoPixel control
Provides standard patterns with various colors
"""

from .base_pattern import BasePattern

class NormPattern(BasePattern):
    """Normal pattern with standard colors"""
    
    def __init__(self, pixels, num_pixels):
        super().__init__(pixels, num_pixels)
        
    def start(self):
        """
        Start the normal pattern - this method is kept for compatibility
        but the actual pattern execution is now handled by the main loop
        """
        # This method is no longer used in the new step-based approach
        # The pattern logic is now in the main loop's run_normal_pattern_step function
        pass 