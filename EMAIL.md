
## Telnet as SMTP and POP3 client
SMTP and POP3 are text based protocols to transfer email messages. We can use telnet to connect to a mail server and send and receive emails. User input lines will begin with `>>>` to denote this. The servers are on *localhost*.

### SMTP
SMTP is on localhost on port 25. We will present as valerionew.it and send an email from me@valerionew.it to user@labfir.lan.
```
$ telnet localhost 25
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
220 I'm Luke Skywalker, I'm here to Postfix you
>>> HELO valerionew.it
250 www.labfir.lan
>>> MAIL FROM:<me@valerionew.it>
250 2.1.0 Ok
>>> RCPT TO:<user@labfir.lan>
250 2.1.5 Ok
>>> DATA
354 End data with <CR><LF>.<CR><LF>
>>> Mail From: me@valerionew.it
>>> Subject: Hello World!
>>> Hello,
>>> This is my first email sent without a client
>>> .
250 2.0.0 Ok: queued as 588D48D8A
>>> QUIT
221 2.0.0 Bye
Connection closed by foreign host.
```
We successfully sent the email. Note that after the `DATA` command we entered some headers: *Mail From:*, *Subject*. These weren't actually in the SMTP protocol, they come from **RFC 822**, which is an additional standard.
### POP3
Now we will connect to the user@labfir.lan email inbox with POP3, we will use telnet on port 110.
```
$ telnet localhost 110
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
+OK Hello Jedi, may the Force be with you!
>>> USER user
+OK
>>> PASS labfir
+OK Logged in.
>>> LIST
+OK 1 message:
1 489
.
>>> RETR 1
+OK 489 octets
Return-Path: <me@valerionew.it>
X-Original-To: user@labfir.lan
Delivered-To: user@labfir.lan
Received: from valerionew.it (localhost [127.0.0.1])
	by www.labfir.lan (Postfix) with SMTP id 588D48D8A
	for <user@labfir.lan>; Thu, 27 Aug 2020 18:09:22 +0200 (CEST)
Subject: Hello World!
Message-Id: <20200827160938.588D48D8A@www.labfir.lan>
Date: Thu, 27 Aug 2020 18:09:22 +0200 (CEST)
From: me@valerionew.it

Mail From: me@valerionew.it
Hello,
This is my first email sent without a client
.
>>> DELE 1
+OK Marked to be deleted.
>>> QUIT
+OK Logging out, messages deleted.
Connection closed by foreign host.
```
We successfully got the list of the messages waiting in the inbox, retrived one email and deleted it.
