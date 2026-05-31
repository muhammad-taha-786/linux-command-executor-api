from fastapi import FastAPI
from routes import system

app = FastAPI(
    title="Linux Command Executor API",
    description="A secure API to execute predefined Linux system commands.",
    version="1.0.0"
)

# Health endpoint as required
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy"}

# Include system command routes
app.include_router(system.router)