---
description: Getting "Step ID" of the Workflow task item
authors:
  - greg
tags:
  - SAP Workflow
  - SAP My Inbox
categories:
  - Development
date: 2026-02-05
slug: Getting-Step-ID-of-the-Workflow-task-item
---

# How to get "Step ID" of the Workflow task item

Step ID is a useful piece of information that you might need when troubleshooting My Inbox and workflow topics. Here is how to find the Step ID for a workflow task with a given ID.
<!-- more -->

1. Start SAP GUI transaction SWIA.
2. Put the Task ID in the “Identification” field. 
3. Remove the restriction on creation timestamp by clearing both “Creation date” and “Created At”. 
4. Go to the menu “Edit”, “Display Workflow log.”
5. In the Workflow log window, choose the button “Chronological view.”

