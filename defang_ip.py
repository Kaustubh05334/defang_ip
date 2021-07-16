def defang_ip(ip):
    d_ip = ip.split(".")
    defanged_ip= "[.]".join(d_ip)
    return defanged_ip
x= input("Enter a ip address: ")
print(defang_ip(x))