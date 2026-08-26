from fastapi import FastAPI

app = FastAPI(
    title="ML Evaluation Platform",
    version="0.1.0",
    description="Reproducible machine-learning evaluation workflows.",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "ml-evaluation-platform",
        "version": app.version,
    }
