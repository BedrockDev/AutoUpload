# AutoUpload
A Python CLI tool for uploading video to YouTube

### Flow

1. Read title from file
2. Automatically append suffixes to the title (date, name)
3. *Ask the user for title confirmation*
4. Rename latest mp4 file
5. *Ask the user for file confimation*
6. Convert mp4 file to mp3 file and add ID3 tags
7. Upload video to YouTube
8. Open mp3 file location → open edited html file → open webpage

*All tasks are syncronous*