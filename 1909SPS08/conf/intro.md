#  Configuration

As Fiori Apps' usage administrator, there is only one parameter that you need to set:

## Define RFC destination of a Central system

In each Managed system you need to provide RFC destination pointing to the Central system just use it in the next step. If you do not have such RFC destination, please prepare it in transaction `SM59`.

Run `SM30` transaction and add an entry to `ZFSL_SYST_CONFIG` table.


|  Config key   |      Config value                            |
| ------------- |:-------------------------------------------: |
|  TARGET_RFC   | `<RFC destination of your Central system>`   |

!> RFC destination user must have authorizations to run function module: Z_FT_LOG_APPLICATION_USAGE

![](/installation/res/rfc.png)


