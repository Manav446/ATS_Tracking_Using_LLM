import os
import sys
from pathlib import Path
import warnings

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.document_loaders import PyPDFLoader

from src.logger import logging
from src.exception import CustomException
from src import constants
from src.utils import get_gemini_api_key

logger = logging.getLogger("Helper")
warnings.filterwarnings("ignore")

class Helper:
    def __init__(self):
        super().__init__()
        self.llm_model = None
        self.chain = None
        self.prompt_template = None
    
    def resume_data(self, input_file)-> str:
        logger.info("Entering into resume_data() for getting the resume text.....")
        try:
           reader = PyPDFLoader(input_file)
           text = reader.load()[0].page_content
        except Exception as e:
            raise CustomException(e, sys)
        return text

    def get_model(self):
        logger.info("Loading Gemini model.......")
        try:
            llm_model = ChatGoogleGenerativeAI(
                google_api_key = get_gemini_api_key(), 
                model = constants.LLM_MODEL_NAME,
                temperature = constants.LLM_MODEL_TEMPERATURE_VALUE, 
                top_p=0.8,
                convert_system_message_to_human = constants.CONVERT_TO_HUMAN_MESSAGE
            )
        except Exception as e:
            raise CustomException(e, sys)
        return llm_model
    
    def get_prompt(self):
        logger.info("Getting the prompt for LLM model.........")

        try:
            input_prompt = """
            Hey Act Like a skilled or very experience ATS(Application Tracking System)
            with a deep understanding of tech field,software engineering,data science ,data analyst
            and big data engineer. Your task is to evaluate the resume based on the given job description.
            You must consider the job market is very competitive and you should provide 
            best assistance for improving the resumes. And also if possible tell whether the resume is applicable for the passed job description like applicable or not applicable.
            Assign the percentage Matching based 
            on Jd and the missing keywords with high accuracy
            resume:{resume_content}
            description:{job_description}

            I want the response in one single string having the structure
            {{"JD Match":"%", "MissingKeywords:[]", "Profile Summary":"", "applicable": ""}}
            """
        
            prompt_template = PromptTemplate(
                input_variables=["resume_content", "job_description"],
                template=input_prompt
            )
        
        except Exception as e:
            raise CustomException(e, sys)
        return prompt_template
        
    
    def get_chain(self):
        logger.info("Getting chain for LLM.....")
        try:
            chain = LLMChain(llm=self.get_model(), prompt=self.get_prompt())
        except Exception as e:
            raise CustomException(e, sys)
        return chain
    
    def get_response_from_gemini(self, input_variables):
        logger.info("Calling GEMINI API for ATS tracking .........")
        try:
            chain = self.get_chain()
            response = chain.invoke(input_variables)
        except Exception as e:
            raise CustomException(e, sys)
        return response
        
