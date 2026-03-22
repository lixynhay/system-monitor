from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from core import SystemCore
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory=".")

# API Endpoints
@app.get("/api/data")
async def get_stats():
    try:
        return SystemCore.get_metrics()
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/api/kill/{pid}")
async def kill_proc(pid: int):
    if SystemCore.kill_process(pid):
        return {"status": "success"}
    raise HTTPException(status_code=403, detail="Access denied")

# Frontend Route
@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
