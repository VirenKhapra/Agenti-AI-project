print(" GRAPH FILE STARTED")

from typing import TypedDict

print(" TypedDict imported")

from langgraph.graph import StateGraph, END

print(" LangGraph imported")

from data_input import get_email_text

print(" data_input imported")

from llm_extractor import extract_data

print(" llm_extractor imported")

from validator import validate_data

print(" validator imported")


# STATE
class AgentState(TypedDict):
    email_text: str
    extracted_data: str
    validation_result: dict


# NODE 1 → Fetch Email
def fetch_email_node(state):

    print("\n FETCHING EMAIL...\n")

    email_text = get_email_text()

    return {
        "email_text": email_text
    }


# NODE 2 → Extract Data
def extract_data_node(state):

    print("\n EXTRACTING DATA...\n")

    extracted = extract_data(state["email_text"])

    return {
        "extracted_data": extracted
    }


# NODE 3 → Validate Data
def validate_node(state):

    print("\n VALIDATING DATA...\n")

    result = validate_data(state["extracted_data"])

    print("\n VALIDATION RESULT:\n")
    print(result)

    return {
        "validation_result": result
    }


# CONDITIONAL ROUTING
def decide_next_step(state):

    if state["validation_result"]["status"] == "valid":
        return "valid"

    return "invalid"


# BUILD GRAPH
workflow = StateGraph(AgentState)

# ADD NODES
workflow.add_node("fetch_email", fetch_email_node)
workflow.add_node("extract_data", extract_data_node)
workflow.add_node("validate", validate_node)

# ENTRY POINT
workflow.set_entry_point("fetch_email")

# FLOW
workflow.add_edge("fetch_email", "extract_data")
workflow.add_edge("extract_data", "validate")

# CONDITIONAL FLOW
workflow.add_conditional_edges(
    "validate",
    decide_next_step,
    {
        "valid": END,
        "invalid": "extract_data"
    }
)

# COMPILE GRAPH
app = workflow.compile()