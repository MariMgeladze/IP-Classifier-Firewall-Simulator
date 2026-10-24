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