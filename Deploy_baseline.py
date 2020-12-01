import paramiko
import time

string_v1 = [" dp import baseline bdos set \"POC_Demo\" \\",
" -icmp_in_bps_ipv4 201798688 -icmp_out_bps_ipv4 171798688 \\",
" -tcp_in_bps_ipv4 18038861824 -tcp_out_bps_ipv4 18038861824 \\",
" -udp_in_bps_ipv4 10069803776 -udp_out_bps_ipv4 25769803776 \\",
" -udp_frag_in_bps_ipv4 6012954112 -udp_frag_out_bps_ipv4 6012954112 \\",
" -igmp_in_bps_ipv4 171798688 -igmp_out_bps_ipv4 171798688 \\",
" -tcp_syn_in_bps_ipv4 811748864 -tcp_syn_out_bps_ipv4 811748864 \\",
" -tcp_rst_in_bps_ipv4 1623497728 -tcp_rst_out_bps_ipv4 1623497728 \\",
" -tcp_ack_in_bps_ipv4 5153960448 -tcp_ack_out_bps_ipv4 5153960448 \\",
" -tcp_ack_psh_in_bps_ipv4 109521666048 -tcp_ack_psh_out_bps_ipv4 109521666048 \\",
" -tcp_ack_fin_in_bps_ipv4 811748864 -tcp_ack_fin_out_bps_ipv4 811748864 \\",
" -tcp_syn_ack_in_bps_ipv4 811748864 -tcp_syn_ack_out_bps_ipv4 811748864 \\",
" -tcp_frag_in_bps_ipv4 360777248 -tcp_frag_out_bps_ipv4 360777248 \\",
" -icmp_in_pps_ipv4 2386093 -icmp_out_pps_ipv4 2386093 \\",
" -tcp_in_pps_ipv4 60129540 -tcp_out_pps_ipv4 60129540 \\",
" -udp_in_pps_ipv4 73628008 -udp_out_pps_ipv4 73628008 \\",
" -udp_frag_in_pps_ipv4 12025908 -udp_frag_out_pps_ipv4 12025908 \\",
" -igmp_in_pps_ipv4 2386093 -igmp_out_pps_ipv4 2386093 \\",
" -tcp_syn_in_pps_ipv4 12683576 -tcp_syn_out_pps_ipv4 12683576 \\",
" -tcp_rst_in_pps_ipv4 27058296 -tcp_rst_out_pps_ipv4 27058296 \\",
" -tcp_ack_in_pps_ipv4 12884901 -tcp_ack_out_pps_ipv4 12884901 \\",
" -tcp_ack_psh_in_pps_ipv4 273804160 -tcp_ack_psh_out_pps_ipv4 273804160 \\",
" -tcp_ack_fin_in_pps_ipv4 13529148 -tcp_ack_fin_out_pps_ipv4 13529148 \\",
" -tcp_syn_ack_in_pps_ipv4 13092724 -tcp_syn_ack_out_pps_ipv4 13092724 \\",
" -tcp_frag_in_pps_ipv4 721555 -tcp_frag_out_pps_ipv4 721555 \\",
" -icmp_in_bps_ipv6 171798688 -icmp_out_bps_ipv6 171798688 \\",
" -tcp_in_bps_ipv6 18038861824 -tcp_out_bps_ipv6 18038861824 \\",
" -udp_in_bps_ipv6 25769803776 -udp_out_bps_ipv6 25769803776 \\",
" -udp_frag_in_bps_ipv6 6012954112 -udp_frag_out_bps_ipv6 6012954112 \\",
" -igmp_in_bps_ipv6 171798688 -igmp_out_bps_ipv6 171798688 \\",
" -tcp_syn_in_bps_ipv6 811748864 -tcp_syn_out_bps_ipv6 811748864 \\",
" -tcp_rst_in_bps_ipv6 1623497728 -tcp_rst_out_bps_ipv6 1623497728 \\",
" -tcp_ack_in_bps_ipv6 5153960448 -tcp_ack_out_bps_ipv6 5153960448 \\",
" -tcp_ack_psh_in_bps_ipv6 109521666048 -tcp_ack_psh_out_bps_ipv6 109521666048 \\",
" -tcp_ack_fin_in_bps_ipv6 811748864 -tcp_ack_fin_out_bps_ipv6 811748864 \\",
" -tcp_syn_ack_in_bps_ipv6 811748864 -tcp_syn_ack_out_bps_ipv6 811748864 \\",
" -tcp_frag_in_bps_ipv6 360777248 -tcp_frag_out_bps_ipv6 360777248 \\",
" -icmp_in_pps_ipv6 2386093 -icmp_out_pps_ipv6 2386093 \\",
" -tcp_in_pps_ipv6 60129540 -tcp_out_pps_ipv6 60129540 \\",
" -udp_in_pps_ipv6 73628008 -udp_out_pps_ipv6 73628008 \\",
" -udp_frag_in_pps_ipv6 12025908 -udp_frag_out_pps_ipv6 12025908 \\",
" -igmp_in_pps_ipv6 2386093 -igmp_out_pps_ipv6 2386093 \\",
" -tcp_syn_in_pps_ipv6 12683576 -tcp_syn_out_pps_ipv6 12683576 \\",
" -tcp_rst_in_pps_ipv6 27058296 -tcp_rst_out_pps_ipv6 27058296 \\",
" -tcp_ack_in_pps_ipv6 12884901 -tcp_ack_out_pps_ipv6 12884901 \\",
" -tcp_ack_psh_in_pps_ipv6 273804160 -tcp_ack_psh_out_pps_ipv6 273804160 \\",
" -tcp_ack_fin_in_pps_ipv6 13529148 -tcp_ack_fin_out_pps_ipv6 13529148 \\",
" -tcp_syn_ack_in_pps_ipv6 13092724 -tcp_syn_ack_out_pps_ipv6 13092724 \\",
" -tcp_frag_in_pps_ipv6 721555 -tcp_frag_out_pps_ipv6 721555"]

def main():

    ip = "10.213.17.52"
    username = "radware"
    password = "radware1"

    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(ip, port=22, username=username,
                            password=password,
                            look_for_keys=False, allow_agent=False)

    remote_conn = remote_conn_pre.invoke_shell()
    output = remote_conn.recv(65535)
    time.sleep(.5)
    # remote_conn.send(' dp import baseline bdos set "POC_Demo" -icmp_in_bps_ipv4 611798688 -icmp_out_bps_ipv4 171798688 \n')
    for line in string_v1:
        remote_conn.send(line)
        # print(line)
        time.sleep(0.2)
        remote_conn.send("\r")
    remote_conn.send("\r\n")
    output = remote_conn.recv(6000)
    print(output)

main()


