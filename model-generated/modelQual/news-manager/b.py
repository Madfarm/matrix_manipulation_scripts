class Article:
    def __init__(self, title, publication_date, content):
        self.title = title
        self.publication_date = publication_date
        self.content = content

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
us_atoday = News()
nbc_news = News()

us_atoday.create("WikiLeaks' Julian Assange to face US extradition hearing", "2024-01-01", "Julian Assange, the founder of WikiLeaks, will face an extradition hearing in the United States in 2024.")
us_atoday.create("WikiLeaks releases classified documents on US government surveillance", "2024-02-01", "WikiLeaks has released a trove of classified documents revealing the extent of US government surveillance on its citizens.")

nbc_news.create("Athing Mu sets new world record in 800m", "2024-03-01", "Athing Mu has set a new world record in the 800m at the 2024 World Athletics Championships.")
nbc_news.create("Athing Mu wins gold in 800m at 2024 Olympics", "2024-04-01", "Athing Mu has won gold in the 800m at the 2024 Summer Olympics.")

print(us_atoday.search("WikiLeaks"))  # Returns articles with WikiLeaks in the title or content
print(nbc_news.search("Athing Mu"))  # Returns articles with Athing Mu in the title or content