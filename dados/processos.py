import socket               # Import socket module
import netifaces

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    My_ip=s.getsockname()[0]
    s.close()
    return My_ip


def main():
    #print(netifaces.interfaces())

    for i in netifaces.interfaces():
        try:
            print("IP Address: ", netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
            print("Máscara de subrede: ", netifaces.ifaddresses(i)[netifaces.AF_INET][0]['netmask'])
            print("Gateway: ", netifaces.gateways()['default'][netifaces.AF_INET][0])
            print("\n")

        except:pass

main()

