# Libc Box for pwners

## Usage

```
$ docker run -w "/problem" -v "$PWD:/problem" -it moratorium08/libc:2.23 /bin/bash
```

You can attach the container and debug it by gdb with peda and pwngdb:

```
$ docker exec -it <container_id> /bin/bash
$ gdb -p `pgrep xxxx`
```

Supported libc versions

* 2.30
* 2.29
* 2.28
* 2.27
* 2.26
* 2.24
* 2.23

Detail: [Docker Hub](https://hub.docker.com/r/moratorium08/libc)

## Build & Push

### Generate Dockerfiles

#### 1.Write `config.yaml`

Example

```
docker:
    id: moratorium08
    repo: libc
```

#### 2. Run python script

```
$ pip install -r requirements.txt
$ ./gen.sh
```

### Build Dockerfiles

```
$ ./build.sh
```

### Push Dockerfiles

```
$ ./push.sh
```
