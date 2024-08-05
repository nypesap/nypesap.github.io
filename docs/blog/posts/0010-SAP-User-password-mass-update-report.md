---
authors:
  - greg
tags:
  - SAP ABAP
  - SAP S/4HANA
categories:
  - Testing solutions
date: 2020-01-20
description: SAP user password mass update report - disable forced password change at the first logon
---

# SAP user password mass update report - disable forced password change at the first logon

Each implementation project with SAP Fiori's role-based principle brings the need to keep numerous test users. Those test users are going to be used by different project members simultaneously, thus the need to share the test users with their passwords.

<!-- more -->

 Before sharing the list, there is a need to set the user passwords. Manually updating more than 10 passwords seems like a tedious task. Especially that there are two steps needed:

1. Setting the password,
2. Avoid forced password change at the first logon to keep password unchanged

Below is the report that automates this job.

The report sets the passwords the same as users, but feel free to adapt the program if you find it disturbing.

``` ABAP
REPORT zfioripassreset.

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

