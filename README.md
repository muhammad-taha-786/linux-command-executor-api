# Linux Command Executor API

A secure, production-ready FastAPI application that executes specific, predefined Linux system commands and returns their outputs in clean JSON format.

## Features
- **Secure Execution:** Uses Python's `subprocess` module safely without shell injection risks.
- **Predefined Commands Only:** Strictly allows execution of `uptime`, `df -h`, `free -m`, and `whoami`.
- **Error Handling:** Built-in catch-all for system command errors and structural status returns.
- **Health Check:** Includes a `/health` endpoint for monitoring.

## Technologies Used
- Python 3
- FastAPI
- Uvicorn
- Linux CLI Utilities
