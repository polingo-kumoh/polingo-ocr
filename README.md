# POLINGO OCR API Server


## Installation
```shell

git clone https://github.com/polingo-kumoh/polingo-ocr.git

```

## Get Started

- To use this service, Docker must be installed on the server.

```shell
docker network create --driver=bridge --subnet=172.22.0.0/16 polingo

docker compose up
```

### Usage

- Text can be extracted from image files that are in English or Japanese.

```shell

curl --location 'http://{OCR_SERVER_URL}:5001/api/ocr/v1/to-text' \
--form 'file=@"/C:/Desktop/image.png"'

```
