from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide

from .containers import Container
from .services import ArticlesService
from .schema import ArticleListResponseModel

router = APIRouter()


@router.get("/articles", 
    tags=["Article"],
    status_code=status.HTTP_200_OK,
    response_model=ArticleListResponseModel
    )
@inject
async def get_articles(
    article_service: ArticlesService = Depends(Provide[Container.article_service])
):
    articles = await article_service.get_articles()    
    return {
        "articles": articles
    }
