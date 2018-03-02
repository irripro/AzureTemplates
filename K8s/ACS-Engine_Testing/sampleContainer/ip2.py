from fabric.api import local

output = str(local("""ip -o -4 a | awk '$2 == "eth0" { gsub(/\/.*/, "", $4); print $4 }'""", capture=True))
print(output)
