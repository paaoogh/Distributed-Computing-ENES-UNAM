# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#Fetching data from EONET: credentials needed in first instance   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import json
from urllib import request
import BeautifulSoup4

#days and limit of time to track
days, limit = str(input())


#These are the credentials
api = "" #credential
data_url = "https://eonet.sci.gsfc.nasa.gov/api/v2.1/events ?limit=5&days=20&source=InciWeb&status=open"
res = request.urlopen(data_url).read()

data = BeautifulSoup(res, "html.parser")
data_json=json.loads(data.text)
