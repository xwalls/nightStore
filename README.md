# Manual nightStore

## 📋 Prerequisites

- [Docker](https://docs.docker.com/engine/install/)
- [Docker compose](https://docs.docker.com/compose/install/)
- GNU Make

## Clone:
- Clone the repository:

```bash
git clone https://github.com/xwalls/nightStore
cd nightStore
```

## Usage:
- Create and start containers:
```bash
make up
```

- Stop and remove containers, networks and volumes:
```bash
make down
```

## Visualize the API:
- After starting containers we can call the API from our browser:
```bash
http://localhost:8181/stations/
```