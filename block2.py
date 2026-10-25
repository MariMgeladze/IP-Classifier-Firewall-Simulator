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
port = input("enter port: ") #ცვლადში ჩნდება ტექსტად
if port.isdigit():  #ამოწმებს თუ არის რიცხვები
    port = int(port) #თუ ციფრებია ცვლადი რიცხვად გადაიქცევა
else: 
    print("invalid port" ) #თუ არა და  არ გაეშვება
    

protocol = input("enter protocol (TCP/UDP): ").upper()
if protocol in ["TCP", "UDP"]:
    print(protocol)
else:
    print("invalid protocol")
    

