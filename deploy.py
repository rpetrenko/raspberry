#!/bin/env python
import paramiko
import os
import sys
import re


class LocalHost(object):
    def run_cmd(self, cmd):
        print(cmd)
        #TODO replace with subprocess
        os.system(cmd)


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
        print(cmd)
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

    def copy_files(self, local_path, remote_path, local_host):
        fname_zip = "{}.tar.gz".format(local_path)
        fname_remote = os.path.join(remote_path, fname_zip)
        local_host.run_cmd("tar cfz {} {}".format(fname_zip, local_path))
        sftp = self.ssh.open_sftp()
        sftp.put(fname_zip, fname_remote)
        sftp.close()
        local_host.run_cmd("rm {}".format(fname_zip))
        self._exec("tar xvzf {}".format(fname_remote))


raspi_ip = os.environ['RPI_IP'] #'rpi3.local'
username = os.environ.get('RPI_USER', 'pi')
password = os.environ['RPI_PASSWORD']
host = Host(raspi_ip, username, password)
local_host = LocalHost()

local_path, remote_path = sys.argv[1], sys.argv[2]
host.copy_files(local_path, remote_path, local_host)

