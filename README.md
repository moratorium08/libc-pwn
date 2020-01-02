# Libc Box for pwners

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
