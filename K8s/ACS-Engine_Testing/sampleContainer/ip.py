from fabric.api import local

response = local("""ip addr show eth0 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1""")
print(response)
