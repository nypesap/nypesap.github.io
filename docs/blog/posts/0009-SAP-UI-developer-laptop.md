---
authors:
  - greg
tags:
  - SAP Fiori
  - SAP UI5 development
  - SAP S/4HANA
categories:
  - Developer tools
date: 2023-05-01
description: SAP UI5 developer laptop setup.
---

# SAP UI5 developer laptop setup

This guid will help you make sure that your project laptop is ready for SAP UI5 development. I'm listing the essential hardware and software configuration you need to develop and support SAP UI5 applications.

<!-- more -->

## Windows

Hardware configuration:

- RAM: 32 GB (minimum), 64 GB (recommended)
- Processor: Intel Core i7 2.7GHz, 6 cores or similar
- Hard Disk: 512 GB

Software:

- Chrome - Code debugging and issue investigation
- SAP Gui - SAP backend access
- Eclipse - SAP CDS development
- ABAP Development Tools for Eclipse (ADT) - SAP CDS development
- Visual Studio Code - Code editing, HTTP requests testing
- Gitgui - local repository visualization and management
- Notepad++ - text files handling
- MS PowerToys - easing getting text from bitmaps, screen management and other productivity improvements
- ShareX - Screen recording for preparing the test evidence for scenarios with multiple steps
- Nodejs - automation through scripting
- Python - automation through scripting
- Docker -  OS-level virtualization
- WSL2 - OS-level virtualization

Web apps access:

- SAP Business Application Studio

Ensure SAP Business Application Studio (SAP BAS) connects efficiently to SAP cloud systems. These systems handle SAP BAS application files and proxy a massive influx of calls to on-premise backends, especially during UI5 app tests using the 'Preview' function. On corporate networks with SSL Inspection, some requests may be blocked. In such cases, add 'applicationstudio.cloud.sap' to the allowlist ("whitelist").

Example laptop models:

- Lenovo Thinkpad T15P
- HP ZBook Firefly 14 G8

