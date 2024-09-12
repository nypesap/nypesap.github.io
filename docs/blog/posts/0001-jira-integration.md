---
title: How to speed up Jira issue creation for SAP Fiori apps
description: The Fiori Tracker plugin for SAP Fiori Launchpad speeds up Jira issue creation by automatically identifying the problem app and pre-filling technical details.
authors:
  - greg
tags:
  - SAP Fiori
  - SAP Fiori Launchpad
  - SAP S/4HANA
categories:
  - Testing solutions
date: 2019-02-10
---


# How to speed up Jira issue creation for SAP Fiori applications

Gathering feedback on SAP Fiori applications is crucial during both the implementation and support phases of the SAP system lifecycle. Quick, accurate problem reports save valuable time.

<!-- more -->

SAP Fiori apps often face the challenge of non-technical users or team members not knowing which application is causing issues. To solve this, we've developed a plugin for the SAP Fiori Launchpad. This plugin allows users to report problems directly from the problematic app.

Here's how it works:

Auto-Identify the App: The plugin is part of the Fiori Tracker tool. It automatically detects the running SAP Fiori application and fills in the Jira ticket with relevant technical info. Users just click a button to get a prefilled issue title, including the exact name and technical ID of the app.

Simplified Problem Reporting: In the Jira ticket's description field, users only need to describe the problem they're facing.

Screenshot Option: The plugin also captures a screenshot and lets users choose whether to include it in the Jira issue.

With the Fiori Tracker and its "Report Issue" function, reporting problems during testing becomes simple and fast. Your team will appreciate the streamlined process!

:fontawesome-brands-youtube:{ .youtube } [How Fiori Tracker - Report Issue function works](https://youtu.be/adMJJYTxhks?si=xt0QxRs2tVMbRvTI) - :octicons-clock-24: 1m30s

For streamlined testing, check out also my blog post on Fiori Role Testing: [Spot untested apps automatically](0008-fiori-role-testing.md)