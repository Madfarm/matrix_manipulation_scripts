class Language:
    def __init__(self, name, region, speakers, parent=None):
        self.name = name
        self.region = region
        self.speakers = speakers
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def __str__(self):
        return f"{self.name} ({self.region})"

class LanguageTree:
    def __init__(self, root):
        self.root = root

    def add_language(self, language, parent=None):
        if parent:
            parent.add_child(language)
        else:
            self.root = language

    def remove_language(self, language):
        if language == self.root:
            self.root = None
        else:
            language.parent.remove_child(language)

    def find_shortest_path(self, language1, language2):
        def find_path(start, end, path=[]):
            path = path + [start]
            if start == end:
                return path
            if start.children:
                for node in start.children:
                    if node not in path:
                        new_path = find_path(node, end, path)
                        if new_path:
                            return new_path
            return None

        return find_path(self.root, language1, [])

# Example usage
root = Language("Proto-Indo-European", "Europe", 10000)
tree = LanguageTree(root)

english = Language("English", "Europe", 1000, root)
tree.add_language(english)

french = Language("French", "Europe", 500, root)
tree.add_language(french)

spanish = Language("Spanish", "Europe", 200, root)
tree.add_language(spanish)

# Adding a new language
portuguese = Language("Portuguese", "Europe", 500, root)
tree.add_language(portuguese)

# Removing a language
tree.remove_language(french)

# Finding the shortest path from English to Spanish
path = tree.find_shortest_path(english, spanish)
for lang in path:
    print(lang)