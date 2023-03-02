## Ubuntu Server - 20.04 (Extras)

This file contains guides to deploy project to a (Ubuntu Server)

### Enable remote access to database via SSL

-   To enable ssl
>   It needs certbot implementation
```bash
sudo cp /etc/letsencrypt/live/#SERVER_NAME#/cert.pem /etc/postgresql/<PG_VERSION>/main/server.crt
sudo cp /etc/letsencrypt/live/#SERVER_NAME#/privkey.pem /etc/postgresql/<PG_VERSION>/main/server.key
sudo chown postgres:postgres /etc/postgresql/<PG_VERSION>/main/server.crt /etc/postgresql/<PG_VERSION>/main/server.key
sudo chmod 400 /etc/postgresql/<PG_VERSION>/main/server.crt /etc/postgresql/<PG_VERSION>/main/server.key
```

```bash
sudo vim /etc/postgresql/<PG_VERSION>/main/postgresql.conf
-- ssl = on
-- ssl_cert_file = '/etc/postgresql/<PG_VERSION>/main/server.crt'
-- ssl_key_file = '/etc/postgresql/<PG_VERSION>/main/server.key'
```

```bash
sudo vim /etc/postgresql/<PG_VERSION>/main/pg_hba.conf
-- hostssl    all             all             0.0.0.0/0          md5
```

### References

-   Gunicorn-nginx tutorial [https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04#creating-systemd-socket-and-service-files-for-gunicorn](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04#creating-systemd-socket-and-service-files-for-gunicorn)
-   PostgreSQL SSL [https://www.vultr.com/docs/use-ssl-encryption-with-postgresql-on-ubuntu-20-04/](https://www.vultr.com/docs/use-ssl-encryption-with-postgresql-on-ubuntu-20-04/)
-   Increase storage EC2 [https://medium.com/@m.yunan.helmy/increase-the-size-of-ebs-volume-in-your-ec2-instance-3859e4be6cb7] (https://medium.com/@m.yunan.helmy/increase-the-size-of-ebs-volume-in-your-ec2-instance-3859e4be6cb7)

### See also

-   [AWS Code Deploy](222_code_deploy.md)