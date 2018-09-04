To build and test pgbench tool

# Install tools
1. Search specific client
```bash
apt search postgresql-client
```
2. Install the client
```bash
 apt-get install postgresql-client-9.6/xenial-pgdg
```
3. Connect to Postgre Instance
```bash
psql --host=<YourDB>.us-east-1.rds.amazonaws.com --port=5432 --username=<YourName> --password --dbname=<YourDBName>
```
    *   to list DBs ```\list'''
    *   to view tables '''\dt'''
4. Setup the db
```bash
/usr/lib/postgresql/9.6/bin/pgbench --host=<YourDB>.us-east-1.rds.amazonaws.com --port=5432 --username=<YourName> -i -s 50 example
```
5. Establish baseline
```bash
/usr/lib/postgresql/9.6/bin/pgbench --host=<YourDB>.us-east-1.rds.amazonaws.com --port=5432 --username=<YourName> -c 10 -j 2 -t 10000 example
```