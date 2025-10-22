import re
def detect_intent(cleaned_input: str) -> str:
    """
    Detect what the user wants the agent do(e.g . , create account, login, etc. )
    """
    text = cleaned_input.lower()

    if "create" in text or "new account" in text or "sign up" in text:
        return "create_account"
    elif "login" in text or "sign in " in text:
        return "login"
    elif "recover" in text or "reset" in text:
        return "recover_password"
    else:
        return "unknown"
def generate_action_sequence(intent: str) -> list:
    """
    Based on detected intent, generate ordered steps the agent will execute
    """
    if intent == "create_account":
        return [
            "open_outlook_app",
            "tap_create_account",
            "enter_username",
            "enter_password",
            "enter_name",
            "enter_dob", 
            "solve_captcha", 
            "confirm_account"
        ]
    elif intent == "login":
        return [
            "open_outlook_app",
            "tap_sign_in",
            "enter_username",
            "enter_password",
            "confirm_login"
        ]
    elif intent == "recover_password":
        return [
            "open_outlook_app",
            "tap_forgot_password",
            "enter_email",
            "verify_identity",
            "reset_password"
        ]
    else: 
        return []
    
def parse_intent_and_actions(cleaned_input: str) :
    """
    Full pipeline: detect intent and get corresponding action sequence
    """
    intent = detect_intent(cleaned_input)
    actions = generate_action_sequence(intent)
    return {"intent":intent, "actions":actions}