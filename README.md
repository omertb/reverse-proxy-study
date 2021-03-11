> Before running `docker-compose up` :
```
curl -O http://tengine.taobao.org/download/tengine.tar.gz
tar -zxf tengine.tar.gz
git clone https://github.com/vozlt/nginx-module-vts.git
git clone http://github.com/yaoweibin/nginx_upstream_check_module
mv tengine-2.1.0 tengine
```

> To create your own self-signed certificates in the nginx_conf directory:
```angular2html
openssl req -x509 -sha256 -newkey rsa:2048 -keyout certificate.key -out certificate.crt -days 1024 -nodes
```