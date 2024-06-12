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

    def get_artifacts(self):
        return self.artifacts

    def update_artifact(self, old_artifact, new_artifact):
        index = self.artifacts.index(old_artifact)
        self.artifacts[index] = new_artifact

# Example usage
manager = ArtifactManager()

# Add artifacts
manager.add_artifact(Artifact("Ancient statue", "500 BC", "2022", "Egypt"))
manager.add_artifact(Artifact("Medieval sword", "1200 AD", "2020", "Europe"))

# Remove artifact
manager.remove_artifact(manager.artifacts[0])

# Update artifact
old_artifact = manager.artifacts[0]
new_artifact = Artifact("Ancient statue", "500 BC", "2023", "Egypt")
manager.update_artifact(old_artifact, new_artifact)

# Get all artifacts
print(manager.get_artifacts())