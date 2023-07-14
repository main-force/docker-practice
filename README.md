# 과제5

# Build Images

## Build print_hello_service Image

```bash
docker build -t print_hello_service:1.0.0 -f ./Dockerfile_print_hello_service .
```

![스크린샷 2023-07-13 오후 10.34.31.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/099e048a-20b1-4fe6-a92a-b42a5fe4fdc3/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-07-13_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_10.34.31.png)

## Build print_bye_service Image

```bash
docker build -t print_bye_service:1.0.0 -f ./Dockerfile_print_bye_service .
```

![스크린샷 2023-07-13 오후 10.35.42.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/458fd7bf-aed0-4248-b3c6-92ef16d68bd8/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-07-13_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_10.35.42.png)

# Run Containers

## Run print_hello_service Container

```bash
docker run -v ./shared:/app/shared -it print_hello_service:1.0.0
```

### Expected Output

![스크린샷 2023-07-13 오후 10.39.28.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ff3c5376-480e-46a0-86ed-f833a699dd41/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-07-13_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_10.39.28.png)

## Run print_bye_service Container

```bash
docker run -v ./shared:/app/shared -p 8888:8888 -it print_bye_service:1.0.0
```

![스크린샷 2023-07-13 오후 11.11.32.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/002b600a-9fa2-4b01-8979-405f9633bbc2/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-07-13_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_11.11.32.png)

### Expected Output

![스크린샷 2023-07-13 오후 11.12.33.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bc8f7258-78ae-428a-9dad-c77339dd4384/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-07-13_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_11.12.33.png)

# Troubleshoots

## Ports are not available

```bash
mainforce@gimjulyeog-ui-MacBookAir-16824 assignment_3 % docker run -v ./shared:/app/shared -p 5000:5000 -it print_bye_service:1.0.0
docker: Error response from daemon: Ports are not available: exposing port TCP 0.0.0.0:5000 -> 0.0.0.0:0: listen tcp 0.0.0.0:5000: bind: address already in use.
```

### Solution

`lsof` 명령어를 통해 점유하는 프로세스 번호 찾기

```bash
lsof -i tcp:5000

COMMAND   PID      USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
ControlCe 544 mainforce    7u  IPv4 0xd55b454651ecd315      0t0  TCP *:commplex-main (LISTEN)
ControlCe 544 mainforce    8u  IPv6 0xd55b4537ebc766cd      0t0  TCP *:commplex-main (LISTEN)
```

점유하고있는 PID번호를 가진 프로세스에게 SIGTERM을 보냄

```bash
kill -9 544
```

# Git

## 충돌

### 최신 반영 사항을 pull을 하지 않고, push를 시도할 때

```bash
git add test_print_hello.py
git commit -m "upload print_hello_service test_file:"
git push
```

![스크린샷 2023-07-14 오전 9.35.12.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/31c2e3c5-21cd-4707-804c-4a5aa4930bd8/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-07-14_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_9.35.12.png)

merge를 통해, 현재 브랜치 상태에 merge한다.

```bash
git config pull.rebase false
git pull
```

이를 통해, 최신 반영 사항으로 로컬을 업데이트 후

로컬의 변동 사항을 push한다.

```bash
git push
```
