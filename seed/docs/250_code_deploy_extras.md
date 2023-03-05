## Route53 migration

### From GoDaddy

* Go to Amazon Route53 service and create a hosted zone with your domain name. Then click on NS record and copy all of them. Looks like: ns-xxxx.awsdns-xx.org. ns-xxxx.awsdns-xx.co.uk. ns-xxx.awsdns-xx.com. ns-xxx.awsdns-xx.net.
* In GoDaddy, go to Nanage DNS in your domain and click in Change Nameservers button, select "Enter my own nameservers (advanced)" and paste all Route53 NS copied previously.

### Subdomain creation

* Click on Create Record.
* Select Record Type (A for IPV4, AAAA for IPV6, CNAME for domains, etc.).
* In value, type ip or domain you want to redirect.