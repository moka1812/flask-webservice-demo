This webservice response header data in json format

Example:

```json
{"Host": "68.183.231.138:5000", "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Client IP": "14.186.65.95"}
```

Event log to global.log


Build service with docker:

```bash
docker build -t webservice:latest . 
```

After the build completes, run the container with command:
```
docker run -d -p 5000:5000 flask-tutorial
```


Deployed on server IP 68.183.231.138

Can run test on this server:
```bash
curl 68.183.231.138:5000
```

