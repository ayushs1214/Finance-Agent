from typing import Dict, List
import autogen
import google.generativeai as genai
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

# Custom configuration for Gemini-based LLM
class GeminiConfig:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-pro')
    
    async def create(self, messages):
        prompt = self._format_messages(messages)
        response = self.model.generate_content(prompt)
        return response.text
    
    def _format_messages(self, messages):
        formatted_prompt = ""
        for message in messages:
            role = message.get("role", "user")
            content = message.get("content", "")
            formatted_prompt += f"{role}: {content}\n"
        return formatted_prompt

# Create a configuration dictionary for the LLM
config_list = [{
    "model": "gemini-pro",
    "api_base": "not_openai",  # This indicates we're not using OpenAI
    "api_type": "not_openai",
    "api_key": GEMINI_API_KEY
}]

# Initialize our agents
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    system_message="A human user interacting with the financial management system.",
    code_execution_config={"last_n_messages": 3, "work_dir": "financial_workspace", "use_docker": False},
    llm_config=False
)

financial_advisor = autogen.AssistantAgent(
    name="Financial_Advisor",
    system_message="""You are an expert financial advisor. Your responsibilities include:
    - Analyzing financial data and providing insights
    - Offering personalized financial recommendations
    - Identifying potential savings opportunities
    - Creating financial plans and strategies""",
    llm_config={
        "config_list": config_list,
        "temperature": 0.7,
        "cache_seed": None,
        "use_cache": False,
        "timeout": 60,
        "functions": None
    }
)

data_analyst = autogen.AssistantAgent(
    name="Data_Analyst",
    system_message="""You are a financial data analyst. Your responsibilities include:
    - Processing and organizing financial data
    - Identifying spending patterns and trends
    - Generating reports and visualizations
    - Maintaining accurate financial records""",
    llm_config={
        "config_list": config_list,
        "temperature": 0.7,
        "cache_seed": None,
        "use_cache": False,
        "timeout": 60,
        "functions": None
    }
)
  