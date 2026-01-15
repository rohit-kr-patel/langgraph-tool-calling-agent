# LangGraph Looping Tool-Calling Agent

## Overview
A state-driven AI agent built with LangGraph that uses an LLM to route tool execution and safely terminate via a looping workflow.

## Architecture
Agent → Tool → Agent → END, with routing controlled by LangGraph based on shared state.

## Key Concepts
- Agent plans and updates state
- Tools execute logic only
- Router decides control flow
- Graph enforces safe termination

## Why Looping
The agent re-runs after tool execution to detect completion and avoid infinite loops.

## Tech Stack
Python, LangGraph, LangChain Tools, OpenRouter (DeepSeek LLM)

## Installation

Install dependencies using:

`pip install -r requirements.txt`

## How to Run
Set API key and run `python main.py`.

## Learning Outcome
Built a looping LangGraph agent with clean separation of planning, execution, and routing.
