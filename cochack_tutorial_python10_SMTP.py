import smtplib

server = smtplib.SMTP('http://localhost:3000')
server.sendmail('soothsayer@example.com', 'jcaesar@example.org')

""" To: jcaesar@example.com
    From: soothsayer@example.com
"""

