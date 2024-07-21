from dotenv import load_dotenv
import sys
import os

from src.logger import logging
from src.exception import CustomException

logger = logging.getLogger("Utils")
load_dotenv()

def get_gemini_api_key() -> str:
    logger.info("Getting Gemini API KEY.........")
    try :
        GEMINI_API_Key = os.getenv("GEMINI_API_KEY")
    except Exception as exe:
        raise CustomException(exe, sys)
    return GEMINI_API_Key
