# Internet watcher

For when you internet provider, or landlords says: "your internet is fine", and you want to prove them wrong

## Installation

```bash
virtualenv venv --python=python3.7
```

## Running locally 

```bash
source sourcefile
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Running the full stack with Grafana and Prometheus

```bash
docker-compose up -d
```

You can the access Grafana at http://localhost:3000

You'll have to connect the datasource and create a dashboard.

Data source url: `prometheus:9090`

The dashboard is available as an import in `dashboards/`

## A note on issues

I put this together in a very short amount of time to prove a point. 

Please don't use this if you are looking for perfect accuracy, streaming of data etc. 

It's meant as a rudimentary way to show what my internet looks like on a daily basis.

If you think of improvements, feel free to open a PR, or fork the project :) 

Cheers