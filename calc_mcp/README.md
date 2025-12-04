# Calc MCP Server

This project demonstrates how to set up and run a simple **Model Context Protocol (MCP) Server** for basic arithmetic operations (add, subtract, multiply, divide) using Python.

## 🚀 Prerequisites

Before running the server, ensure you have the following installed:

- **Windows Package Manager (winget)**
- **NVM for Windows** (Node Version Manager)
- **Node.js (LTS version)**

---

## 📦 Installation Steps

### 1. Install NVM for Windows
```powershell
winget install -e --id CoreyButler.NVMforWindows
```

### 2. Install Node.js (LTS)
```powershell
nvm install lts
nvm use lts
node --version
```

---

## 🔍 Run the Model Inspector

To verify MCP server functionality, run:
```bash
npx @modelcontextprotocol/inspector
```

---

## 🛠️ MCP Server Setup

In `calc.py`, initialize the MCP server:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="calc-mcp")

# Add tools for basic arithmetic
# Example:
# mcp.tool("add", lambda a, b: a + b)
# mcp.tool("sub", lambda a, b: a - b)
# mcp.tool("multiply", lambda a, b: a * b)
# mcp.tool("divide", lambda a, b: a / b)
```

---

## ▶️ Run the Server

Start the MCP server in development mode:
```bash
mcp dev calc.py
```

---

## 📖 Usage

Once the server is running, you can interact with it through the **Model Inspector** or any MCP-compatible client. The server exposes tools for:

- `add(a, b)` → returns sum  
- `sub(a, b)` → returns difference  
- `multiply(a, b)` → returns product  
- `divide(a, b)` → returns quotient  

---

## ✅ Summary

You now have:
1. Installed NVM and Node.js  
2. Verified Node.js installation  
3. Run the MCP Model Inspector  
4. Built and launched a custom MCP server for arithmetic operations  

This serves as a foundation for extending MCP servers with more complex tools and workflows.
```

