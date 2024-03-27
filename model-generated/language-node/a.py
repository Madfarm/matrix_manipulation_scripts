class LanguageNode:
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

    def get_ancestors(self):
        ancestors = []
        current_node = self
        while current_node.parent:
            ancestors.append(current_node.parent)
            current_node = current_node.parent
        return ancestors

    def get_descendants(self):
        descendants = []
        stack = [self]
        while stack:
            current_node = stack.pop(0)
            descendants.append(current_node)
            stack.extend(current_node.children)
        return descendants

# Create a root node (the ancestor of all languages)
root = LanguageNode("Proto-Human", "Earth", 7900000000)

# Create some languages
english = LanguageNode("English", "Europe", 800000000, root)
french = LanguageNode("French", "Europe", 76000000, root)
german = LanguageNode("German", "Europe", 93000000, root)
spanish = LanguageNode("Spanish", "America", 489000000, root)

# Add them as children of the root node
root.add_child(english)
root.add_child(french)
root.add_child(german)
root.add_child(spanish)

# Create some more languages
american_english = LanguageNode("American English", "North America", 330000000, english)
british_english = LanguageNode("British English", "Europe", 67000000, english)
canadian_french = LanguageNode("Canadian French", "North America", 8000000, french)
swiss_german = LanguageNode("Swiss German", "Europe", 200000, german)

# Add them as children of their respective parent nodes
english.add_child(american_english)
english.add_child(british_english)
french.add_child(canadian_french)
german.add_child(swiss_german)

# Remove a language
root.remove_child(spanish)

# Get ancestors of a language
ancestors = american_english.get_ancestors()
for ancestor in ancestors:
    print(ancestor.name)

# Get descendants of a language
descendants = root.get_descendants()
for descendant in descendants:
    print(descendant.name)