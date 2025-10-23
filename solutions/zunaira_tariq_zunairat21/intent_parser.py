# intent_parser.py
def parse_intent_and_actions(text: str):
    """
    Simple rule-based intent -> action sequence mapper.
    Returns: {"intent": str, "actions": [ {type,target,value?}, ... ]}
    """
    text = (text or "").lower()

    # Create account flow
    if ("create" in text or "new account" in text or "crear cuenta" in text) and "outlook" in text:
        return {
            "intent": "create_outlook_account",
            "actions": [
                {"type": "click", "target": "create_account_button"},
                {"type": "type",  "target": "username_field", "value": "<<<username>>>"},
                {"type": "type",  "target": "password_field", "value": "<<<password>>>"},
                {"type": "type",  "target": "first_last_name_fields", "value": "<<<name>>>"},
                {"type": "type",  "target": "dob_fields", "value": "1996-02-24"},
                {"type": "long_press", "target": "captcha_button"},
                {"type": "click", "target": "accept_button"}
            ]
        }

    # Open inbox
    if "open" in text and "inbox" in text:
        return {"intent": "open_inbox", "actions": [{"type": "click", "target": "inbox_button"}]}

    # Compose / send email
    if "send" in text and "email" in text:
        # simple: open compose; typing recipient handled by action_executor later if value present
        return {
            "intent": "send_email",
            "actions": [
                {"type": "click", "target": "compose_button"},
                {"type": "type", "target": "to_field", "value": "alice@example.com"},
                {"type": "type", "target": "subject_field", "value": "Hello"},
                {"type": "type", "target": "body_field", "value": "Hi Alice, this is a test."},
                {"type": "click", "target": "send_button"}
            ]
        }

    # Schedule meeting
    if "schedule" in text and "meeting" in text:
        return {"intent": "schedule_meeting", "actions": [{"type": "click", "target": "calendar_create_meeting"}]}

    # CAPTCHA test phrase
    if "captcha" in text or "press and hold" in text or "mantén presionado" in text:
        return {"intent": "test_captcha_hold", "actions": [{"type": "long_press", "target": "captcha_button", "value": 3}]}

    # fallback
    return {"intent": "unknown", "actions": []}