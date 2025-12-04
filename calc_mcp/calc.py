from mcp.server.fastmcp import FastMCP

# creating a server
mcp = FastMCP("calc_mcp")

@mcp.tool()
def add(a:int|float, b:int|float) -> int|float:
    """This method adds two numbers

    Args:
        a (int | float): number 
        b (int | float): number

    Returns:
        int|float: a + b
    """
    return a + b

@mcp.tool()
def subtract(a:int|float, b:int|float) -> int|float:
    """This method adds two numbers

    Args:
        a (int | float): number 
        b (int | float): number

    Returns:
        int|float: a - b
    """
    return a - b

@mcp.tool()
def multiply(a: int|float, b: int|float) -> int|float:
    """Multiplies two numbers

    Args:
        a (int): number
        b (int): number

    Returns:
        int: a * b
    """
    return a * b

@mcp.tool()
def divide(a: int|float, b: int|float) -> float:
    """Divides two numbers

    Args:
        a (int): number
        b (int): number

    Returns:
        float: a / b
    """
    return a / b


if __name__ == "__main__":
    mcp.run(transport="stdio")



