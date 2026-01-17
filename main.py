from typing import TypedDict
from langgraph.graph import StateGraph,END

from agent import agent_node
from tools import add,multiply,sub,divide

#define State
class AgentState(TypedDict):
    input:str
    decision:str
    a:int
    b:int
    res:float
    done: bool 
    steps:dict
    step_index:int
    max_step:int

def adding_node(state:AgentState)->AgentState:
    state["res"] = add.invoke({
        "a": state["a"],
        "b": state["b"]
    })
    return state
def sub_node(state:AgentState)->AgentState:
    state["res"] = sub.invoke({
        "a": state["a"],
        "b": state["b"]
    })
    return state
def mul_node(state:AgentState)->AgentState:
    state["res"] = multiply.invoke({
        "a": state["a"],
        "b": state["b"]
    })
    return state
def div_node(state:AgentState)->AgentState:
    state["res"] = divide.invoke({
        "a": state["a"],
        "b": state["b"]
    })
    return state


def route_decision(state: AgentState):
    return state["decision"]

def route_after_agent(state: AgentState):
    if state.get("done"):
        return END
    return state["decision"]

graph=StateGraph(AgentState)
graph.add_node("agent",agent_node)
graph.add_node("adding_node",adding_node)
graph.add_node("sub_node",sub_node)
graph.add_node("mul_node",mul_node)
graph.add_node("div_node",div_node)

graph.set_entry_point("agent")


graph.add_conditional_edges(
    "agent",
    route_after_agent,
    {
        "add": "adding_node",
        "sub": "sub_node",
        "multiply": "mul_node",
        "divide": "div_node",
        END: END,
        "none": END,
    }
)

# Tool → Agent (THIS CREATES THE LOOP)
graph.add_edge("adding_node", "agent")
graph.add_edge("sub_node", "agent")
graph.add_edge("mul_node", "agent")
graph.add_edge("div_node", "agent")



app=graph.compile()

if __name__ == "__main__":
    initial_state = {
        "input": "Add 10 and 5 then then then then ",
       "max_step": 5 
    }

    final_state = app.invoke(initial_state)
    print(final_state)