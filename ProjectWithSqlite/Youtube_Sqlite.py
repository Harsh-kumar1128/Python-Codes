import sqlite3
conn = sqlite3.connect("youtube_videos.db")
cursor = conn.cursor()
cursor.execute(''' 
        create table if not exists videos(
               id integer primary key,
               name text not null,
               time text not null)
''')

def list_all_video():
    cursor.execute("select * from videos")
    videos = cursor.fetchall()

    if not videos :
        print("Video Not Found !")
    else :
        for ID,Name,Time in videos:
            print(f"Id: {ID}, Name: {Name}, Time: {Time}")
            print("*" * 70)
        
         
def add_video(name,time):
    cursor.execute("insert into videos (name,time) values (?,?)",(name,time))
    print("Successfully Added Your Video ")
    conn.commit()

def update_video(video,new_name,new_time):
    if cursor.fetchone() is None:
        print("No Video is Found!")
    else :
         cursor.execute("update videos set name = ?, time = ? where id = ? ",(new_name,new_time,video))
         print("Successfully Update Your Video ")
         conn.commit()

#def delete_video(video):
    #cursor.execute("delete from videos where id = ? ",(video,))
    #print("Successfully Deleted Your Video ")
    #conn.commit()

def delete_video(video_id):
    cursor.execute("SELECT * FROM videos WHERE id = ?", (video_id,))
    if cursor.fetchone() is None:
        print("Video not found!")
        return
    
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    print("Successfully Deleted Your Video")

    # Renumbering IDs sequentially
    cursor.execute("CREATE TEMP TABLE videos_temp AS SELECT name, time FROM videos")
    cursor.execute("DELETE FROM videos")
    cursor.execute("INSERT INTO videos (name, time) SELECT name, time FROM videos_temp")
    cursor.execute("DROP TABLE videos_temp")

    conn.commit()


def main():
    while True:
        print("\n Youtube Manger with Sqlite3 ")
        print("1. List all videos  ")
        print("2. Add videos ")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit App")
        
        print("*" * 70)

        choice = input("Enter your choice : ")

        if choice == '1':
            list_all_video()
        elif choice == '2':
            name = input("Enter the Video Name : ")
            time = input("Enter the Video Time : ")
            add_video(name,time)       
        elif choice == '3':
            video = input("Enter the Video ID for the Update : ")
            name = input("Enter the Video Name : ")
            time = input("Enter the Video Time : ")
            update_video(video,name,time)
        elif choice == '4':
            video = input("Enter the Video ID for the Delete : ")
            delete_video(video)
        elif choice == '5':
            break
        else :
            print("Invalid Choice")
    conn.close()



    




if __name__ == "__main__":
    main()