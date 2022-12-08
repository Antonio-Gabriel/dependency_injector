from typing import Callable, List, Iterable
from contextlib import AbstractAsyncContextManager

from ..model import ArticleModel
from ..gateway.contracts import IArticleGateway


class ArticlesService:

    def __init__(self, 
        timeout: int,
        article_gateway: Callable[..., AbstractAsyncContextManager[IArticleGateway]]
        ) -> None:
        self.__timeout = timeout
        self.__articles: List[ArticleModel] = []
        self.__article_gateway = article_gateway
        
    async def get_articles(self) -> Iterable[ArticleModel]:
        """resolt article response"""        

        async with self.__article_gateway(self.__timeout)\
            .get_articles() as gateway:            
            _, articles = gateway
                                               
            for index, article in enumerate(articles):
                self.__articles.append(
                    ArticleModel(
                        id=(index + 1),
                        title=article.get("title"),
                        url=article.get("url"),
                        imageUrl=article.get("imageUrl"),
                        newsSite=article.get("newsSite"),
                        summary=article.get("summary"),
                        publishedAt=article.get("publishedAt"),
                        updatedAt=article.get("updatedAt")
                    )._asdict()
                )
            
            return self.__articles
