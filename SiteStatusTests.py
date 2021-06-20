import requests
import Constants

def IsSiteOnline(siteURL):
    response = requests.get(siteURL,timeout=10)
    
    if response.status_code==200:
        return True     
    else:
        return False

if IsSiteOnline(Constants.BASE_URL)== True:
    print('Website is online')
else:
    print('Website is not online')

