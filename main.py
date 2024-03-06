import argparse
from payload import Payload

parser = argparse.ArgumentParser()
parser.add_argument("--linux",help="Payload targeting Linux",action="store_true")
parser.add_argument("--windows",help="Payload targeting Windows",action="store_true")
parser.add_argument("--ip",help="Reverse connection IP Adress")
parser.add_argument("--port",help="Reverse connection Port")

args = parser.parse_args()

if args.linux:
    payload = Payload(platform="Linux")
    payload.permut()
    print(payload)

    
elif args.windows:
    print("Platform: Windows")
    print("/!\ Not yet implemented /!\\")