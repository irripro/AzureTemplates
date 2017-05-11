from __future__ import absolute_import, division, print_function, with_statement
import winrm, sys

#Define environment specific variables
global domain,dnsserver,username,passwd

domain = "altst.local"
dnsserver = "altstdns1st.eastus.cloudapp.azure.com"
username = "alihhussain"
passwd="2#Adamhussain"

#exampe: python dnsauto.py adda fqdn ipaddress
def addarecord(fqdn,ipadd):
	ps_script=str("dnscmd localhost /recordadd %s %s A %s" %(domain,fqdn,ipadd))
	s = winrm.Session(dnsserver, auth=(username, passwd))
	r = s.run_ps(ps_script)
#	print("The status code is: %s" %r.status_code)
#	print("The standard output is : %s" %r.std_out)


#exampe: python dnsauto.py deletea fqdn
def deletearecord(fqdn):
	ps_script=str("dnscmd localhost /recorddelete %s %s A /f" %(domain,fqdn))
	s = winrm.Session(dnsserver, auth=(username, passwd))
	r = s.run_ps(ps_script)
#	print("The status code is: %s" %r.status_code)
#	print("The standard output is : %s" %r.std_out)


#exampe: python dnsauto.py addc fqdn cname
def addcname(fqdn,cname):
	ps_script=str("dnscmd localhost /recordadd %s %s CNAME %s" %(domain,fqdn,cname))
	s = winrm.Session(dnsserver, auth=(username, passwd))
	r = s.run_ps(ps_script)
#	print("The status code is: %s" %r.status_code)
#	print("The standard output is : %s" %r.std_out)

#exampe: python dnsauto.py deletec fqdn
def deletecname(fqdn):
	ps_script=str("dnscmd localhost /recorddelete %s %s CNAME /f" %(domain,fqdn))
	s = winrm.Session(dnsserver, auth=(username, passwd))
	r = s.run_ps(ps_script)
#	print("The status code is: %s" %r.status_code)
#	print("The standard output is : %s" %r.std_out)

def main():
#   Examples
#    Usage: python dnsauto.py adda fqdn ipaddress
#    Usage: python dnsauto.py addc fqdn(No domain) cname
#    Usage: python dnsauto.py deletea fqdn
#    Usage: python dnsauto.py deletec fqdn(No domain)
    try:
        if 'adda' in sys.argv[1].lower():
            addarecord(sys.argv[2],sys.argv[3])
            print("Successful")
        elif 'deletea' in sys.argv[1].lower():
            deletearecord(sys.argv[2])
            print("Successful")
        elif 'addc' in sys.argv[1].lower():
            addcname(sys.argv[2],sys.argv[3])
            print("Successful")
        elif 'deletec' in sys.argv[1].lower():
            deletecname(sys.argv[2])
            print("Successful")
        else:
            print("You have not selected one of the valid entries to utilize this script")
            sys.exit()
            print("Unsuccessful")
    except (IndexError):
#        print("You didn't enter anything\nBelow are examples on how to use the script")
        print("Unsuccessful")
        sys.exit()


if __name__ == "__main__":
    main()

"""
from __future__ import absolute_import, division, print_function, with_statement
import winrm
ps_script=str("dnscmd dns.altst.local /recordadd altst.local test A 10.0.0.119")

s = winrm.Session('altstdns1st.eastus.cloudapp.azure.com', auth=('alihhussain', '2#Adamhussain'))
r = s.run_ps(ps_script)
print("The status code is: %s" %r.status_code)
print("The standard output is : %s" %r.std_out)
"""