import requests
import pandas as pd
import time

location = pd.read_csv("data/location.csv")

for i in range(190,len(location)):
    time.sleep(0.75)
    city,state,country,eu = location.iloc[i,2].split(",")

    print(city,state,country)
    try :
        # url = f"https://geocode.maps.co/search?q={adresse}"
        url = f"https://geocode.maps.co/search?q={city},{country}"

        ans = requests.get(url)

        print(ans.status_code)
        print(ans.json())
        print(ans.text)
        print(ans.content)


        lat = ans.json()[0]["lat"]
        lon = ans.json()[0]["lon"]

        location.loc[i,"lat"] = lat
        location.loc[i,"lon"] = lon

        print(location.iloc[i,:])
        location.to_csv("data/location.csv",index=False)
    except :
        pass
