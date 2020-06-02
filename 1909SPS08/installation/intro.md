# Installation

Fiori App's Usage report collects start count records for applications started from SAP Fiori Launchpad. 

> In order to clearly identify started applications it refers to application entry maintained in [Fiori Tracker](http://help.fioritracker.org) - an additional tool that you need to install as prerequisite for running Fiori App's Usage report. If you do not have Fiori Tracker yet please install it using [Fiori Tracker installation guide](http://help.fioritracker.org/installation).

Fiori apps' usage has two parts:
1. "Application usage plugin" - UI5 application that is loaded and run automatically as SAP Fiori launchpad plugin for all users with role ZFT_LOGGER
2. OData service used by SAP Fiori launchpad plugin

For each SAP Gateway system that you plan to collect data from your Basis expert needs to complete procedure described in [Basis expert steps](/installation/basis.md).
