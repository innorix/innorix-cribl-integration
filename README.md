# INNORIX Cribl Integration

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Cribl](https://img.shields.io/badge/Cribl-Stream-FF6A00)
![Event Pipeline](https://img.shields.io/badge/Event-Pipeline-00A3E0)
![License](https://img.shields.io/badge/License-Commercial-red)
![Status](https://img.shields.io/badge/Status-Official-success)

Official integration example for integrating INNORIX file transfer events with Cribl Stream.

## Features

- Retrieve transfer information using the INNORIX REST API
- Generate transfer events from INNORIX
- Build event pipelines for Cribl Stream
- Enrich transfer events with transfer details and file information
- Route transfer events to downstream observability and security platforms

## Repository Structure

```text
.
├── client.py
└── integrations/
    └── cribl/
        ├── README.md
        └── pipeline.py
```

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

- Transfer Information
- Transfer Status
- Transfer Metadata
- File Information
- Event Timestamp

## Requirements

- Python 3.10+
- INNORIX Platform
- INNORIX API Key
- Cribl Stream

## Installation

```bash
pip install -r requirements.txt
```

Copy the example configuration.

```bash
cp .env.example .env
```

Update the configuration.

```text
INNORIX_BASE_URL=
INNORIX_API_KEY=
AUTOMATION_ID=
```

Run the pipeline.

```bash
cd integrations/cribl

python pipeline.py
```

## License

Commercial License

Copyright © INNORIX Co., Ltd. All rights reserved.