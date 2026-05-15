from langchain.tools import Tool

from data_input import get_email_text
from llm_extractor import extract_data


# Tool 1 (extracting the emial)
email_tool = Tool(
    name="Email Extraction Tool",
    func=get_email_text,
    description="Fetches latest email and extracts raw text from body and attachments."
)


# Tool 2 (fetching the data through llm)
def llm_tool_wrapper(text):
    return extract_data(text)

llm_tool = Tool(
    name="Financial Data Extractor",
    func=llm_tool_wrapper,
    description="Extracts structured financial information from email text."
)

