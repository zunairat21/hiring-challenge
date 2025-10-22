import re

def preprocess_input(user_input: str) -> str:
    """
    Clean and normalize user input before intent parsing
    """
    # Remove leading/trailing spaces
    text = user_input.strip()

    # Convert to lowercase for uniformity

    text = text.lower()

    # Remove unnecessary characters (like emojis, symbols)
    text = re.sub(r"[^a-zA-Z0-9\s,.!?]", "", text)

    return text 

def validate_input(user_input: str) -> bool:
    """
    Check if user input is valid (not empty or gibberish).
    """
    if not user_input or len(user_input.strip()) < 2:
        return False
    return True

def handle_user_input(raw_input: str):
    """
    Full pipeline: validate, clean and return structured input
    """
    if not validate_input(raw_input):
        return{"valid" : False, "cleaned" : None, "error":"invalid input provided"}
    cleaned = preprocess_input(raw_input)
    return {"valid":True, "cleaned":cleaned, "error": None}
