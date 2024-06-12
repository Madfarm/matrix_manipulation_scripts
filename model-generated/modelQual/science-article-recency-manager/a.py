class ScienceArticle:
    def __init__(self, name, publication_date, tags):
        self.name = name
        self.publication_date = publication_date
        self.tags = tags

class ScienceArticleManager:
    def __init__(self):
        self.articles = []

    def add_article(self, article):
        self.articles.append(article)
        self.articles.sort(key=lambda x: x.publication_date)
        if len(self.articles) > 3:
            self.articles.pop(0)

    def search_articles(self, tag):
        return [article for article in self.articles if tag in article.tags]

# Example usage:
manager = ScienceArticleManager()

article1 = ScienceArticle("Article 1", "2022-01-01", ["tag1", "tag2"])
article2 = ScienceArticle("Article 2", "2022-01-02", ["tag2", "tag3"])
article3 = ScienceArticle("Article 3", "2022-01-03", ["tag1", "tag3"])

manager.add_article(article1)
manager.add_article(article2)
manager.add_article(article3)

print(manager.search_articles("tag1"))  # Output: [Article 1, Article 3]
print(manager.search_articles("tag2"))  # Output: [Article 1, Article 2]
print(manager.search_articles("tag3"))  # Output: [Article 2, Article 3]