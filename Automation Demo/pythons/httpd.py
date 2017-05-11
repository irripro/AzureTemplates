#!/usr/bin/env python
import sys, json
from fabric.api import *
from pprint import pprint

filename=sys.argv[1]

with open(filename) as data_file:    
    data = json.load(data_file)

vms=data["properties"]["outputs"]["sshCommand"]["value"]
vms1=vms.split('#',1)
vm1=vms1[0]
vm2=vms1[1]

env.hosts = open(hostname, 'r').read().replace('\n', '')
env.user = 'alihhussain'

env.key_filename = '/var/lib/jenkins/.ssh/id_rsa'
#env.combine_stderr = False
env.disable_known_hosts = True
env.output_prefix = False
env.colorize_errors = True
env.linewise = True

def installhttpd(vmtoworkon):
    conffile=str("<VirtualHost *:80>\n	ServerName www.%s\n	ServerAlias %s\n	DocumentRoot /var/www/%s/public_html\n	ErrorLog /var/log/httpd/error.log\n	CustomLog /var/log/httpd/requests.log combined	\n</VirtualHost>" %(vmtoworkon,vmtoworkon,vmtoworkon))
    with hide('everything'):
        sudo("yum update -y")
    sudo("yum -y install httpd")
    sudo("systemctl enable httpd.service")
    sudo("mkdir -p /var/www/%s/public_html" %vmtoworkon)
    sudo("chown -R %s:%s /var/www/%s/public_html" %(vmtoworkon,vmtoworkon,vmtoworkon))
    sudo("chmod -R 755 /var/www")
    run("curl -O -u 315c4187412e9cbdf0bfa7ae13c6cc949d10a970:x-oauth-basic https://raw.githubusercontent.com/alihhussain/ops/master/oss/TestWebPage/testweb.zip")
    run("unzip /home/alihhussain/testweb.zip -d /var/www/%s/public_html/" %vmtoworkon)
    run("mv /var/www/%s/public_html/index.htm /var/www/%s/public_html/index.html" %(vmtoworkon,vmtoworkon))
    run("sed -i 's#server_name#%s#g' /var/www/%s/public_html/index.html" %(vmtoworkon,vmtoworkon))
    sudo("mkdir /etc/httpd/sites-available")
    sudo("mkdir /etc/httpd/sites-enabled")
    sudo("echo 'IncludeOptional sites-enabled/*.conf' >> /etc/httpd/conf/httpd.conf")
    sudo("echo '%s' > /etc/httpd/sites-available/%s.conf" %(conffile,vmtoworkon))
    sudo("ln -s /etc/httpd/sites-available/%s.conf /etc/httpd/sites-enabled/%s.conf" %(vmtoworkon,vmtoworkon))
    sudo("service httpd stop")
    sudo("service httpd start")

if __name__ == "__main__":
    execute(installhttpd(vm1))
    execute(installhttpd(vm2))
