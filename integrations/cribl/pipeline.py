import json
import os
import time

from client import INNORIXClient

client = INNORIXClient()


def export_transfer_events():

    transfers = client.get_unified_transfer_list(
        automation_id=os.getenv("AUTOMATION_ID"),
        limit=100,
        type_filter="automation,monitor,history"
    )

    items = transfers.get("data", [])

    for item in items:

        transfer_id = (
            item.get("transferId")
            or item.get("id")
            or item.get("monitorId")
        )

        if not transfer_id:
            continue

        detail = client.get_transfer_detail(transfer_id)
        files = client.get_transfer_files(transfer_id)

        event = {
            "event": "innorix.transfer",
            "timestamp": int(time.time()),

            "transfer": detail,

            "files": files,

            "summary": {
                "transferId": transfer_id,
                "status": item.get("status"),
                "source": item.get("source_id"),
                "target": item.get("target_id"),
                "fileCount": len(files.get("data", []))
            }
        }

        print(json.dumps(event, indent=4))

        # TODO:
        # Send event to Cribl Stream
        # HTTP Event Collector
        # TCP Source
        # Syslog Source
        # Kafka Destination


if __name__ == "__main__":

    print("INNORIX Cribl Pipeline started.")

    while True:

        export_transfer_events()

        time.sleep(5)