from typing import Union
from abc import ABC, abstractmethod


class IArticleGateway(ABC):
    @abstractmethod
    async def get_articles() -> Union[int, list]:
        """make request on spaceflightnewsapi and return
           the articles
        """

        raise NotImplementedError("Method not implemented")
