import requests
import json
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

#Login to vision

login = "https://10.213.17.49/mgmt/system/user/login"

switchuser='radware'
switchpassword='radware'
myheaders={'content-type':'application/json','Accept':'*/*','Accept-Encoding':'gzip, deflate, br','Connection':'keep-alive'}

payload={
    "username": "radware", 
    "password": "radware"
 }

print("test")
res = requests.post(login,data=json.dumps(payload),verify=False,headers=myheaders,auth=(switchuser,switchpassword))
reposne_back = res.json()
cookie = reposne_back["jsessionid"]


cookie_srever_format = "JSESSIONID="+cookie+";"+"JSESSIONID="+cookie


baseline='https://10.213.17.49/mgmt/device/byip/10.213.17.52/config/getnetworktemplate?PolicyName=POC_Demo&ExportConfiguration=off&ExportBaselineDNS=off&ExportBaselineBDoS=on&ExportBaselineHttpsFlood=off&ExportSigUsrProf=off&ExportTrafficFiltersProf=off&ExportAntiScanWhitelists=off&saveToDb=false&fileName=DP_MR20_POC_Demo_2020.11.26_17.03.55'
myheaders2={'content-type':'application/json','Accept':'*/*','Accept-Encoding':'gzip, deflate, br','Connection':'keep-alive','Cookie':cookie_srever_format}
params={"token": cookie}

response = requests.get(baseline,data=json.dumps(payload),verify=False,params=params,headers=myheaders2)
print(response.text)
udp_baselin = response.text.splitlines()
udp_baselin_rate = udp_baselin[3].split()
print("\n"*3)
print(udp_baselin_rate[1])

