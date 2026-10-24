#  IP Classifier & Firewall Simulator

ეს არის კიბერუსაფრთხოების კურსის საფინალო პროექტი, რომელიც შედგება ორი ძირითადი მოდულისგან: 
**IP მისამართების კლასიფიკაცია** და **ფაირვოლის სიმულატორი**.

##  ფუნქციონალი

### 1. IP Classifier (`block1.py`)
- IPv4 მისამართის ფორმატისა და სტრუქტურის ვალიდაცია.
- IP მისამართის კლასის დადგენა (Class A, B, C, D, E) პირველი ოქტეტის მიხედვით.
- Private vs Public IP მისამართის ტიპის განსაზღვრა (RFC 1918 სტანდარტით).

### 2. Firewall Simulator (მუშავდება...)

python block1.py


### 2. Firewall Simulator (`block2.py`) — მუშავდება...

სიმულატორი Packet Filtering Firewall-ის პრინციპზეა აგებული: თითოეულ მოთხოვნას (IP ტიპი, პორტი, პროტოკოლი) წესების სიის მიხედვით ამოწმებს და წყვეტს, ALLOW იქნება თუ DENY.

**უკვე დასრულებულია:**
- Firewall-ის წესები აღწერილია dictionary-ების სახით (`ip_type`, `port`, `protocol`, `action`)

| # | IP ტიპი | პორტი | პროტოკოლი | მოქმედება |
|---|---|---|---|---|
| 1 | any | 23 (Telnet) | TCP | DENY |
| 2 | Private | 22 (SSH) | TCP | ALLOW |
| 3 | Public | 22 (SSH) | TCP | DENY |
| 4 | any | 80 (HTTP) | TCP | ALLOW |
| 5 | any | 443 (HTTPS) | TCP | ALLOW |
| 6 | any | 53 (DNS) | UDP | ALLOW |

**დაგეგმილია:**
- წესები ერთ სიაში გაერთიანდება და ზემოდან ქვემოთ შემოწმდება (**First Match**)
- თუ არცერთი წესი არ ერგება, მოთხოვნა დაიბლოკება (**Default Deny**)
- IP-ის ტიპს (Private/Public) განსაზღვრავს IP Classifier-ის ლოგიკა
