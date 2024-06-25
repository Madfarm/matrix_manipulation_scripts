from datetime import datetime

class Article:
    def __init__(self, title, publication_date, content):
        self.title = title
        self.publication_date = datetime.strptime(publication_date, '%Y-%m-%d')
        self.content = content

    def __repr__(self):
        return f"Title: {self.title} \n Published: {self.publication_date}\n Content: {self.content}\n"

class News:
    def __init__(self):
        self.articles = []

    def create(self, title, publication_date, content):
        self.articles.append(Article(title, publication_date, content))

    def read(self):
        return sorted(self.articles, key=lambda x: x.publication_date, reverse=True)

    def delete(self, title):
        self.articles = [article for article in self.articles if article.title != title]

    def search(self, keyword):
        return [article for article in self.articles if keyword in article.title or keyword in article.content]

# Usage
news = News()

# Create articles
news.create('WikiLeaks', '2024-01-01', 'This is an article about WikiLeaks.')
news.create('Julian Assange', '2024-01-02', 'This is an article about Julian Assange.')
news.create('Athing Mu', '2024-01-03', 'This is an article about Athing Mu.')

# Search for articles
wikileaks_articles = news.search('WikiLeaks')
assange_articles = news.search('Julian Assange')
athing_mu_articles = news.search('Athing Mu')

# Read articles
all_articles = news.read()
for article in all_articles:
    print(article)

# Delete an article
news.delete('Julian Assange')

# Read articles again
all_articles = news.read()
for article in all_articles:
    print(article)