# Fiori Apps' Usage architecture

Fiori Apps' Usage report collects usage data from any SAP Gateway of a SAP Business Suite or SAP S/4 HANA system. 

Fiori Apps' usage has two parts:
1. "Application usage plugin" - UI5 application that is loaded and run automatically as SAP Fiori launchpad plugin for all users with role ZFT_LOGGER
2. OData service used by SAP Fiori launchpad plugin

The picture below depicts typical Fiori Apps' Usage architecture.
![](res/architecture.png)
*Recommended installation in three tier system landscape with central system on SAP Solution Manager*

You can install the tool also directly on any other SAP Gateway – find all deployment options in section [Deployment options](deployment/intro.md).


