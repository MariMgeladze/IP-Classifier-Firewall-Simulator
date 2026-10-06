
address = input("enter IP address: ") #მომხმარებელს სთხოვს შეიყვანოს IP მისამართი
parts = address.split(".") #ამის შემდეგ parts ხდება IP მისამართის ცალ-ცალკე ნაწილი

if len(parts) != 4: #ამოწმებს, რომ IP მისამართი შედგება 4 ნაწილისგან
    print("არასწორი ფორმატის IP მისამართი") #თუ არა, გამოაქვს შეტყობინება
elif parts[0].isdigit(): # ეს გამორიცხავს,რომ პირველი ოქტეტი არ იყოს ციფრი
    first_octet = int(parts[0])
    second_octet = int(parts[1])
    #print(first_octet) თუ ჩავრთავთ ამ ფუნქციას,გამოიტანს ასევე პირველი ოქტეტის ციფრს
 
#ვამოწმებთ კლასებს, რომელშიც შედის IP მისამართი

    if first_octet >= 1 and first_octet <= 126:
        print("IP class is A")
    elif first_octet >= 128 and first_octet <= 191:
        print("IP class is B")
    elif first_octet >= 192 and first_octet <= 223:
        print("IP class is C")
    elif first_octet >= 224 and first_octet <= 239:
        print("IP class is D")
    elif first_octet >= 240 and first_octet <= 255:
        print("IP class is E")
    else:
        print("არასწორი ფორმატის IP მისამართი")  
        
#private and public IP მისამართის დადგენა
         
if first_octet == 10:
    print("Private IP")
elif first_octet == 172 and second_octet >= 16 and second_octet <= 31:
    print("Private IP")
elif first_octet == 192 and second_octet == 168:
    print("Private IP")
else:
    print("Public IP")    
        
          
    
    
    

