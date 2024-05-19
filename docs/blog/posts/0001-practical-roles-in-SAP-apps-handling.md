---
authors:
  - greg
categories:
  - Project organization
tags:
  - SAP UI5
  - SAP Fiori
  - SAP Fiori Launchpad
  - SAP S/4HANA
date: 2022-03-11
---

# Practical project roles in SAP Fiori application handling

This blog post discusses the project roles related to managing SAP Fiori applications. Based on my and my teammates' experience, I'm sharing a practical approach to organizing project roles. This approach factors in the real situation of the projects coming from ECC to S/4HANA and ensures cost-effective app handling without unnecessary delays.
<!-- more -->
The post focuses on three project roles:
- Roles and Authorization Expert
- Functional Application Expert
- Developer
I have skipped the UX lead role suggested by SAP as ECC to S/4HANA migration projects often pass on it. Instead, I added the new UX lead tasks to the existing ECC project roles.

Below, I have listed the roles with their corresponding activities, and the specific deliverables for the two most popular requisites in S/4HANA projects: 1. Preparing roles and authorizations and FLP content management concepts, and 2. Adding new custom or extended application:

1. Adding new custom or extended application:

``` mermaid
sequenceDiagram
autonumber
    Note right of Developer: Prepares the new<br/>custom app or extension<br/>in DEV system
    Note right of Developer: Configures the target <br/>mapping and tile in the<br/> test catalog
    Note right of Functional Expert: An adjusted version<br/>of Roles list
    Note right of Functional Expert:  An adjusted version of <br/>apps mapping to catalogs
    
    Note right of Developer: Custom/extended <br/>app objects developed
    Note right of Developer: Tile in the test catalog<br/> configured, and unit tested
    Developer ->> Functional Expert: App handover document
    Developer ->> Authorizations Expert: App handover document
    Note right of Functional Expert:  Decides how to fit<br/>a custom or extended app<br/>into the existing<br/> catalogs
    Functional Expert->> Authorizations Expert: List of the catalogs to hold<br/> the app
    Note right of Authorizations Expert: Copies or references <br/> the tile and target <br/>from the test catalog <br/>into the catalogs chosen <br/> by Functional Expert 
    Note right of Authorizations Expert: New app is available <br/> to end-users
```

2. Preparing roles and authorizations concept and FLP content management concept

``` mermaid
sequenceDiagram
autonumber
    Note right of Developer: Prepares the new<br/>custom app or extension<br/>in DEV system
    Note right of Developer: Configures the target <br/>mapping and tile in the<br/> test catalog
    Note right of Functional Expert: An adjusted version<br/>of Roles list
    Note right of Functional Expert:  An adjusted version of <br/>apps mapping to catalogs
    
    Note right of Developer: Custom/extended <br/>app objects developed
    Note right of Developer: Tile in the test catalog<br/> configured, and unit tested
    Developer ->> Functional Expert: App handover document
    Developer ->> Authorizations Expert: App handover document
    Note right of Functional Expert:  Decides how to fit<br/>a custom or extended app<br/>into the existing<br/> catalogs
    Functional Expert->> Authorizations Expert: List of the catalogs to hold<br/> the app
    Note right of Authorizations Expert: Copies or references <br/> the tile and target <br/>from the test catalog <br/>into the catalogs chosen <br/> by Functional Expert 
    Note right of Authorizations Expert: New app is available <br/> to end-users
```