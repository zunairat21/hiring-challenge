import time
from src.logger import log_step

class ActionExecutor:
    """
    Simulates user actions like clicking, typing nd long press.
    Later, this will be replaced by real device automation using ADB or Appium
    """
    def __init__(self, device=None):
        self.device = device #placeholder for real device controller 
    
    def click(self, job_id, selector):
        """ Simulate a click action """
        log_step(job_id, f"click:{selector}", True, f"Simulated click on '{selector}'")
        time.sleep(0.5)
    def type_text(self, job_id, selector, text):
        """Simulate typing text into an input field"""
        log_step(job_id, f"type:{selector}", True, f"Simulated typing '{text}' into '{selector}'")
        time.sleep(0.5)
    def long_press(self, job_id, selector, duration=3):
        """Simulate a long press gesture."""
        log_step(job_id, f"long_press:{selector}", True, f"Simulated long press on '{selector}' for {duration}s")
        time.sleep(duration)
    def run_action(self, job_id, action):
        """ 
        Execute an action dictionary in the format:
        {
        "type" : "click" | "type_text" | "long_press",
        "selector" : "element_name",
        "text" : "optional"
        }
        """

        action_type = action.get("type")
        selector = action.get("selector")
        text = action.get("text", "")

        if action_type == "click":
            self.click(job_id, selector)
        elif action_type == "type_text":
            self.type_text(job_id, selector, text)
        elif action_type == "long_press":
            self.long_press(job_id, selector)
        else:
            log_step(job_id, f"unknown: {action_type} ",False, f"unknown_action_type:'{action_type}'" )