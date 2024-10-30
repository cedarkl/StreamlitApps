import streamlit as st
import googleapiclient.discovery
#import googleapiclient.errors

st.title("Extract Youtube Comments App")
st.write('''
Let's listen to our customers!
''')

api_servive_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyCc5J7nR0UueeSpKHVbV3MmKlrnKPpkbvQ"

youtube = googleapiclient.discovery.build(api_servive_name, api_version, developerKey=DEVELOPER_KEY)

try:
    videoId = st.text_input("Your video ID, please: ")
    maxResults = st.text_input("The number of comments: ")
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=videoId,
        maxResults=maxResults
    )

    response = request.execute()

    for item in response['items']:
        st.write(item['snippet']['topLevelComment']['snippet']['textDisplay'])

except:
    st.write("Please enter to continue...")

# comments = []
# for item in response['items']:
#     comment = item['snippet']['topLevelComment']['snippet']
#     comments.append([
#         comment['authorDisplayName'],
#         comment['publishedAt'],
#         comment['updatedAt'],
#         comment['likeCount'],
#         comment['textDisplay']
#     ])
#
# df = pd.DataFrame(comments, columns=['author', 'published_at', 'updated_at', 'like_count', 'text'])
# print(df)
#
# df.head()