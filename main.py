import argparse
from payload import Payload

parser = argparse.ArgumentParser()
parser.add_argument("--linux",help="Payload targeting Linux",action="store_true")
parser.add_argument("--windows",help="Payload targeting Windows",action="store_true")
parser.add_argument("-p","--port",help="Reverse connection Port",required=True)

args = parser.parse_args()
port = int(args.port)

if (port < 4097 or port > 65535 ):
    print("Please specify a port between 4097 and 65535")
    exit(1)

if args.linux:
    payload = Payload(platform="Linux",port=port)
    payload.permut()
    print(payload)

    
elif args.windows:
    print("Platform: Windows")
    print("/!\ Not yet implemented /!\\")