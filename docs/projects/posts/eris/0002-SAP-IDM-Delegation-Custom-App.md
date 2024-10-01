---
title: SAP IDM Delegation custom app
description: >
  SAP IDM Delegation - custom application
authors:
  - nype
categories:
  - Custom applications
tags:
  - SAP S/4HANA 2021
  - SAP IDM 8.0
  - SAP IDM REST API
  - SAP Security
industries:
  - Finance (Germany)
date: 2023-10-02
---

<!-- more -->

Custom application: SAP IDM Delegation

The app was using standard SAP IDM rest API ([SAP Identity Management REST Interface Version 2](https://help.sap.com/docs/SAP_IDENTITY_MANAGEMENT/4773a9ae1296411a9d5c24873a8d418c/0b1d493d512c422691cbb31c30159734.html)) to create, update and delete delegation records in SAP Identity Management version 8.0 (SAP IDM).

The work included the use od SAP Identity Management Studio 8.8.39 (based on Eclipse).

SAP IDM REST API services used:

/idmrestapi/v2/service/ET_MX_PERSON<br>
/idmrestapi/v2/service/TASK_CONFIGURATIONS




