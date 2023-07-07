# Frequently Asked Questions

### 1. What are the prerequisites/minimal requirements for installation?

The minimal requirement is any SAP system with GAP Gateway (software component SAP_GWFND) on SAP NetWeaver version at least 7.52 ([see details](inst/min.md))

### 2. Will the Fiori App Usage Report release 2020 work on my S/4 HANA system that is on the different releases (1610, 1709, 1809, 1909)?

Yes. Fiori App Usage Report release numbering is independent of SAP release numbering. Fiori App Usage Report release 2020 is compatible with SAP S/4 HANA releases from 1610 to 2022. Refer [Minimal requirements](inst/min.md) for more details.

### 3. What details do you need for troubleshooting the issues?

Please send the screenshots from the application running in Chrome with URL and "Developer tools" console.

Screenshot from respective SAP Gateway system from SAP Gui menu: System->Status SAP System Data -> Details.

### 4. Is there any way that I can pull the historical data?

The data is collected when the Fiori App' Usage Plugin is active for the user, so there is no way to pull the historical data. 

### 5. What is the architecture of the solution?

Please find the details in [the Architecture section](arch/architecture.md).

### 6. How is the solution deployed?

Fiori App Usage Report is deployed by importing the transports. Please find the details in [deployment section](FPS01/deployment/deployment.md).

### 7. How much time does it take to implement the Fiori App Usage and start collecting the usage records?

You can set up and start using Fiori App Usage in a couple of hours. The descriptions in [the installation section](FPS01/inst.md) will guide you through all the required steps. Should you encounter any problem, you can reach Fiori App Usage team on the support Slack channel or ask the team for a screen-sharing session.

### 8. Can I use my roles instead of the ones provided in Fiori App Usage transport requests?

Yes. [See how to create or extend an existing role](FPS01/extend-existing-role.md).

### 9. How to get the SAP system installation number?

Please check the [detailed description](inst/installation-number.md).

### 10. Should we install Fiori App Usage Report on SAP Solution Manager?

SAP Solution Manager is a very good choice when it comes to using Fiori App Usage Report and Fiori Tracker suite tools when your main landscape can get temporarily offline (upgrades and other maintenance activities). The only reason we do not encourage our users to use SAP Solution Manager is that most of the installations are on NetWeaver below 7.52 while Fiori Tracker Suite component need at least NetWeaver 7.52. If your SAP Solution Manager is on 7.52 then it is a perfect place for installation.

### 11. Do you have a demo of the application? 

We can arrange a call to demo Fiori App Usage Report on our systems. Please let us know using [the "Get an offer" on the main page](https://help.fioriAppusage.org/) if you would like to have a call. We will send the timing proposition.

### 12. What are all roles needed for manager and user?

Please check the [summary](inst/roles.md).

### 13. What is the Fiori App Usage impact on applications and system performance?

Fiori App usage impacts overall system performance as little as possible. See the details in [Fiori App Usage performance influence section](FPS01/performance.md).


### 14. Why should we use a third-party solution instead of waiting for the same function delivered by SAP out of the box?

Any solution to the application usage reporting problem will require identifying the applications covered by the project. As the Fiori App Usage Report's key aspect is the identification, you can start tracking the app's usage with the Fiori App Usage report and leverage the same app identification records if the standard out-of-the-box solution will be developed.

