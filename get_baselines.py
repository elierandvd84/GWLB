import requests
import json
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def GetBaseline():
  
    #Login to vision with API
    vision_url = "https://44.233.145.252/mgmt/system/user/login"
    switchuser='radware'
    switchpassword='radware'
    myheaders={'content-type':'application/json','Accept':'*/*','Accept-Encoding':'gzip, deflate, br','Connection':'keep-alive'}
    payload={
        "username": "radware", 
        "password": "radware"
    }
    res = requests.post(vision_url,data=json.dumps(payload),verify=False,headers=myheaders,auth=(switchuser,switchpassword))
    reposne_back = res.json()
    cookie = reposne_back["jsessionid"]
    cookie_srever_format = "JSESSIONID="+cookie+";"+"JSESSIONID="+cookie

    print("Get DP 1 BDoS baselinse...\n\n")

    #Get BDoS Baselinses from DP1 
    baseline='https://44.233.145.252/mgmt/device/byip/10.10.10.56/config/getnetworktemplate?PolicyName=any&ExportConfiguration=off&ExportBaselineDNS=off&ExportBaselineBDoS=on&ExportBaselineHttpsFlood=off&ExportSigUsrProf=off&ExportTrafficFiltersProf=off&ExportAntiScanWhitelists=off&saveToDb=false&fileName=DP_MR20_POC_Demo_2020.11.26_17.03.55'
    myheaders2={'content-type':'application/json','Accept':'*/*','Accept-Encoding':'gzip, deflate, br','Connection':'keep-alive','Cookie':cookie_srever_format}
    params={"token": cookie}

    response = requests.get(baseline,data=json.dumps(payload),verify=False,params=params,headers=myheaders2)
    response_string = response.text
    print(response_string)
    return response_string

DP_Baselinse = GetBaseline()

udp_baselin = DP_Baselinse.splitlines()
udp_baselin_rate = udp_baselin[3].split()
print("\n"*3)
# print(udp_baselin_rate[1])

