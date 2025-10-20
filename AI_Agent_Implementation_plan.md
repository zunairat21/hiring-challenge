# Phase 03 — Implementation Blueprint

## Objective
Scaffold and define the implementation of the AI Agent modules that will automate the Outlook account creation flow on Android devices.

## Modules (purpose & responsibilities)
1. `input_handler.py` — Accepts job input (CURP row, job_id) and normalizes parameters.
2. `intent_parser.py` — Converts high-level job instructions into a step list (username -> password -> name -> dob -> captcha -> confirm).
3. `action_executor.py` — Executes actions on the Android device via ADB/Appium (tap, type, long_press, swipe).
4. `vision_module.py` (optional) — Captures screenshots and extracts text via OCR.
5. `logger.py` — Writes structured JSON logs for each step.
6. `main_controller.py` — Orchestrates the whole flow for a single job.

## Data flow
Input (job) -> InputHandler -> IntentParser -> MainController -> ActionExecutor -> VisionModule -> Logger -> Output (job result)

## Local dev setup
- Python 3.10+
- Virtual environment
- Packages: appium-python-client, adbutils, opencv-python, pillow, pytesseract, fastapi (later)

## Day 03 deliverables
- `AI_Agent_Implementation_Plan.md` (this file)
- `src/` folder with module stubs
- `requirements.txt`
- Basic README status update in `docs/daily_progress.md`