# Set the Central system

1. In your Managed system, start SAP Gui transaction **ZNYPEFAMANADMIN**, and start step **1. Modify Central system**:

In RFC Destination field provide the RFC destination of your Central system (see [how to prepare it](rfc.md))

Configuration table: **znypefaman_sc**

|Key|Value|
|--|--|
|SYSTEM_ID|SID that will show in central system as source SID|
|TARGET_RFC|RFC destination of Central system|

Empty values will result in sending to local system as a central one and source system ID will be set as local system SID.
