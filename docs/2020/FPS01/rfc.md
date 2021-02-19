# How to prepare the RFC destinations for Central system

On each Managed system you will need RFC destinations that will run Fiori Apps' Usage App, and serve as you Central system. Create RFC destination in your Managed system using transaction **sm59**. 

The user set in RFC destination needs to have type SYSTEM and the following authorizations:

Authorization: S_RFC

ACTVT: 16

RFC_TYPE: FUGR

RFC_NAME: Z_FTASIS
