# PNAI AI Agent — secure starter

This starter contains a small FastAPI backend and browser chat UI. It is **not yet connected** to your GitHub, Azure Data Factory, or Microsoft Fabric accounts, and it is not a compiled Android APK.

## First: secure the exposed key
1. Open https://platform.openai.com/api-keys
2. Delete/revoke the key that was pasted into ChatGPT.
3. Review https://platform.openai.com/usage for unexpected activity.
4. Create a replacement key only after revoking the exposed one.

## Run locally
1. Install Python 3.11+.
2. In this folder, run: `pip install -r requirements.txt`
3. Set `OPENAI_API_KEY` as an environment variable in your terminal/hosting provider. Do not commit it.
4. Run: `uvicorn app:app --host 0.0.0.0 --port 8000`
5. Open `http://localhost:8000`.

For the static UI to be served, add the following lines at the end of `app.py` before starting the server:

```python
from pathlib import Path
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return FileResponse("static/index.html")
```

## Deployment
Deploy the backend to a trusted hosting provider. Add `OPENAI_API_KEY` in the host's secret/environment-variable settings. Never put the secret in HTML, JavaScript, an APK, a public GitHub file, or a screenshot.

## Azure / Fabric / GitHub
Those integrations are intentionally not enabled in this starter. Add them only after setting up OAuth/service-principal credentials and least-privilege permissions. Begin with read-only monitoring; require approval before restarts, deployments, or other cloud changes.

## Android
An Android app should call your deployed backend over HTTPS. Do not ship an OpenAI key in the Android app. This ZIP does not include a compiled APK.
