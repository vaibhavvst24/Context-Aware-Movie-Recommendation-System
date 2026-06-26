from fastapi import FastAPI, HTTPException
from app.schemas import RecommendationRequest
from app.services import get_recommendations
from fastapi.responses import RedirectResponse

app = FastAPI(
    title="Movie Recommendation System API",
    version="1.0"
)


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

@app.post("/recommend")
def recommend(request: RecommendationRequest):

    try:

        recommendations = get_recommendations(
            request.user_id,
            request.context
        )

        return {
            "recommendations": recommendations
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
