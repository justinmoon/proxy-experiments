# Notes on `configurable-http-server`

Install requirements:

```
npm install -g configurable-http-server
pip install flask requests
```

To run `configurable-http-server` on post 5001:

```
CONFIGPROXY_AUTH_TOKEN=abc123 configurable-http-proxy --port 5001
```

To run the flask server on port 5000:

```
flask run
```

To map `/flask` to `localhost:5000/flask`

```
python proxy.py --map /flask http://localhost:5000/flask
```

To list routes:
```
python proxy.py --get
```

To delete `/flask` route:
```
python proxy.py delete /flask
```
