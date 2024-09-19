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

In SAP S/4HANA projects, App IDs play a critical role in managing SAP Fiori applications. While standard apps come with unique IDs that make them easy to track, custom and extended apps rarely get the same attention. <!-- more -->Failing to record the custom App IDs correctly can lead to project confusion, support delays, and documentation gaps. This post will cover the importance of custom App IDs, the challenges teams face without them, and provide a recommendation for proper identification. I will also suggest a tool for managing App IDs and emphasize the significance of accurate tracking for long-term project success.

## Why custom app IDs matter in SAP S/4HANA projects

SAP Fiori standard apps are easily identifiable by a unique App ID, which helps customers find app documentation, communicate in projects, and locate support information. For the same reasons, projects should keep track of custom and extended application IDs.

## Reason 1: Finding and maintaining documentation

Having a list of apps with IDs already serves as documentation. Although it takes time to specify the requirements and features of custom apps, maintaining an official list of the apps is a quick yet fundamental long-term step. Initially, the App IDs provide an understanding of the extent of custom solutions for the project. Additionally, unique App IDs can facilitate live documentation by linking the names of objects stored outside your app directory. For instance, if the git repository's name matches the app ID, every project member can effortlessly locate it and utilize the information stored there (commit descriptions).
Another example is naming transport packages with all ABAP dictionary objects created for the custom app. By following the contents of such a transport package, it is possible to gain insight into how the app is built without the need to reiterate it in technical documents. Keeping a list of the apps with their IDs will also remind you to update your documentation constantly.

## Reason 2: Communication in Projects
Clear identification of the applications in scope helps address the following challenges: How can users identify the correct app when contacting the support center agent? How can project members indicate the applications that require: Status tracking during the development, testing, and documentation process Assignment to a specific business area to establish responsibility during the development, testing, and support of applications.

## Reason 3: Scope management
The list custom apps and SAP standard apps enabled in FLP determine the project's scope. Adding a new app to the Fiori launchpad, especially a custom one, has a major cost impact thus, you should track it. By keeping the rule of including the app entry in the documentation before implementing it, you will gain scope control, together with documentation accuracy.

## Proper identification

Out of experience, I recommend using the same convention SAP uses in its Fiori application library for App IDs: the letter and four digits. SAP follows a naming convention for its standard apps, using letters other than Z and Y for SAP Gui transactions. This allows projects to use Z and Y for their custom and extended apps. For example, "Z0061" is a simple and clear indication that immediately informs the user that they are dealing with a custom app.

When maintaining a list of applications, the choice of tool is not critical as long as the project stores an official list of app IDs in one location. Projects can accomplish this using a SharePoint Excel spreadsheet, a Confluence page, or a similar tool. If you need to connect your App IDs with other records such as Fiori Launchpad catalogs, roles, test users, usage logs, and change requests, consider using a dedicated tool like [Fiori Tracker](https://fioritracker.org).

## Conclusion

Custom App IDs are key to keeping SAP S/4HANA projects organized. They help avoid confusion, improve documentation, and make it easier to manage project scope and support. Whether you use a basic spreadsheet or a tool like [Fiori Tracker](https://fioritracker.org), tracking these IDs early on will save time and effort later. Keep it simple, but make sure it's done right.