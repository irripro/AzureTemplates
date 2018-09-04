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

### AWS Default (db.t2.large 2vCPU 8Gib 20gig)
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

### AWS After custom parameters
```bash
starting vacuum...end.
transaction type: <builtin: TPC-B (sort of)>
scaling factor: 50
query mode: simple
number of clients: 10
number of threads: 2
number of transactions per client: 10000
number of transactions actually processed: 100000/100000
latency average = 6.845 ms
tps = 1460.931862 (including connections establishing)
tps = 1461.159404 (excluding connections establishing)

#Parameters
autovacuum                          1
autovacuum_analyze_scale_factor     0.005
autovacuum_analyze_threshold        10000
autovacuum_max_workers              35
autovacuum_naptime                  2
autovacuum_vacuum_cost_limit        7000
autovacuum_vacuum_scale_factor      0.01
autovacuum_vacuum_threshold         10000
log_min_duration_statement          600
maintenance_work_mem                131072
wal_keep_segments                   1
work_mem                            51200
```

### Azure Default (CPU Optimized 2vCPU ?GiB 24gig)
```bash
starting vacuum...end.
transaction type: <builtin: TPC-B (sort of)>
scaling factor: 50
query mode: simple
number of clients: 10
number of threads: 2
number of transactions per client: 10000
number of transactions actually processed: 100000/100000
latency average = 79.483 ms
tps = 125.813101 (including connections establishing)
tps = 125.911444 (excluding connections establishing)
```