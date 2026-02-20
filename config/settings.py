import os
from dotenv import load_dotenv

# ---------------------------
# Load environment variables
# ---------------------------
load_dotenv()

# ---------------------------
# Gemini API Key (Mandatory)
# ---------------------------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found in .env file")

# ---------------------------
# Model Configuration (Optional)
# ---------------------------
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-3-flash-preview")

# ---------------------------
# Load system prompt from external file
# ---------------------------
PROMPT_FILE = os.path.join(os.path.dirname(__file__), "system_prompt.txt")

try:
    with open(PROMPT_FILE, "r", encoding="utf-8") as f:
        SYSTEM_PROMPT = f.read()
except Exception:
    # Fallback prompt (if file missing)
    SYSTEM_PROMPT = """
    You are an intelligent AI Career Advisor.
    Provide clear, structured, and practical career guidance.
    """