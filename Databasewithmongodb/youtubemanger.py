from pymongo import MongoClient
from bson import ObjectId
try :
    client = MongoClient("mongodb://127.0.0.1:27017/")
    db = client["Pythondb"]
    collection =db["ytmanger"]
    db.command('ping')
    print("✅ MongoDB Connected Successfully!")
except Exception as e:
    print("Connection Failed",e)

def list_all():
    print("List of all Videos ")
    video = collection.find()
    if collection.count_documents({}) == 0:
        print("No video is here Please insert it")
    else:
        for video in video:
            print(f"ID : {video['_id']},Name : {video['name']},Time : {video['time']}")


def add_videos(name,time):
    collection.insert_one({"name":name,"time": time})
    print("Video Added Succesfully")

def update_videos(video_id,new_name,new_time):

    if not ObjectId.is_valid(video_id):
         print(" Invalid ID format! Please enter a valid 24-character ObjectId.")
         return
    rsult = collection.update_one({"_id": ObjectId(video_id)},{"$set":{"name": new_name,"time":new_time}})
    if rsult.matched_count == 0:
        print("Enter the Right video_id")
    else:
        print("Updated Successfully")

def delete_video(video_id):
    
    if not ObjectId.is_valid(video_id):
         print(" Invalid ID format! Please enter a valid 24-character ObjectId.")
         return
    rslt = collection.delete_one({"_id":ObjectId(video_id)})
    if rslt.deleted_count == 0:
        print("Enter the Right video_id")
    else:
        print("Deleted Successfully")
def main():
    while(True):
        print("\n Youtube manager list ")
        print("1. List all videos : ")
        print("2. Add videos: ")
        print("3. Updates videos :")
        print("4. Delete videos: ")
        print("5. Exit")

        choice = input("Enter your choicee : ")

        match choice:
            case '1':
                list_all()
            case '2':
                name = input("Enter your videos name : ")
                time = input("Enter your videos Time :")
                add_videos(name,time)
            case '3':
                video_id = input("Enter your video video for the update : ")
                name = input("Enter new video name : ")
                time = input("Enter your new video time : ")
                update_videos(video_id,name,time)
            case '4':
                video_id = input("Enter your video_ delete for delete : ")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid ID ")


if __name__ == "__main__":
    main()