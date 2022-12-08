from typing import List
from datetime import datetime
from pydantic import BaseModel

class ArticlesResponseModel(BaseModel):
    """articles schema response model"""
    id: int
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: str
    publishedAt: datetime
    updatedAt: datetime


class ArticleListResponseModel(BaseModel):
    """articles list"""
    articles: List[ArticlesResponseModel]
