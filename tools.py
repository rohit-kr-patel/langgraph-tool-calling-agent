from langchain.tools import tool

#Define tools
@tool
def add(a:int,b:int)->int:
    """
    Use this tool when user asks for addition two numbers.
    """
    return a+b

@tool
def multiply(a:int,b:int)->int:
    """
    Use this tool when user asks for multiplication or product of two numbers.
    """
    return a*b

@tool
def divide(a:int,b:int)-> float:
    """
    Use this tool when user ask for division.
    """
    return a/b

@tool
def sub(a:int , b:int)->int:
    """
    Use this tool when user asks for subtraction of two numbers.
    """
    return a-b

tools=[add,multiply,divide,sub]
tools_by_name={tool.name: tool for tool in tools}

