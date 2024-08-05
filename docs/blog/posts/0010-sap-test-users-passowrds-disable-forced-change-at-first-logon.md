---
authors:
  - greg
tags:
  - SAP ABAP
  - SAP S/4HANA
categories:
  - Testing solutions
date: 2024-08-05
description: SAP test users passwords - disable forced change at first logon 
---

# SAP test users passwords - disable forced change at first logon 

When implementing SAP Fiori with its [role-based principle](https://experience.sap.com/fiori-design-web/design-principles/), you’ll need numerous test users. These users will be shared among different project members, so they need to have set passwords.

<!-- more -->

Updating these passwords manually, especially for more than 10 users, is tedious. You need to:

1. Set the password.
2. Disable forced password change at the first logon.

Here's a report to automate this process. It sets the passwords to match the usernames by default, but you can adjust it as needed.

``` ABAP
REPORT zpassreset.

DATA: uname TYPE xubname, returny TYPE i, 
bapimsg LIKE bapiret2 OCCURS 0 WITH HEADER LINE, 
p_passw TYPE bapipwd.

TYPES: BEGIN OF ty_itab,
uname TYPE xubname,

END OF ty_itab.

TYPES: tt_itab TYPE STANDARD TABLE OF ty_itab.
DATA: itab TYPE tt_itab,
wa_itab TYPE ty_itab.

SELECTION-SCREEN: BEGIN OF BLOCK b1 WITH FRAME TITLE TEXT-001.

SELECT-OPTIONS: s_uname FOR uname.

SELECTION-SCREEN: END OF BLOCK b1.

INITIALIZATION.
%_s_uname_%_app_%-text = 'User'.

DATA: user LIKE LINE OF s_uname.

LOOP AT s_uname INTO user.

uname = user-low.
WRITE:/ 'Changing: ',uname.

p_passw-bapipwd = uname.

CALL FUNCTION 'BAPI_USER_CHANGE'
EXPORTING
username = uname
password = p_passw
passwordx = 'X'
productive_pwd = 'X'
TABLES
return = bapimsg.

LOOP AT bapimsg.

WRITE:/ bapimsg-message .
ENDLOOP.
WRITE:/.

ENDLOOP.
```

