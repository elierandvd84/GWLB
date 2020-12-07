import requests
import paramiko
import time
import json
import math
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

DP1_IP = "10.10.10.56"
Global_dp_ip = "44.239.210.66"
Global_dp_ip2 = "44.237.142.246"

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

def CalculateBasline(baseline_output,number_of_devices,vector):
    base_list = baseline_output.splitlines()
    
    #print(baseline_output)
    if vector == "icmp":
        value = base_list[1].split()
        in_icmp = int(value[1])/number_of_devices
        out_icmp = int(value[3])/number_of_devices
        icmp_threhsold_in = math.floor(in_icmp)
        icmp_threhsold_out = math.floor(out_icmp)
        base_list[1] = " -icmp_in_bps_ipv4 " + \
            str(icmp_threhsold_in)+" -icmp_out_bps_ipv4 " + str(icmp_threhsold_out)+" \\"
        #print(base_list)
        return base_list

    if vector == "udp":
        value = base_list[3].split()
        in_udp = int(value[1])/number_of_devices
        out_in_udp = int(value[3])/number_of_devices
        udp_threhsold_in = math.floor(in_udp)
        udp_threhsold_out = math.floor(out_in_udp)
        base_list[3] = " -udp_in_bps_ipv4 " + \
            str(udp_threhsold_in)+" -udp_out_bps_ipv4 " + str(udp_threhsold_out)+" \\"
        #print(base_list)
        return base_list

def UpdateDPBaseline(baseline_template,dp_ip):
 
    username = "radware"
    password = "radware123"

    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(dp_ip, port=22, username=username,
                            password=password,
                            look_for_keys=False, allow_agent=False)

    remote_conn = remote_conn_pre.invoke_shell()
    output = remote_conn.recv(65535)
    time.sleep(.5)
    for line in baseline_template:
        remote_conn.send(line)
        # print(line)
        time.sleep(0.2)
        remote_conn.send("\r")
    remote_conn.send("\r\n")
    output = remote_conn.recv(6000)
    #remote_conn.close()
    print(output)
    print("\n\n")


def configureDpBaseline(dp_list,base_temp):
    
    for ip in range(len(dp_list)):
        print("configure DP: "+str(dp_list[ip])+"\n\n\n")
        #print(base_temp)
        time.sleep(2)
        UpdateDPBaseline(base_temp, dp_list[ip])


dp_list = [Global_dp_ip, Global_dp_ip2]
DP_Baselinse = GetBaseline()
print("\n"*3)
base_template = CalculateBasline(DP_Baselinse,2,"udp")
configureDpBaseline(dp_list, base_template)
# UpdateDPBaseline(base_template)
