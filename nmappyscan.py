#Automate script for scan IP with nmap

value = input('Enter the file name: ')
file = open (value,"r")

content = file.readlines()
for line in content:
    IP = line.split()
    print(IP)

