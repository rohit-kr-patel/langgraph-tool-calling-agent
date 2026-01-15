from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("API_KEY")


client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

def get_decision(input_text):
    prompt=f"""
    You are a router agent.

    user input:"{input_text}"

    Available Tools:
   - add        ← add, addition, plus
   - sub        ← subtract, minus, subtraction
   - multiply   ← multiply, product
   - divide     ← divide, division

Rules:
    - Return only the tool name
    -if no tool applies, return "none"

    """
    response = client.chat.completions.create(
    model="deepseek/deepseek-r1-0528:free",
    messages=[
        {"role": "system", "content":prompt},
    ],
    temperature=0
)

    return response.choices[0].message.content.strip().lower()

def agent_node(state):
    if "res" in state:
        # Tool has already run
        state["done"] = True
        return state

    # ---- First run: planning phase ----
    state["done"] = False

    input_text = state["input"].lower()
    words = input_text.split()

    numbers = []
    for word in words:
        clean = "".join(ch for ch in word if ch.isdigit())
        if clean:
            numbers.append(int(clean))

    if len(numbers) < 2:
        state["decision"] = "none"
        return state

    state["a"] = numbers[0]
    state["b"] = numbers[1]

    decision = get_decision(input_text)
    state["decision"] = decision
    print("LLM DECISION:", decision)

    return state