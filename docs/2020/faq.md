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

## 6. What is the recommended deployment option?

We recommend using the production system to install and run as a Central System for Fiori Apps' Usage Report. Please find the details in [the deployment recommendation section](FPS01/deployment/prod.md).

## 7. How much time does it take to implement the Fiori Apps' Usage and start collecting the usage records?

You can set up and start using Fiori Apps' Usage in under one day. The detailed installation steps will guide you through the installation process.
