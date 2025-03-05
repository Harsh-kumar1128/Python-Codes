import requests

def fetch_username_api():
    url = "https://api.freeapi.app/api/v1/public/randomusers/13"
    response = requests.get(url)
    data = response.json()
    #message = data.get("message","Message not found")

    if "success" and "data" in data and "message" in data :
        user_data =data["data"]
        usesrname =user_data["login"]["username"]
        country = user_data["location"]["country"]
        dob    = user_data["dob"]["age"]
        email = user_data["email"]
        picture =user_data["picture"]["large"]
        message = data["message"]
        sucess = data["success"]
        return usesrname,country,dob,email,picture,message,sucess

    else:
        raise Exception("Failed to fetch Url data")
    

def main():
    try:
       username,country,dob,email,picture,message,sucess= fetch_username_api()
       print(f"Username : {username} \n Country : {country} \n Age : {dob} \n Email :{email} \n Picture :{picture} \n Message : {message} Success: {sucess}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()