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

This blog post discusses the project roles related to managing SAP Fiori applications. I share a practical way to organize project roles based on our experience. This approach factors in the actual situation of the projects coming from ECC to S/4HANA and ensures timely SAP Fiori app handling.
<!-- more -->


## The Challenge 

One key difference between SAP S/4HANA and SAP ECC implementations is the need to manage SAP Fiori launchpad content. This task, unique to SAP S/4HANA, requires projects to create a new role or distribute the task between existing roles. SAP recommends [(1)](#footnotes) creating a new role called "User Experience Lead" (UX lead), but projects often pass on it. Instead, they add new tasks to the existing ECC project roles. The positions involved are:

- Roles and Authorization Expert
- Functional Application Expert
- Developer

These three positions are taking on new responsibilities. To ensure these new tasks are effectively handled, they must be clearly defined and assigned. The project needs to do so to avoid delays, as each team member may assume that someone else is responsible for these tasks.

## The Solution

I have outlined the responsibilities of the three roles involved in the SAP Fiori task to address the need for setting responsibilities. To clarify, I have used two standard project processes in SAP S/4HANA projects as examples:

1. Preparation of roles and authorizations concept and FLP content management concept
2. Addition of new custom or extended applications.

## Adding new custom or extended application

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

## Preparation of roles and authorizations concept and FLP content management concept

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

## Footnotes

(1) SAP Community Blog post: [Essential Roles for S/4HANA Fiori Projects](https://community.sap.com/t5/enterprise-resource-planning-blogs-by-sap/essential-roles-for-s-4hana-fiori-projects/ba-p/13342812) by Pierre Cassano, architect from SAP S/4HANA Regional Implementation Group