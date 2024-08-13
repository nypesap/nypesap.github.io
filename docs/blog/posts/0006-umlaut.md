---
title: Issue with German special character in SAP Fiori app "Default Settings for Users" (F1995)
description: >
  Issue with character 'ß' (scharfes S) in username in SAP Fiori app "Default Settings for Users" (F1995)
authors:
  - greg
categories:
  - Troubleshooting
tags:
  - SAP Fiori
  - SAP Fiori Launchpad
  - SAP S/4HANA
  - SAP S/4HANA 2021
industries:
  - Administration (Germany)
date: 2024-02-28
---

SAP systems allow for the use of umlauts (German special characters) in usernames - what could go wrong?
<!-- more -->

Nothing, until you capitalize a username containing the character 'ß' (scharfes S). As per the rules, the uppercase equivalent of 'ß' is 'SS', and suddenly, you have a different username.

An example application with this hiccup is the SAP Fiori app within procurement: 'Default Settings for Users' (F1995). The app’s front end converts the entered username to uppercase before transmitting it to the oData service resulting in an error. 