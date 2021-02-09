# Fiori Apps' Usage Report - Installation
General Basis expert steps

1. [Obtain the transport files from Nype's representative](../../../inst/step-1) - files for Release `2020FPS01` 
2. [Activate Frontend ICF nodes](../../../inst/step-2) for node `zfau`
3. [Enable backend odata service](../../../inst/step-3) for service `ZNYPEFAU_SRV`
4. [Assign pfcg roles](../../../inst/step-4) for role `ZNYPE_FAU`

As-is plugin, Basis expert steps

1. [Install As-is on Central system]({{ prod.fau.compatibleAsisCenLink }})
2. [Install As-is on each Managed system]({{ prod.fau.compatibleAsisManLink }}) 

If you are installing Catalog Import for the first time please check [Evaluation deployment](eval-dep.md) for details on installing Catalog Import to one system (f.e. Sandbox).

# General considerations
We designed each Fiori Apps' Usage Report product to work independently. Once you install the product and any dependent products are needed, it will guide the user to install those.

!!! Note
    Release 2020 FPS01 is not downward compatible with previous releases. It should **not** be installed on top of older releases. If you have used previous releases and would like to move to release 2020 FPS01 then you need to move your data manually. If you need help with moving you data please contact our project manager for an offer (gm@nypesap.com)