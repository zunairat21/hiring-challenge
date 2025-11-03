import time
import os
from logger import log_step

class ActionExecutor:
    """
    Executes real user actions on Android device using ADB commands.
    Supports: click (tap), type_text, long_press.
    """
    def __init__(self, device=None):
        self.device = device #placeholder for real device controller 
    
    def click(self, job_id, selector):
        """ Simulate a real tap using ADB """
        try:
            # Selector may contain coordinates like '500 800'
            coords = selector.split()
            if len(coords) == 2:
                x, y = coords
                print(f"👆 Tapping at ({x}, {y})")
                os.system(f"adb shell input tap {x} {y} ")
                log_step(job_id, f"click:{selector}", True, f"Tapped at coordinates ({x}, {y})")
            else:
                #Fallback placeholder tap
                os.system("adb shell input tap 500 800")
                log_step(job_id, f"click:{selector}", True, f"Tapped at default position (500,800)")
        except Exception as e:
            log_step(job_id, f"click:{selector}", False, f"Error: {e}")
        time.sleep(0.5)

        
    def type_text(self, job_id, selector, text):
        """Type text into an input field using ADB"""
        try:
            print(f"⌨️ Typing text: {text}")
            os.system(f'adb shell input text "{text}"')
            log_step(job_id, f"type:{selector}", True, f"Typed text '{text}'")
        except Exception as e:
            log_step(job_id, f"type:{selector}", False, f"Error: {e}")
        time.sleep(0.5)

    def long_press(self, job_id, selector, duration=3):
        """Simulate a long press gesture via ADB swipe"""
        try:
            coords = selector.split()
            if len(coords) == 2:
                x, y = coords
                print(f"✋ Long pressing at ({x}, {y}) for {duration}s")
                ms = int(duration * 1000)
                os.system(f"adb shell input swipe {x} {y} {x} {y} {ms}")
                log_step(job_id, f"long_press:{selector}", True, f"Long press at ({x},{y}) for {duration}s")
            else:
                os.system("adb shell input swipe 500 800 500 800 2000")
                log_step(job_id, f"long_press:{selector}", True, "Long press at default position (500,800)")
        except Exception as e:
            log_step(job_id, f"long_press:{selector}", False, f"Error: {e}")
        time.sleep(duration)
    def run_action(self, job_id, action):
        """ 
        Execute an action dictionary in the format:
        {
        "type": "tap" | "click" | "type" | "type_text" | "long_press", "target"/"selector": str, "value"/"text": optional}
        """
        action_type = action.get("type")
        selector = action.get("target") or action.get("selector", "")
        text = action.get("value") or action.get("text", "")

        if action_type in ["tap", "click"]:
            self.click(job_id, selector)
        elif action_type in ["type", "type_text"]:
            self.type_text(job_id, selector, text)
        elif action_type == "long_press":
            self.long_press(job_id, selector)
        else:
            print(f"⚠️ Unknown action type: {action_type}")
            log_step(job_id, f"unknown:{action_type}", False, f"Unknown action type '{action_type}'")