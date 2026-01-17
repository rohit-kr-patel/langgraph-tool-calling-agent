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

    # ---- First run: planning phase ----
    

    input_text = state["input"].lower()
    if "steps" not in state:
        state["steps"] = [
        s.strip()
        for s in input_text.split("then")
        if s.strip()
    ]
        state["step_index"]=0
    
    if state["step_index"] >= len(state["steps"]) or state["step_index"]>=state["max_step"] :
        state["done"]=True
        return state
    state["done"] = False
    current_step_text=state["steps"][state["step_index"]]
    numbers = []
    words = current_step_text.split()
    for word in words:
            clean = "".join(ch for ch in word if ch.isdigit())
            if clean:
                numbers.append(int(clean))
    if state["step_index"]==0:
        if len(numbers) < 2:
            state["decision"] = "none"
            return state

        state["a"] = numbers[0]
        state["b"] = numbers[1]
    else:
        if len(numbers) < 1:
            state["decision"] = "none"
            return state

        state["a"] = state["res"]
        state["b"] = numbers[0]
    decision = get_decision(current_step_text)
    state["decision"] = decision
    state["step_index"]+=1
    print("PLANNING STEP:",current_step_text)
    print("LLM DECISION:", decision)

    return state