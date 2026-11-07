from fastapi import FastAPI

app = FastAPI(
    title="House Price API",
    description="Serves house price predictions.",
    version="1.0.0",
)


@app.get("/health", tags=["System"], summary="Health check")
def health():
    """Returns ok if the service is alive."""
    return {"status": "ok"}