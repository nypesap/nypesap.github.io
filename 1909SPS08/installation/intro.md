# Installation

Fiori App's Usage report collects start count records for applications started from SAP Fiori Launchpad. In order to clearly identify started applications it refers to record collected in Fiori Tracker - an additional tool that you need to install as prerequisite for running Fiori App's Usage report.

To obtain the installation files see section "[Getting transports](trans)".

Section "[Location](/installation/deployment/location.md)" explains where in your landscape "Main part" should be installed to.

Fiori apps' usage is composed of:
- "Application usage plugin" - UI5 application that is loaded and run automatically as SAP Fiori launchpad plugin for all users with role ZFT_LOGGER
- OData service used by SAP Fiori launchpad plugin

Fiori apps' usage a Managed systems. All described activities should be performed in that system. Typically users configure as Managed systems all SAP Gateway systems from their landscape.

There is one set of activities to be performed:

1. [Basis expert steps](/installation/basis.md)