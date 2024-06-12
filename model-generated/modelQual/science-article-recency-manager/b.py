class Article:
    def __init__(self, name, publication_date, tags):
        self.name = name
        self.publication_date = publication_date
        self.tags = tags

class DataStore:
    def __init__(self):
        self.articles = []

    def add_article(self, article):
        self.articles.append(article)
        if len(self.articles) > 3:
            self.articles.pop(0)

    def search_articles(self, tag):
        return [article for article in self.articles if tag in article.tags]



# Create some articles
article1 = Article("Article 1", "2022-01-01", ["Science", "Technology"])
article2 = Article("Article 2", "2022-01-02", ["Science", "Biology"])
article3 = Article("Article 3", "2022-01-03", ["Technology", "Computing"])

# Add articles to the data store
data_store = DataStore()
data_store.add_article(article1)
data_store.add_article(article2)
data_store.add_article(article3)

def manage_articles(tag, article=None):
    if article:
        data_store.add_article(article)
    return data_store.search_articles(tag)

# Search for articles with the tag "Science"
print(manage_articles("Science"))
