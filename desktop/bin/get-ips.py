#!/usr/bin/env python
import subprocess
import re

proc = subprocess.Popen(["ip", "addr", "show"],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)

stdout, stderr = proc.communicate()

if stderr:
    raise Exception("cannot get ips with [ip addr show]")
stdout = stdout.decode('utf-8')
interfaces = {}
name = None
ip = None
for l in stdout.split("\n"):
    if l and l[0].isdigit():
        m = re.search(r'^\d:\s+(\S+)\:\s+', l)
        if m:
            name = m.groups()[0]
    if name:
        m = re.search(r'inet\s+([\d\.]+)\/', l)
        if m:
            ip = m.groups()[0]
            interfaces[name] = ip
            name = None

for k, v in interfaces.items():
    print("{:<10} {}".format(k, v))