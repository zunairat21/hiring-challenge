from logger import log_step
from input_handler import handle_user_input
from intent_parser import parse_intent_and_actions
from action_executor import ActionExecutor
import uuid
import time

def main():
    executor = ActionExecutor()
    job_id = f"session_{str(uuid.uuid4())[:8]}"

    print("🤖 AI Outlook Agent started! Type 'exit' to quit.\n")
    log_step(job_id, "start", True, "Agent started")

    while True:
        user_input = input("You: ").strip()

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
        intent = parsed.get("intent")
        actions = parsed.get("actions", [])
        print(f"🔍 Intent detected: {parsed['intent']}")
        print(f"🧩 Actions: {parsed['actions']}")
        log_step(job_id, "intent_parsed", True, f"Intent: {parsed['intent']}")

        if not actions:
            print("⚠️ No actions to execute.")
            log_step(job_id, "no_actions", False, "No actions found.")
            continue

        # Step 3:Execute actions (real ADB)

        for action in actions:
            executor.run_action(job_id, action)
            time.sleep(1)
            
if __name__ == "__main__":
 main()
