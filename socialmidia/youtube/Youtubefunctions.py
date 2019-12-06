from youtube_transcript_api import  YouTubeTranscriptApi

def getSubtitle(id, languages):
    video = YouTubeTranscriptApi.get_transcript(id, languages)
    return video
