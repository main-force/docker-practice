# 과제5
- print_hello_service는 컨테이너 구동 시, 특정 정보들을 print하고 종료하는 서비스입니다.
- print_bye_service는 flask를 활용한 웹서버로, "GET http://${hostIp}:{8888}/" 요청 시 "bye" 10개를 return하는 서비스입니다.
- Github 액션은 pytest를 수행하고, 테스트는 print_hello_service의 `return_hello`함수의 정상 동작을 확인합니다.

# Build Images

## Build print_hello_service Image

```bash
docker build -t print_hello_service:1.0.0 -f ./Dockerfile_print_hello_service .
```

<img width="560" alt="스크린샷 2023-07-13 오후 10 34 31" src="https://github.com/main-force/docker-practice/assets/44683307/aa11c820-ae77-40ab-baa6-ef8c29108b48">

## Build print_bye_service Image

```bash
docker build -t print_bye_service:1.0.0 -f ./Dockerfile_print_bye_service .
```

<img width="562" alt="스크린샷 2023-07-13 오후 10 35 42" src="https://github.com/main-force/docker-practice/assets/44683307/5e16b897-5e1c-434c-9c49-faa37eb9df62">


# Run Containers

## Run print_hello_service Container

```bash
docker run -v ./shared:/app/shared -it print_hello_service:1.0.0
```

### Expected Output

<img width="964" alt="스크린샷 2023-07-13 오후 10 39 28" src="https://github.com/main-force/docker-practice/assets/44683307/8bdb6456-62e4-4567-9039-1937984d5bab">


## Run print_bye_service Container

```bash
docker run -v ./shared:/app/shared -p 8888:8888 -it print_bye_service:1.0.0
```

### Expected Output

<img width="1061" alt="스크린샷 2023-07-13 오후 11 11 32" src="https://github.com/main-force/docker-practice/assets/44683307/ad5dafbe-6110-41d0-86d9-438949950a0e">

<img width="669" alt="스크린샷 2023-07-13 오후 11 12 33" src="https://github.com/main-force/docker-practice/assets/44683307/7f12d225-fef7-4424-88f8-a104b91e4b93">

# Docker Swarm

```bash
docker swarm init
```

> print_hello_service의 경우 데몬상태로 서비스되지 않기때문에(특정 내용 print후 종료 됨), 실행하지 않았습니다.

## Create print_bye_service

```bash
docker service create --name print_bye_service --replicas 3 --publish published=8888,target=8888 --mount type=bind,src=$(pwd)/shared,dst=/app/shared print_bye_service:1.0.0
```

<img width="917" alt="스크린샷 2023-07-16 오후 4 29 44" src="https://github.com/main-force/docker-practice/assets/44683307/9cfee7da-6a43-400e-9357-900ad6c61aa2">


# Troubleshoots

## Git 충돌

### 최신 반영 사항을 pull을 하지 않고, push를 시도할 때

```bash
git add test_print_hello.py
git commit -m "upload print_hello_service test_file:"
git push
```

<img width="773" alt="스크린샷 2023-07-14 오전 9 35 12" src="https://github.com/main-force/docker-practice/assets/44683307/00e42754-290a-4a20-a3c0-5371d16e9ab2">

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
