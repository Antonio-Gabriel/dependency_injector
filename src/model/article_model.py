from collections import namedtuple


ArticleModel = namedtuple(
    "ArticleModel", 
    """
      id 
      title 
      url
      imageUrl
      newsSite
      summary
      publishedAt
      updatedAt
    """
    )
