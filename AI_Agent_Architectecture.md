# Phase 02 – System Architecture Design

## 🎯 Objective
To design a modular AI Agent architecture that automates the **Outlook account creation process** by understanding user interactions, executing steps intelligently, and validating each stage for successful completion.

---

## 🧱 System Components

| Component | Description |
|------------|--------------|
| 🧭 **User Interface Layer** | Interface where the user triggers or monitors the AI Agent (CLI or Web UI). Displays progress and status updates. |
| 🧠 **AI Logic Layer** | The core brain of the system that interprets Outlook flow, decides next steps, and manages control flow using state tracking. |
| ⚙️ **Automation Layer** | Executes real user-like actions (clicks, typing, navigation) using automation tools such as Selenium or Playwright. |
| 💾 **Data / Storage Layer** | Securely stores intermediate states, logs, and encrypted credentials for tracking and debugging. |

---

## 🔄 Outlook Flow → AI Agent Mapping

| Outlook Step | AI Agent Action |
|---------------|----------------|
| Add Email Accounts → “Crear cuenta” | Detect “Create Account” button via UI element recognition and click it |
| Enter username → “Siguiente” | Generate or input username; submit the form |
| Enter password → “Siguiente” | Create secure password; click next |
| Fill first/last name → “Siguiente” | Use name dataset or user-provided input |
| Select DOB → “Siguiente” | Generate valid date of birth; move to next step |
| CAPTCHA → “Hold button” | Pause automation and request manual validation if required |
| Success Message → “ACEPTAR” | Confirm completion, log result, and close session |

---

## 🧠 Logical Workflow

1. **Initialization**
   - Agent starts session
   - Loads environment variables (browser, credentials)

2. **Step Detection**
   - Identifies current Outlook page/screen
   - Uses pattern recognition (text, DOM, or API cues)

3. **Action Execution**
   - Performs context-aware actions (input, click, wait)
   - Validates success of each step before continuing

4. **Error Handling**
   - Retries failed steps or reports manual intervention needed

5. **Completion**
   - Verifies account creation message
   - Logs process summary

---

## Architecture Diagram

+--------------------------------------------------------+
| AI Outlook Account Agent |
+--------------------------------------------------------+
| 1. User Interface (CLI / Web UI) |
| - Initiate and monitor agent workflow |
| - Show live progress and logs |
| |
| 2. AI Logic Layer |
| - Understands Outlook flow (rule-based or LLM) |
| - Decides next action dynamically |
| |
| 3. Automation Layer (Selenium / Playwright) |
| - Simulates user actions (click, input, navigation) |
| - Validates UI transitions and waits where needed |
| |
| 4. Data Layer |
| - Stores logs, outcomes, and credentials securely |
+--------------------------------------------------------+


## ✅ Summary
This architecture mirrors the human-like process of creating an Outlook account, breaking it into identifiable, automatable steps. The modular design ensures flexibility — future versions can integrate visual recognition, language understanding (LLMs), or real-time monitoring without altering the core structure.