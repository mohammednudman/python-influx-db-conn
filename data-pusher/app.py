import os
import time
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

INFLUXDB_URL = os.getenv('INFLUXDB_URL')
INFLUXDB_ORG = os.getenv('INFLUXDB_ORG')
INFLUXDB_BUCKET = os.getenv('INFLUXDB_BUCKET')
INFLUXDB_TOKEN = os.getenv('INFLUXDB_TOKEN')

write_client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)
write_api = write_client.write_api(write_options=SYNCHRONOUS)

for value in range(5):
    current_time = int(time.time() * 1000)
    
    point = (
        Point("measurement1")
        .tag("tagname1", "tagvalue1")
        .tag("location", "office")
        .field("field1", value)
        .field("field2", value * 2.5)
        .field("status", "active")
        .time(current_time)
    )
    
    write_api.write(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG, record=point)
    print(f"Data point {value} written to {INFLUXDB_BUCKET}")
    time.sleep(1)

write_client.close()
