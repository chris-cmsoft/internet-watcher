import time
from prometheus_client import Histogram, Gauge, start_http_server
from speedtest import Speedtest, ConfigRetrievalError, HTTP_ERRORS, SpeedtestCLIError, get_exception, printer, \
    NoMatchedServers, ServersRetrievalError, InvalidServerIDType


def run_speedtest_loop():
    try:
        speedtest = Speedtest(timeout=10)
    except (ConfigRetrievalError,) + HTTP_ERRORS:
        printer('Cannot retrieve speedtest configuration', error=True)
        raise SpeedtestCLIError(get_exception())

    try:
        speedtest.get_servers(servers=None, exclude=None)
    except NoMatchedServers:
        raise SpeedtestCLIError('No matched servers')
    except (ServersRetrievalError,) + HTTP_ERRORS:
        printer('Cannot retrieve speedtest server list', error=True)
        raise SpeedtestCLIError(get_exception())
    except InvalidServerIDType:
        raise SpeedtestCLIError('Invalid Server ID Type supplied')

    speedtest.get_best_server()
    speedtest_results = speedtest.results
    speedtest.download()
    speedtest.upload()

    return {
        "ping": speedtest_results.ping,
        "latency": speedtest_results.server["latency"],
        "download": speedtest_results.download / 1000.0 / 1000.0,
        "upload": speedtest_results.upload / 1000.0 / 1000.0,
    }


if __name__ == '__main__':
    start_http_server(8005)
    download_gauge = Gauge('internet_download_speed', 'Download Speed')
    upload_gauge = Gauge('internet_upload_speed', 'Upload Speed')
    ping_gauge = Gauge('internet_ping', 'Ping Speed')
    latency_gauge = Gauge('internet_latency', 'Ping Speed')

    while True:
        results = run_speedtest_loop()
        download_gauge.set(results["download"])
        upload_gauge.set(results["upload"])
        ping_gauge.set(results["ping"])
        latency_gauge.set(results["latency"])
        time.sleep(5)
