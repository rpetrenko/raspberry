#!/bin/env python
import paramiko
import os
import sys


class Host(object):
    def __init__(self, ip, username, password, connect=True):
        self.ip = ip
        self.username = username
        self.password = password
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if connect:
            self.connect()

    def connect(self):
        self.ssh.connect(self.ip,
                         username=self.username,
                         password=self.password)

    def _exec(self, cmd, sudo=None):
        if sudo:
            cmd = "sudo -S -p '' {}".format(cmd)
        sin, sout, serr = self.ssh.exec_command(cmd)
        if sudo:
            sin.write(self.password + "\n")
            sin.flush()
        rc = sout.channel.recv_exit_status()
        se = serr.readlines()
        so = sout.readlines()
        return rc, se, so

    def hostname(self):
        rc, se, so = self._exec("hostname")
        return so[0]

    def disconnect(self):
        self.ssh.close()

    def copy_files(self, local_path, remote_path):
        sftp = self.ssh.open_sftp()
        remote_home = "/home/pi/"

        for path, dirs, files in os.walk(local_path):
            for f in files:
                fname = os.path.join(path, f)
                fname_remote = os.path.join(remote_home, f)
                sftp.put(fname, fname_remote)
                if 'bin/' in remote_path:
                    self._exec("chmod +x {}".format(fname_remote))
                self._exec("mv {} {}".format(fname_remote, remote_path),
                           sudo=True)
        sftp.close()


raspi_ip = os.environ['RPI_IP'] #'rpi3.local'
username = os.environ.get('RPI_USER', 'pi')
password = os.environ['RPI_PASSWORD']
host = Host(raspi_ip, username, password)

local, remote = sys.argv[1], sys.argv[2]
host.copy_files(local, remote)

