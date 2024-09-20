---
description: App IDs are key in SAP S/4HANA projects but custom/extended SAP Fiori apps often lack clear IDs
authors:
  - greg
tags:
  - SAP S/4HANA
  - SAP Fiori launchpad
categories:
  - Project organization
date: 2024-09-16
slug: SAP-Fiori-custom-app-identification
---

# SAP Fiori custom application identification

In SAP S/4HANA projects, application IDs play a critical role in managing SAP Fiori applications. While standard apps come with unique IDs that make them easy to track, custom and extended apps rarely get the same attention. <!-- more -->Failing to record the custom app IDs correctly can lead to project confusion, support delays, and documentation gaps. This post will cover the importance of custom app IDs, the challenges teams face without them, and provide a recommendation for proper identification. I'll suggest a tool for managing app IDs and highlight why accurate tracking is key for long-term project success.

## Why custom app IDs matter in SAP S/4HANA projects

SAP Fiori standard apps are easily identifiable by a unique App ID, which helps customers find app documentation, communicate in projects, and locate support information. For the same reasons, projects should keep track of custom and extended application IDs.

## Reason 1: Finding and maintaining documentation

A list of custom apps with IDs is already a foundation of technical documentation. Although specifying the requirements and features of custom apps takes time, maintaining an official list of the apps is a quick yet fundamental long-term step. Ultimately, you need a list of what needs documentation.

The app list shows the extent of custom solutions in the project. App IDs help connect these with external docs. For example, if your git repo is named after the app ID, everyone can easily find source with comments and the history of commit descriptions. Similarly, naming transport packages with ABAP objects lets the team see app's structure without extra documentation. Orientating documentation around app id will help to keep it current.

## Reason 2: Communication in Projects

Identifying the applications in scope is crucial. It helps with several challenges. First, users can find the right app when contacting support. Next, project members can easily track the status of apps during development, testing, and documentation. Finally, assigning apps to specific business areas clarifies responsibility throughout the project.

## Reason 3: Scope management

The apps enabled in the Fiori Launchpad, whether custom or standard, define the project’s scope. Adding a new app, especially a custom one, can be costly. So, it’s crucial to track it. To maintain scope control and accurate documentation, always include the app in your documentation before implementing it. This simple step ensures clarity and helps maintain control over the scope.

## Proper identification

Out of experience, I recommend using the same convention SAP uses in its Fiori application library for App IDs: the letter and four digits. SAP follows a naming convention for its standard apps, using letters other than Z and Y for SAP Gui transactions. This allows projects to use Z and Y for their custom and extended apps. For example, "Z0061" is a simple and clear indication that immediately informs the user that they are dealing with a custom app.

When maintaining a list of applications, the choice of tool is not critical as long as the project stores an official list of app IDs in one location. Projects can accomplish this using a SharePoint Excel spreadsheet, a Confluence page, or a similar tool. If you need to connect your App IDs with other records such as Fiori Launchpad catalogs, roles, test users, usage logs, and change requests, consider using a dedicated tool like [Fiori Tracker](https://fioritracker.org).

## Conclusion

Custom App IDs are key to keeping SAP S/4HANA projects organized. They help avoid confusion, improve documentation, and make it easier to manage project scope and support. Whether you use a basic spreadsheet or a tool like [Fiori Tracker](https://fioritracker.org), tracking these IDs early on will save time and effort later. Keep it simple, but make sure it's done right.
