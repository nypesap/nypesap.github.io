---
description: SAP Workflow Essentials for SAP Fiori Developer working with "My Inbox"
authors:
  - greg
tags:
  - SAP S/4HANA
  - SAP Fiori
categories:
  - Development
date: 2024-11-16
slug: SAP-Workflow-Essentials-for-SAP-Fiori-Developers
---

# SAP Workflow Essentials for SAP Fiori Developer working with "My Inbox"

If you're a SAP Fiori developer working on "My Inbox" or migrating from SAP Workflow in SAP Business Suite, Unified Inbox, or SAP Portal, it is important to understand SAP Workflow basics. This guide breaks down the essentials you need to streamline your work with "My Inbox".<!-- more -->

## Terminology summary

`Workflow Scenario`
: A collection of tasks, agent-determination rules, and related artifacts that can be sequenced to construct workflows. Identified by Workflow ID  f.e. WS99100200

`Task`
: The description and context of what needs to be performed in a workflow step/activity. Part of Workflow Scenarios. Identified by Task ID f.e. TS12300116

`Work item`
: The instance of a task.

## Transactions

`SWDD`	
: Workflow builder

`SWIA`	
: Work item administration (WI)

You can find the details of the workflow item. To identify the workflow item id while running My Inbox app check the URL. The last part of the URL is the work item number.

`PFTC`	
: Template, task management (WS, TS)

## Recreating the workflow item presentation

Existing workflows are like small apps, some of which have been customized for specific user experiences. As part of the migration project, you will aim to maintain the look and behavior of these workflows in the "My Inbox" app. You may need to adjust your "My Inbox" settings to align with your existing workflows to achieve similar results. The following customizations will need adjustments in "My Inbox":

1. Decision buttons modelled as "Activity steps"
    - configuration to display button
    - configuration to handle button press
