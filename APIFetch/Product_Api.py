import requests

def Product_apifetch():
    url = "https://api.freeapi.app/api/v1/public/randomjokes"
    response = requests.get(url)
    apidata = response.json()

    if "success" and "data" in apidata:
        productdata = apidata["data"]
        jock_list = productdata.get("data",[])

        if not jock_list:
            raise Exception("No Joke Here")
        current = productdata.get("currentPageItems",0)
        limit = productdata.get("limit")

        for joke in jock_list:
            joke_data = {  
            "id": joke["id"],  
            "content": joke["content"],  
            "categories": joke["categories"]
            }
        jock_list.append(joke_data)
        #jokes = [{"id": joke["id"], "content": joke["content"], "categories": joke["categories"]} for joke in jock_list]
        return current,jock_list,limit

        
    else :
        raise Exception("Failed")
    

def main():
    try:
        current,jokes,limit= Product_apifetch()
        print(f"current:{current} \n Limit : {limit} ")
        print("Jokes")
        for joke in jokes:
            print(f"Id:{joke['id']}")
            print(f"Content:{joke['content']}")
            print(f"Categories: {', '.join(joke['categories']) if joke['categories'] else 'None'}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()