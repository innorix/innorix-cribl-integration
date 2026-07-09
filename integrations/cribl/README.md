# Cribl Stream

This example demonstrates how to integrate INNORIX transfer events with Cribl Stream.

## Overview

The pipeline retrieves transfer information from the INNORIX Platform, enriches each transfer with metadata and file information, and generates structured events that can be ingested by Cribl Stream.

## Features

- Retrieve transfer events from the INNORIX Platform
- Enrich events with transfer details
- Include transferred file information
- Generate structured JSON events
- Forward events to Cribl Stream

## Workflow

```text
INNORIX Platform
        │
Transfer API
        │
        ▼
Transfer Event Pipeline
        │
        ▼
Cribl Stream
        │
Transform
Route
Enrich
        │
        ▼
SIEM / Object Storage / Analytics
```

## Event Contents

- Transfer ID
- Transfer Status
- Source Device
- Target Device
- Transfer Metadata
- File Information
- Event Timestamp

## Run

```bash
python pipeline.py
```

Configure the pipeline in `.env`.

```text
INNORIX_BASE_URL=
INNORIX_API_KEY=
AUTOMATION_ID=

CRIBL_ENDPOINT=
CRIBL_SOURCE=
CRIBL_TOKEN=
```