
#წესები
rule1 = {
    "ip_type": "any",
    "port": 23,
    "protocol": "TCP",
    "action": "DENY"
}
rule2 = {
    "ip_type": "Private",
    "port": 22,
    "protocol": "TCP",
    "action": "ALLOW"
}
rule3 = {
    "ip_type": "Public",
    "port": 22,
    "protocol": "TCP",
    "action": "DENY"
}
rule4 = {
    "ip_type": "any",
    "port": 80,
    "protocol": "TCP",
    "action": "ALLOW"
}
rule5 = {
    "ip_type": "any",
    "port": 443,
    "protocol": "TCP",
    "action": "ALLOW"
}
rule6 = {
    "ip_type": "any",
    "port": 53,
    "protocol": "UDP",
    "action": "ALLOW"
}
rules = [rule1, rule2, rule3, rule4, rule5, rule6]

#პორტის შემოწმება

port = input("enter port: ") #ცვლადში ჩნდება ტექსტად
if port.isdigit():  #ამოწმებს თუ არის რიცხვები
    port = int(port) #თუ ციფრებია ცვლადი რიცხვად გადაიქცევა
else: 
    print("invalid port" ) #თუ არა და  არ გაეშვება
    exit()
    
#პროტოკოლის შემოწმება

protocol = input("enter protocol (TCP/UDP): ").upper()
if protocol in ["TCP", "UDP"]:
    print(protocol)
else:
    print("invalid protocol")
    exit()

#IP მისამართის შემოწმება

address = input("enter IP address: ")
parts = address.split(".")

if len(parts) != 4:
    print("invalid IP")
    exit()

if not (parts[0].isdigit() and parts[1].isdigit()):
    print("invalid IP")
    exit()

first_octet = int(parts[0])
second_octet = int(parts[1])

if first_octet == 10:
    ip_type = "Private"
elif first_octet == 172 and second_octet >= 16 and second_octet <= 31:
    ip_type = "Private"
elif first_octet == 192 and second_octet == 168:
    ip_type = "Private"
else:
    ip_type = "Public"

print("IP Type: ", ip_type)

#წესების შემოწმება   
    
found = False

for rule in rules:
    if (rule["ip_type"] == "any" or rule["ip_type"] == ip_type) and rule["port"] == port and rule["protocol"] == protocol:
        print(rule["action"])
        found = True
        break

if found == False:
    print("Result: DENY")
