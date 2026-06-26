from pydantic import BaseModel


class RecommendationRequest(BaseModel):
    user_id: int
    context: int


class MovieRecommendation(BaseModel):
    movie: str
    predicted_rating: float


class RecommendationResponse(BaseModel):
    recommendations: list[MovieRecommendation]