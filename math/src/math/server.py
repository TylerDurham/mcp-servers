from fastmcp.server import FastMCP

mcp = FastMCP("MathServer", stateless_http=True)


@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Adds the second integer to the first integer and returns the result.
    """
    return a + b


@mcp.tool("Subtract a Number from Another")
def subtract(a: int, b: int) -> int:
    """
    Subtracts the second integer from the first integer and returns the result.
    """
    return a - b
