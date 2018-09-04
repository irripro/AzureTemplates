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
export PGPASSWORD=<YourPassword>
psql --host=<YourDB>.us-east-1.rds.amazonaws.com --port=5432 --username=<YourName> --dbname=<YourDBName>
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

### AWS Default
```bash
starting vacuum...end.
transaction type: <builtin: TPC-B (sort of)>
scaling factor: 50
query mode: simple
number of clients: 10
number of threads: 2
number of transactions per client: 10000
number of transactions actually processed: 100000/100000
latency average = 7.289 ms
tps = 1371.870361 (including connections establishing)
tps = 1372.056012 (excluding connections establishing)
```