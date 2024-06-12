class Artifact:
    def __init__(self, description, origin_date, discovery_date, location):
        self.description = description
        self.origin_date = origin_date
        self.discovery_date = discovery_date
        self.location = location

class ArtifactManager:
    def __init__(self):
        self.artifacts = []

    def add_artifact(self, artifact):
        self.artifacts.append(artifact)

    def remove_artifact(self, artifact):
        self.artifacts.remove(artifact)

    def update_artifact(self, old_artifact, new_artifact):
        index = self.artifacts.index(old_artifact)
        self.artifacts[index] = new_artifact

    def search_artifacts(self, description=None, origin_date=None, discovery_date=None, location=None):
        results = []
        for artifact in self.artifacts:
            if (description is None or artifact.description == description) and \
               (origin_date is None or artifact.origin_date == origin_date) and \
               (discovery_date is None or artifact.discovery_date == discovery_date) and \
               (location is None or artifact.location == location):
                results.append(artifact)
        return results

# Example usage:
manager = ArtifactManager()

# Add artifacts
manager.add_artifact(Artifact("Artifact 1", "1000 BC", "2024", "Italy"))
manager.add_artifact(Artifact("Artifact 2", "500 AD", "2023", "Egypt"))
manager.add_artifact(Artifact("Artifact 3", "2000 BC", "2022", "Greece"))

# Search artifacts
results = manager.search_artifacts(description="Artifact 1")
for artifact in results:
    print(artifact.description, artifact.origin_date, artifact.discovery_date, artifact.location)