# Lab 02
We will learn socket programming, we will write the code for an UDP client and an UDP server

## Lib docs
We will use the [python socket library](https://docs.python.org/3/library/socket.html)

## `netstat`
To check if our server is running, we can use `netstat`:
```
        $ netstat -aut
Connessioni Internet attive (server e stabiliti)
Proto CodaRic CodaInv Indirizzo locale        Indirizzo remoto       Stato      
tcp        0      0 localhost:63342         *:*                     LISTEN     
tcp        0      0 *:pop3                  *:*                     LISTEN     
tcp        0      0 user-VirtualBox:domain  *:*                     LISTEN     
tcp        0      0 localhost:ipp           *:*                     LISTEN     
tcp        0      0 *:smtp                  *:*                     LISTEN     
tcp        0      0 localhost:6942          *:*                     LISTEN     
tcp6       0      0 [::]:http               [::]:*                  LISTEN     
tcp6       0      0 [::]:ftp                [::]:*                  LISTEN     
tcp6       0      0 ip6-localhost:ipp       [::]:*                  LISTEN     
tcp6       0      0 [::]:smtp               [::]:*                  LISTEN     
udp        0      0 user-VirtualBox:domain  *:*                                
udp        0      0 *:bootpc                *:*                                
udp        0      0 *:42069                 *:*                                
udp        0      0 10.0.2.15:ntp           *:*                                
udp        0      0 localhost:ntp           *:*                                
udp        0      0 *:ntp                   *:*                                
udp        0      0 *:24187                 *:*                                
udp6       0      0 [::]:29565              [::]:*                             
udp6       0      0 fe80::a00:27ff:feae:ntp [::]:*                             
udp6       0      0 ip6-localhost:ntp       [::]:*                             
udp6       0      0 [::]:ntp                [::]:*    


```
