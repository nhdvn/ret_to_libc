
### Turn off random address
```console
$ cat /proc/sys/kernel/randomize_va_space
$ sudo sysctl -w kernel.randomize_va_space=0
```

### Get /bin/sh address in env
```console
$ export MYSHELL=/bin/sh
$ ./prtenv
```

### Get libc address in runtime
```console
$ gdb -q -batch -x gdb_command ./retlib
```

### Link /bin/sh to zsh for root
```console
$ sudo ln -sf /bin/zsh /bin/sh
$ sudo ln -sf /bin/dash /bin/sh
```

[How Set-UID work](https://unix.stackexchange.com/questions/519338/why-does-the-setuid-bit-work-inconsistently)


note:
input_address = 0xffffcce0
system = 0xf7e27e10
exit = 0xf7e1b060
execv = 0xf7ea9410
setuid = 0xf7ea9bb0
sprintf = 0xf7e3bcc0
env = 0xffffd933 (/bin/sh)