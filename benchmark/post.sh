#!/bin/bash
/usr/lib/postgresql/9.6/bin/pgbench --host $PGHOST --port $PGPORT --username $PGUSERNAME -c 10 -j 2 -t 10000 $PGDBNAME