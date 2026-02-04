---
description: How the “Default” flag works in the SAP System alias to the OData Service assignment
authors:
  - greg
tags:
  - SAP S/4HANA
  - SAP Fiori
categories:
  - Development
date: 2026-02-04
slug: SAP-odata-service-alias-default-flag-explained
---

# How the “Default” flag works in the SAP System alias to the OData Service assignment

| Attribute / Case | A | B | C |
|------------------|---|---|---|
| Multi origin (`;mo` parameter in request URL) | No | Yes | Not supported |
| Type | Requests routed to one system | Requests retrieving from multiple systems | One-system-only requests |
| Example |  |  | $metadata request |
| Multitude | N | N | N |
| “Default” flag used | Yes | No | Yes |


The “Default” flag is used by the system only in cases A and C, where it determines which system alias is

