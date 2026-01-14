from openai import OpenAI

client = OpenAI(
    api_key=
    base_url="https://openrouter.ai/api/v1"
)

def get_decision(input_text):
    prompt=f"""
    You are a router agent.

    user input:"{input_text}"

    Available Tools:
    -add
    -multiply
    -sub
    -divide

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
    state["decision"] = "none"
    input_text=state["input"].lower()
    words=input_text.split()
    numbers=[]
    for word in words:
        if word.isdigit():
            numbers.append(int(word))

    if len(numbers) < 2:
        state["decision"] = "none"
        return state

    
    state["a"]=numbers[0]
    state["b"]=numbers[1]
  
    state["decision"] = get_decision(input_text)
    print("LLM DECISION:", state["decision"])
    
    return state