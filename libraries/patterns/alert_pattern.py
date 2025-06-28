"""
Alert pattern for CircuitPython NeoPixel control
Provides warning patterns with yellow colors
"""

from .base_pattern import BasePattern

class AlertPattern(BasePattern):
    """Alert pattern with warning colors"""
    
    def __init__(self, pixels, num_pixels):
        super().__init__(pixels, num_pixels)
        
    def start(self):
        """
        Start the alert pattern - this method is kept for compatibility
        but the actual pattern execution is now handled by the main loop
        """
        # This method is no longer used in the new step-based approach
        # The pattern logic is now in the main loop's run_alert_pattern_step function
        pass 