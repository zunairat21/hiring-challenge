from logger import log_step
from input_handler import handle_user_input
from intent_parser import parse_intent_and_actions
from action_executor import ActionExecutor

def main():
    executor = ActionExecutor()
    job_id = "session_001"

    print("🤖 AI Outlook Agent started! Type 'exit' to quit.\n")
    log_step(job_id, "start", True, "Agent started")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            log_step(job_id, "exit", True, "User exited the program")
            break

        # Step 1: Clean input
        cleaned = handle_user_input(user_input)

        if not cleaned["valid"]:
            print(f"⚠️ Error:{cleaned['error']}")
            log_step(job_id, "input_error", False, cleaned["error"])
            continue

        # Step 2: Parse intent

        parsed = parse_intent_and_actions(cleaned["cleaned"])
        print(f"🔍 Intent detected: {parsed['intent']}")
        print(f"🧩 Actions: {parsed['actions']}")
        log_step(job_id, "intent_parsed", True, f"Intent: {parsed['intent']}")

        # Step 3: Simulate execution
        job_id = "session_001"
        for action in parsed["actions"]:
            act_type = action.get("type")
            act_target = action.get("target")
            act_value = action.get("value")

            if act_type == "click":
                executor.click(job_id,act_target)
            elif act_type == "type":
                executor.type_text(job_id,act_target,act_value)
            elif act_type == "long_press":
                executor.long_press(job_id, act_target)
            else:
                print(f" ⚠️ Unknown action type : {act_type}")
                log_step(job_id, "unknown_action", False, f"Unknown: {act_type}")

if __name__ == "__main__":
 main()
