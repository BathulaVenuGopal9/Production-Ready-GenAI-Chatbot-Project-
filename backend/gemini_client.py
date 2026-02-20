from google import genai
from config.settings import GEMINI_API_KEY, MODEL_NAME
from backend.logger import get_logger

logger = get_logger()

class GeminiClient:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate_response(self, prompt: str) -> str:
        try:
            logger.info("Sending request to Gemini API")

            response = self.client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

            if response and response.text:
                logger.info("Gemini API responded successfully")
                return response.text.strip()
            else:
                logger.warning("Gemini returned empty response")
                return "I'm sorry, I couldn't generate a response. Please try again."

        # API-related issues
        except ValueError as ve:
            logger.error(f"Configuration error: {str(ve)}")
            return "⚠️ Configuration error. Please contact administrator."

        # Network or connection errors
        except ConnectionError as ce:
            logger.error(f"Network error: {str(ce)}")
            return "⚠️ Network issue detected. Please check your connection."

        # Rate limit / quota issues
        except Exception as e:
            error_message = str(e).lower()

            if "quota" in error_message or "rate" in error_message:
                logger.warning(f"Rate limit reached: {str(e)}")
                return "⚠️ Service is busy right now. Please try again in a moment."

            logger.error(f"Unexpected Gemini error: {str(e)}")
            return "⚠️ Something went wrong. Please try again later."