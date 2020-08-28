# DNS Tools
We will learn here `nslookup` and `dig`, tools for analyzing DNS records.
## `nslookup`
Let's say we want to query the NS system to know the address of polimi.it
```
        $ nslookup polimi.it
Server:		127.0.1.1
Address:	127.0.1.1#53

Non-authoritative answer:
Name:	polimi.it
Address: 131.175.187.72

```
We can also ask `nslookup` to do a reverse query, giving it an adress and getting the name of the server. Let's reverse search the address of polimi.it we just got.
```
        $ nslookup 131.175.187.72
Server:		127.0.1.1
Address:	127.0.1.1#53

Non-authoritative answer:
72.187.175.131.in-addr.arpa	name = www.polimi.it.

Authoritative answers can be found from:

```

Let's now try to lookup a bigger website, for example yahoo.com
```
        $ nslookup yahoo.com
Server:		127.0.1.1
Address:	127.0.1.1#53

Non-authoritative answer:
Name:	yahoo.com
Address: 74.6.231.20
Name:	yahoo.com
Address: 74.6.143.26
Name:	yahoo.com
Address: 74.6.231.21
Name:	yahoo.com
Address: 98.137.11.164
Name:	yahoo.com
Address: 74.6.143.25
Name:	yahoo.com
Address: 98.137.11.163
```
Now we got 6 answers! That means that to yahoo.com there are associated six different servers. Sometimes the order of those records can change, that's load distribution made on the dns server

#### Authoritative NS lookup
We can use `nslookup` specifying the type, using `-type=NS`
```
        $ nslookup -type=NS polimi.it
Server:		127.0.1.1
Address:	127.0.1.1#53

Non-authoritative answer:
polimi.it	nameserver = ns.polimi.it.
polimi.it	nameserver = dns.cineca.it.
polimi.it	nameserver = ns2.polimi.it.

Authoritative answers can be found from:

```

## `dig`
Dig is a more advanced name server lookup tool. Let's `dig` yahoo.com. We have to specify the type of the record, here we will specify *ANY*.
```
        $ dig -t ANY yahoo.com
;; Warning: Message parser reports malformed message packet.

; <<>> DiG 9.9.5-11ubuntu1-Ubuntu <<>> -t ANY yahoo.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 29028
;; flags: qr rd ra; QUERY: 1, ANSWER: 27, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: Message has 1 extra bytes at end

;; QUESTION SECTION:
;yahoo.com.			IN	ANY

;; ANSWER SECTION:
yahoo.com.		1541	IN	SOA	ns1.yahoo.com. hostmaster.yahoo-inc.com. 2020082805 3600 300 1814400 600
yahoo.com.		1541	IN	A	74.6.231.21
yahoo.com.		1541	IN	A	74.6.231.20
yahoo.com.		1541	IN	A	74.6.143.25
yahoo.com.		1541	IN	A	98.137.11.163
yahoo.com.		1541	IN	A	74.6.143.26
yahoo.com.		1541	IN	A	98.137.11.164
yahoo.com.		1541	IN	AAAA	2001:4998:44:3507::8000
yahoo.com.		1541	IN	AAAA	2001:4998:24:120d::1:0
yahoo.com.		1541	IN	AAAA	2001:4998:24:120d::1:1
yahoo.com.		1541	IN	AAAA	2001:4998:44:3507::8001
yahoo.com.		1541	IN	AAAA	2001:4998:124:1507::f001
yahoo.com.		1541	IN	AAAA	2001:4998:124:1507::f000
yahoo.com.		1541	IN	MX	1 mta5.am0.yahoodns.net.
yahoo.com.		1541	IN	MX	1 mta7.am0.yahoodns.net.
yahoo.com.		1541	IN	MX	1 mta6.am0.yahoodns.net.
yahoo.com.		21341	IN	NS	ns4.yahoo.com.
yahoo.com.		21341	IN	NS	ns1.yahoo.com.
yahoo.com.		21341	IN	NS	ns5.yahoo.com.
yahoo.com.		21341	IN	NS	ns2.yahoo.com.

;; Query time: 19 msec
;; SERVER: 127.0.1.1#53(127.0.1.1)
;; WHEN: Fri Aug 28 12:23:27 CEST 2020
;; MSG SIZE  rcvd: 512

```
We notice we get **A** records and **AAAA** records. The first being IPv4 and the latter being IPv6. We also find the **MX** section: the mail servers, and the **NS** server, the name servers.

Dig can also be used to trace all the queries:
```
        $ dig polimi.it +trace
```

