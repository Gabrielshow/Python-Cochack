#internet access
#we use urllib.request for retrieving data & smtplib for sending emails

from urllib.request import urlopen

#it won't work yet
response = urlopen("http://localhost:3000")
    #the code won't work yet because response is not defined
for line in response:
    line = line.decode('utf-8')
    
    #decoding the binary data to text
    if 'EST' in line or 'EDT' in line:
        #look for Eastern time
        print(line)
        
