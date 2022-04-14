# Frequently Asked Questions

## 1. What are the prerequisites/minimal requirements for installation?

The minimal requirement is any SAP system with GAP Gateway (software component SAP_GWFND) on SAP NetWeaver version at least 7.52 ([see details](inst/min.md))

## 2. Will the Fiori Tracker release 2020 work on my S/4 HANA system that is on the different releases (1610, 1709, 1809, 1909)?

Yes. Fiori Tracker release numbering is independent of SAP release numbering. Fiori Tracker release 2020 is compatible with SAP S/4 HANA releases from 1610 to 2020. Refer [Minimal requirements](inst/min.md) for more details.

## 3. What details do you need for troubleshooting the issues?

Please send the screenshots from the application running in Chrome with URL and "Developer tools" console.

Screenshot from respective SAP Gateway system from SAP Gui menu: System->Status SAP System Data -> Details.

## 4. Is there any way that I can pull the historical data?

The data is collected when the Fiori Apps' Usage Plugin is active for the user, so there is no way to pull the historical data. 

## 5. What is the architecture of the solution?

Please find the details in [the Architecture section](arch/architecture.md).

## 6. How is the solution deployed?

Fiori Apps' Usage Report is deployed by importing the transports. Please find the details in [deployment section](FPS01/deployment/deployment.md).

## 7. How much time does it take to implement the Fiori Apps' Usage and start collecting the usage records?

You can set up and start using Fiori Apps' Usage in a couple of hours. The descriptions in [the installation section](FPS01/inst.md) will guide you through all the required steps. Should you encounter any problem, you can reach Fiori Apps' Usage team on the support Slack channel or ask us for a screen-sharing session.

### 8. Can I use my own roles instead of using the ones provided in Fiori Apps' Usage transport requests?

Yes. [See how to create or extend an existing role](FPS01/extend-existing-role.md)