import pytest

from unittest import mock
from src.gateway import ArticleListGateway

@pytest.mark.asyncio
# @pytest.fixture
async def test_article_list_gateway():
    """should be return a list of articles"""
    article_list = ArticleListGateway(5)
    async with article_list.get_articles() as gateway:
        status, articles = gateway

        assert status == 200
        assert isinstance(articles, list)
