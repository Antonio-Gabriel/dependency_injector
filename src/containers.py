from dependency_injector import containers, providers

from .services import ArticlesService
from .gateway import ArticleListGateway


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".endpoints"])

    config = providers.Configuration(yaml_files=["config.yml"])    

    article_service = providers.Factory(
        ArticlesService,
        timeout=config.requests.timeout,
        article_gateway=ArticleListGateway
    )
