# How to Build

```bash
docker build -t train_with_infer_server:1.0 .```
```

# How to run train 
```bash
docker run -v ./100_1:/app/100_1 -it -p 5000:5000 train_with_infer_server:1.0
```
