import tomllib
from pathlib import Path

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


def get_value(config, key: str, default=None):
    try:
        return config[key]
    except KeyError:
        return default


def run():
    transport = "streamable-http"
    port = 8080
    project_root = Path(__file__).resolve().parents[2]
    config_file = f"{project_root}/pyproject.toml"
    with open(config_file, "rb") as f:
        config = tomllib.load(f)
        server = config.get("math-mcp.server")
        if server != None:
            port = get_value(server, "port", str(port))
            transport = get_value(server, "transport", transport)
            # host = get_value(server, "host", "http://127.0.0.1")

    mcp.run(transport=transport, port=int(port))
