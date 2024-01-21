#!/usr/bin/python3

from pathlib import Path

# LOAD CONFIG FILES

path = Path(__file__).parent

# envPath = str(path.joinpath('.env.example'))
# envFile = open(envPath, 'r', encoding='utf-8')
# env = envFile.read()

# INPUT: OUTBOUND_HOST

outbound_host = input("Server OUTBOUND_HOST:\n")
if outbound_host == '':
    outbound_host = '1.1.1.1'

# INPUT: INBOUND_PORT

inbound_port = input(f"Server INBOUND_PORT:\n")
if inbound_port == '':
    inbound_port = "1000"

# INPUT: OUTBOUND_PORT

outbound_port = input(f"Server OUTBOUND_PORT:\n")
if outbound_port == '':
    outbound_port = "1000"
    


# SAVE ENV FILE
envContent = f"INBOUND_PORT={inbound_port}\nOUTBOUND_PORT={outbound_port}\nOUTBOUND_HOST={outbound_host}\n"
envPath = str(path.joinpath('.env'))
open(envPath, 'w', encoding='utf-8').write(envContent)

# PRINT OUT RESULT

print('Done!')
