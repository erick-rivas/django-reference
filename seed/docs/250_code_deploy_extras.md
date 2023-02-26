## Route53 migration

### From GoDaddy

* Go to Amazon Route53 service and create a hosted zone with your domain name. Then click on NS record and copy all of them.
* In GoDaddy, go to Nanage DNS in your domain and change Nameservers with Route53 instead.
* Create a subdomain, typing `www` in subdomain and `<domain>` in ip fields, and selecting CNAME in record type.

### Subdomain creation

* Click on Create Record.
* Select Record Type (A for IPV4, AAAA for IPV6, CNAME for domains, etc.).
* In value, type ip or domain you want to redirect.