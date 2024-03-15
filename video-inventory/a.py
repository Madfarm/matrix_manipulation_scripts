class Video:
    def __init__(self, title, video_id, length, tags):
        self.title = title
        self.video_id = video_id
        self.length = length
        self.tags = tags

class VideoManager:
    def __init__(self):
        self.videos = []

    def add_video(self, title, video_id, length, tags):
        new_video = Video(title, video_id, length, tags)
        self.videos.append(new_video)
        self.videos.sort(key=lambda x: x.title)

    def remove_video(self, video_id):
        self.videos = [video for video in self.videos if video.video_id != video_id]

    def get_sorted_by_length(self):
        return sorted(self.videos, key=lambda x: x.length)

    def search_by_id(self, video_id):
        return [video for video in self.videos if video.video_id == video_id]

    def search_by_tag(self, tag):
        return [video for video in self.videos if tag in video.tags]

# Create a new video manager
manager = VideoManager()

# Add some videos
manager.add_video('Video1', 1, 10, ['python', 'coding'])
manager.add_video('Video2', 2, 5, ['python', 'test'])
manager.add_video('Video3', 3, 8, ['coding', 'test'])

# Print all videos
for video in manager.videos:
    print(f'Title: {video.title}, ID: {video.video_id}, Length: {video.length}, Tags: {video.tags}')

print("---------------------------------")

# Remove a video
manager.remove_video(2)

# Print all videos
for video in manager.videos:
    print(f'Title: {video.title}, ID: {video.video_id}, Length: {video.length}, Tags: {video.tags}')

print("---------------------------------")

# Get videos sorted by length
sorted_videos = manager.get_sorted_by_length()
for video in sorted_videos:
    print(f'Title: {video.title}, ID: {video.video_id}, Length: {video.length}, Tags: {video.tags}')

print("---------------------------------")

# Search for a video by id
video_id = 1
found_videos = manager.search_by_id(video_id)
for video in found_videos:
    print(f'Title: {video.title}, ID: {video.video_id}, Length: {video.length}, Tags: {video.tags}')

print("---------------------------------")

# Search for videos by tag
tag = 'coding'
tagged_videos = manager.search_by_tag(tag)
for video in tagged_videos:
    print(f'Title: {video.title}, ID: {video.video_id}, Length: {video.length}, Tags: {video.tags}')