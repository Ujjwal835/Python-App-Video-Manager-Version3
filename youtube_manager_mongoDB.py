from pymongo import MongoClient
from bson import ObjectId

client=MongoClient("mongodb+srv://ujjwaljindal835:pymongo123@cluster0.wpxphxl.mongodb.net/")
db=client["ytmanager"]
video_collection=db["videos"]


def list_videos():
    print("*"*70)
    for video in video_collection.find():
        print(f"ID:{video['_id']}, Name:{video['name']} and Time: {video['time']}")
    print("*"*70)
def add_video(name,time):
    video_collection.insert_one({"name":name,"time":time})
    print("***** Video Added Successfully *****")

def update_video(video_id):
    video = video_collection.find_one({"_id": ObjectId(video_id)})
    if video:
        new_name=input("Enter The Updated Video Name: ")
        new_time=input("Enter The Updated Video Time: ")
        video_collection.update_one(
            {'_id': ObjectId(video_id)},
            {"$set": {"name": new_name, "time": new_time}}
        )
        print("***** Details Updated Successfully *****")
    else:
        print("Video not found.")

    
    
def delete_video(video_id):
    video = video_collection.find_one({"_id": ObjectId(video_id)})
    if video:
        video_collection.delete_one({"_id": ObjectId(video_id)})
        print("***** Video Deleted Successfully *****")
    else:
        print("Video not found.")


def main():
    while True:
        print("\n\t\t Youtube Manager App with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit App")
        choice=input("Enter Your Choice : ")
        print("\n")
        if choice=='1':
            list_videos()
        elif choice=='2':
            name=input("Enter The Video Name: ")
            time=input("Enter The Video Time: ")
            add_video(name,time)
        elif choice=='3':
            video_id=input("Enter The Video ID to Update: ")
            update_video(video_id)
        elif choice=='4':
            video_id=input("Enter The Video ID to Delete: ")
            delete_video(video_id)
        elif choice=='5':
            break
        else:
            print("Invalid Choice !!!")

if __name__=="__main__":
    main()