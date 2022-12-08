import os

from typing import Union
from contextlib import asynccontextmanager
from aiohttp import ClientSession, ClientTimeout

from .contracts import IArticleGateway


class ArticleListGateway(IArticleGateway):
    """Gateway of articles"""

    def __init__(self, timeout: int) -> None:
        self._timeout = ClientTimeout(timeout)
    
    @asynccontextmanager
    async def get_articles(self) -> Union[int, list]:
        """make request on api and return
           the articles
        """
        async with ClientSession(timeout=self._timeout) as session:
            async with session.get(os.environ["URL_BASE"]) as response:
                if response.status != 200:
                    response.raise_for_status()
                            
                yield response.status, await response.json() 
