# YouTube Manager Application with MongoDB

This is a Python application that allows users to manage their YouTube videos using a MongoDB database. Users can perform CRUD (Create, Read, Update, Delete) operations on their videos through a simple command-line interface.

## Requirements

- Python 3.x
- pymongo library (install using `pip install pymongo`)

## Setup

1. Install Python 3.x if you haven't already.
2. Install the pymongo library using `pip install pymongo`.
3. Clone this repository to your local machine.

## Usage

1. Run the `youtube_manager_mongoDB.py` file using Python.
2. Follow the prompts to perform various operations:
   - List Videos: View all videos in the database.
   - Add Videos: Add a new video to the database.
   - Update Videos: Update the details of an existing video.
   - Delete Videos: Delete a video from the database.
   - Exit App: Terminate the application.

## Notes

- Video IDs are represented by MongoDB ObjectId.
- Each video has a name and a time field.
- Video details can be updated by providing the video ID.
- Videos can be deleted by providing the video ID.

## Contributors

- Ujjwal Jindal-ujjwaljindal835@gmail.com

Feel free to contribute to this project by forking the repository and submitting pull requests with improvements or additional features.
