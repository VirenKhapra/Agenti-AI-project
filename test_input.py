from data_input import get_email_text
from llm_extractor import extract_data

print("🚀 Running full pipeline...")

email_text = get_email_text()

print("\n📩 RAW EMAIL:\n")
print(email_text)

result = extract_data(email_text)

print("\n✅ FINAL OUTPUT:\n")
print(result)