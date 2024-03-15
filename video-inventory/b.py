class VideoManager:
    def __init__(self):
        self.videos = []

    def add_video(self, title, video_id, length, tags):
        new_video = {
            "title": title,
            "video_id": video_id,
            "length": length,
            "tags": tags
        }
        self.videos.append(new_video)
        self.videos = sorted(self.videos, key=lambda k: k['title'])

    def remove_video(self, video_id):
        self.videos = [video for video in self.videos if video['video_id'] != video_id]

    def get_sorted_by_length(self):
        return sorted(self.videos, key=lambda k: k['length'])

    def search_by_id(self, video_id):
        return [video for video in self.videos if video['video_id'] == video_id]

    def search_by_tags(self, tag):
        return [video for video in self.videos if tag in video['tags']]

# Create an instance of the VideoManager
video_manager = VideoManager()

# Add some videos
video_manager.add_video("Video1", 1, 10, ["python", "programming"])
video_manager.add_video("Video2", 2, 5, ["java", "programming"])
video_manager.add_video("Video3", 3, 7, ["python", "data science"])
video_manager.add_video("Video4", 4, 8, ["javascript", "web development"])

# Remove a video
video_manager.remove_video(2)

# Get videos sorted by length
sorted_by_length = video_manager.get_sorted_by_length()
print("Videos sorted by length:")
for video in sorted_by_length:
    print(video)

# Search for a video by id
video_id_result = video_manager.search_by_id(3)
print("\nVideo with id 3:")
print(video_id_result)

# Search for videos by tag
tag_result = video_manager.search_by_tags("python")
print("\nVideos with 'python' tag:")
for video in tag_result:
    print(video)