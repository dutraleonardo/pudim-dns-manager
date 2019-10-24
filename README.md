# pysimpledns
Simple DNS Server using Python <3

# Important resources:
This project was created based on this documentation, take a look, that's important to a better understanding about how the was created and about DNS
https://www.ietf.org/rfc/rfc1035.txt

# How to run:
Open a terminal and run
```
git clone https://github.com/dutraleonardo/pysimplesdns
cd pysimplesdns
sudo python dns.py
```
Need to run as sudo because the DNS server use port 53 (UDP port)

Open another terminal and run

```
dig pysimpledns.com @127.0.0.1
```

Voilà.
You will get a response from the DNS server.
