# 2.2.py

LOGFILE = "sample_auth_small.log"  

import re 
ips=[]

def simple_parser(line):
  
    if " from " in line:
        parts = line.split() 
        try:
            anchor = parts.index("from")   
            ip = parts[anchor+1]          
            return ip.strip()             

        except (ValueError, IndexError):
            return None

    return None


if __name__ == "__main__":

    with open(LOGFILE, "r") as f:
        for line in f:
            print (simple_parser(line.strip()))
    
with open('sample_auth_small.log', 'r') as f:
    for line in f:
        ip_pattern = r"\d+\.\d+\.\d+\.\d+"
        found_ips = re.findall(ip_pattern,line)
        for ip in found_ips:
            ips.append(ip)

unique_ips = set(ips)

print("Unique_ips:")
for ip in unique_ips:
    print(ip)