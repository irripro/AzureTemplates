#!/usr/bin/env python
from fabric.api import *

env.hosts = open('vmname.txt', 'r').read().replace('\n', '')
env.user = 'alihhussain'

env.key_filename = '/var/lib/jenkins/.ssh/id_rsa'
#env.combine_stderr = False
env.disable_known_hosts = True
env.output_prefix = False
env.colorize_errors = True
env.linewise = True

domain=env.hosts
domain=domain.split('.',1)
domain=domain[0]

conffile=str("<VirtualHost *:80>\n	ServerName www.%s\n	ServerAlias %s\n	DocumentRoot /var/www/%s/public_html\n	ErrorLog /var/log/httpd/error.log\n	CustomLog /var/log/httpd/requests.log combined	\n</VirtualHost>" %(env.hosts,env.hosts,env.hosts))

def precheck():
    with hide('everything'):
        sudo("yum update -y")

def installhttpd():
    sudo("yum -y install httpd")
    sudo("systemctl enable httpd.service")
    sudo("mkdir -p /var/www/%s/public_html" %env.hosts)
    sudo("chown -R %s:%s /var/www/%s/public_html" %(env.user,env.user,env.hosts))
    sudo("chmod -R 755 /var/www")
    run("curl -O -u dd418d1618849ca321b6244cc11070344f01dcb8:x-oauth-basic https://raw.githubusercontent.com/alihhussain/ops/master/oss/TestWebPage/testweb.zip")
    run("unzip /home/alihhussain/testweb.zip -d /var/www/%s/public_html/" %env.hosts)
    run("mv /var/www/%s/public_html/index.htm /var/www/%s/public_html/index.html" %(env.hosts,env.hosts))
    run("sed -i 's#server_name#%s#g' /var/www/%s/public_html/index.html" %(env.hosts,env.hosts))
    sudo("mkdir /etc/httpd/sites-available")
    sudo("mkdir /etc/httpd/sites-enabled")
    sudo("echo 'IncludeOptional sites-enabled/*.conf' >> /etc/httpd/conf/httpd.conf")
    sudo("echo '%s' > /etc/httpd/sites-available/%s.conf" %(conffile,env.hosts))
    sudo("ln -s /etc/httpd/sites-available/%s.conf /etc/httpd/sites-enabled/%s.conf" %(env.hosts,env.hosts))
    sudo("service httpd stop")
    sudo("service httpd start")

if __name__ == "__main__":
    execute(precheck)
    execute(installhttpd)
