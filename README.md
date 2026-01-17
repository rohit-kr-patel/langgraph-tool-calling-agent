# LangGraph Looping Tool-Calling Agent

## Overview
A state-driven AI agent built with LangGraph that uses an LLM to select tools, execute them, and safely terminate via a looping workflow.

## Architecture
Agent → Tool → Agent → END  
Routing is controlled by LangGraph based on shared state, not by the agent itself.

## Key Concepts
- Agent handles planning and state updates
- Tools execute deterministic logic only
- Router decides control flow
- Graph enforces safe termination

## Why Looping
Instead of ending after a single tool call, the agent re-runs after tool execution to:
- Detect completion correctly
- Support multi-step instructions
- Avoid infinite loops through state-based guards

## Multi-Step Support
The agent supports sequential instructions such as:

    Add 5 and 6, then multiply by 2

 
It achieves this by:
- Splitting the input into steps
- Tracking progress using a step counter
- Re-planning after each tool execution

## Safety Mechanisms
- Step counter (`step_index`) to track progress
- Maximum step limit (`max_step`) to prevent infinite loops
- Input normalization to skip empty or malformed steps

## Tech Stack
- Python
- LangGraph
- LangChain Tools
- OpenRouter (DeepSeek LLM)

## Installation
Install dependencies using:

    `pip install -r requirements.txt`

## How to Run
Set API key and run     
    
    `python main.py`.

## Learning Outcome
Built a production-safe LangGraph agent with looping execution, multi-step planning, and explicit safeguards against infinite workflows.
