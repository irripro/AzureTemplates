FROM postgres:9.6
ENV PGPASSWORD YourPassword
ENV PGHOST YourDB.us-east-1.rds.amazonaws.com
ENV PGUSERNAME YourUserName
ENV PGPORT 5432
ENV PGDBNAME example
COPY post.sh /
CMD ["/bin/bash", "/post.sh"]