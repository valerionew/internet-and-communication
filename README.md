# Fundamentals of Communications and Internet course
My notes and scripts for the Fondamenti di Comunicazione e Internet (fundamentals of communications and internet) course of prof. Capone at Politecnico di Milano.

# Tools learned in the course

## Telnet as HTTP/1.0 client
Telnet can be used as an HTTP client to make HTTP requests, as follows. To make a valid HTTP/1.0 request, it is sufficient to make the GET request, as follows, where `>>>` indicates a line written by user, it is not to be written in the console.  
An **empty row** indicates that the request is over.

```
$ telnet localhost 80
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
>>> GET /testpage.html HTTP/1.0
>>> 
``` 
<details>
  <summary>See response page</summary>
  
```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
	<title> RCI Test Page </title>
	<meta name="author" content="docente rci"/>
	<meta name="description" content="Pagina di prova per lo studio del protocollo HTTP - Corso RCI"/>
	<link rel="stylesheet" type="text/css" href="style_rci.css">
</head>

<body>
<div class="striscione">

<table class="tabella">
<tr>
	<td class="colonna_img">
		<img src="img/logo-antlab.png" width="100" height="100" border="0" alt="LOGO_ANTLAB">
	</td>
	<td class="colonna_titolo">
		<h1>
			Corso di Reti di Comunicazione e Internet
		</h1>
	</td>
	<td class="colonna_img">
		<img src="img/logo_poli_small.png" width="100" height="98" border="0" alt="LOGO_POLIMI" align="right">
	</td>
</tr>
</table>

</div>

<br><br><br><br>

<div class="box">

Questa e' una pagina di prova per testare il protocollo HTTP.<br>
Contiene del testo e delle immagini.<br>
<br><br>

</div>

</body>
</html>
Connection closed by foreign host.
```
</details>

## Telnet as HTTP/1.1 client
Telnet can also be used as a client for HTTP/1.1, but the previous request is not longer valid. Instead, HTTP/1.1 requires the client to specify the host as a header line, as follows:

```
$ telnet localhost 80
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
>>> GET /testpage.html HTTP/1.1
>>> Host: localhost
>>> 
HTTP/1.1 200 OK
Date: Fri, 14 Aug 2020 13:30:38 GMT
Server: Apache/2.4.12 (Ubuntu)
Last-Modified: Thu, 17 Mar 2016 16:10:39 GMT
ETag: "3fb-52e40df1cd8ac"
Accept-Ranges: bytes
Content-Length: 1019
Vary: Accept-Encoding
Content-Type: text/html
``` 
<details>
  <summary>See response page</summary>
  
```html


<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
	<title> RCI Test Page </title>
	<meta name="author" content="docente rci"/>
	<meta name="description" content="Pagina di prova per lo studio del protocollo HTTP - Corso RCI"/>
	<link rel="stylesheet" type="text/css" href="style_rci.css">
</head>

<body>
<div class="striscione">

<table class="tabella">
<tr>
	<td class="colonna_img">
		<img src="img/logo-antlab.png" width="100" height="100" border="0" alt="LOGO_ANTLAB">
	</td>
	<td class="colonna_titolo">
		<h1>
			Corso di Reti di Comunicazione e Internet
		</h1>
	</td>
	<td class="colonna_img">
		<img src="img/logo_poli_small.png" width="100" height="98" border="0" alt="LOGO_POLIMI" align="right">
	</td>
</tr>
</table>

</div>

<br><br><br><br>

<div class="box">

Questa e' una pagina di prova per testare il protocollo HTTP.<br>
Contiene del testo e delle immagini.<br>
<br><br>

</div>

</body>
</html>
```
</details>

This time, as we are using HTTP/1.1, the connection is not closed when the transaction is over, therefore is possible to make more requests, for example requesting the `.png` images embedded in the page:

```
>>> GET /img/logo-antlab.png HTTP/1.1
>>> Host: localhost
>>> 
HTTP/1.1 200 OK
Date: Fri, 14 Aug 2020 13:31:03 GMT
Server: Apache/2.4.12 (Ubuntu)
Last-Modified: Thu, 17 Mar 2016 16:10:39 GMT
ETag: "7832-52e40df1cc90a"
Accept-Ranges: bytes
Content-Length: 30770
Content-Type: image/png

<continues with the binary data>
```

## cURL
*cURL* is a command line tool useful to interact with URL identified resources, such as web pages and their assets. This tool greatly simplifies page downloading, as it is no longer required to manually write the HTTP request.

To download a webpage with cURL we just do:
```
$ curl localhost/testpage.html
``` 
<details>
  <summary>See response page</summary>
  
```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
	<title> RCI Test Page </title>
	<meta name="author" content="docente rci"/>
	<meta name="description" content="Pagina di prova per lo studio del protocollo HTTP - Corso RCI"/>
	<link rel="stylesheet" type="text/css" href="style_rci.css">
</head>

<body>
<div class="striscione">

<table class="tabella">
<tr>
	<td class="colonna_img">
		<img src="img/logo-antlab.png" width="100" height="100" border="0" alt="LOGO_ANTLAB">
	</td>
	<td class="colonna_titolo">
		<h1>
			Corso di Reti di Comunicazione e Internet
		</h1>
	</td>
	<td class="colonna_img">
		<img src="img/logo_poli_small.png" width="100" height="98" border="0" alt="LOGO_POLIMI" align="right">
	</td>
</tr>
</table>

</div>

<br><br><br><br>

<div class="box">

Questa e' una pagina di prova per testare il protocollo HTTP.<br>
Contiene del testo e delle immagini.<br>
<br><br>

</div>

</body>
</html>
```
</details>

To get from cURL only the head of the request, we can use
```
$ curl --head localhost/testpage.html
HTTP/1.1 200 OK
Date: Fri, 14 Aug 2020 13:41:49 GMT
Server: Apache/2.4.12 (Ubuntu)
Last-Modified: Thu, 17 Mar 2016 16:10:39 GMT
ETag: "3fb-52e40df1cd8ac"
Accept-Ranges: bytes
Content-Length: 1019
Vary: Accept-Encoding
Content-Type: text/html
```

## Telnet as SMTP and POP3 clienlab
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
