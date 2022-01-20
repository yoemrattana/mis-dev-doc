Module
++++++
Malaria & ITN Data
==================

VMW
---

Insert/Update/Delete VMW case

Table diagram

::

  +----------------+        +---------------------+
  |                |        |                     | 
  |tblVMWActivity  |--------|tblVMWActivityCases  |
  |                |        |                     |
  +----------------+        +---------------------+  
          |
          |
          |
  +-----------------+
  |                 |
  |tblCensusVillage |
  |                 |
  +-----------------+

- Controller: CaseReport.php (  , ,vmwDeleteReport)

  - ``vmw()`` : view vwm page
  - ``vmwGetPreData()`` get ODs, HFs, Treatments list.
  - ``vmwGetReport()`` get VMWs' villages and reported months list when you select HF.
  - ``vmwGetCase()`` get vmw case report when you click on report month of any village.
  - ``vmwUpdateCase()`` insert/update/delete case.
  
  ::

    if(Rec_ID > 0) 
      then update()
    else if ( Rec_ID < 0 )
      then delete()
    else insert() 

- View: vmwcase_view.php
- ViewModel: VMWCase.js

::

  root
  |
  |__application
  |  |
  |  |__controller
  |  |  |  
  |  |  |__CaseReport.php
  |  |
  |  |__views
  |     |
  |     |__vmwcase_view.php
  |
  |__media
     |
     |__ViewModel
        |
        |__VMWCase.js

HC
---
Insert/Update/Delete HC case

Table diagram

::

  +---------------+        +------------------+
  |               |        |                  | 
  |tblHFActivity  |--------|tblHFActivityCases|
  |               |        |                  |
  +---------------+        +------------------+  
          |
          |
          |
  +---------------+
  |               |
  |tblHFCodes     |
  |               |
  +---------------+

- Controller: CaseReport.php

  - ``hf()`` : view hf page
  - ``hfGetPreData()`` Treatments list.
  - ``hfGetReport()`` get HF and reported months list when you select OD.
  - ``hfGetCase()`` get HF case report when you click on report month of any HF.
  - ``hfUpdateCase()`` insert/update/delete case.
  
  ::

    if( Rec_ID > 0 ) 
      then update()
    else if ( Rec_ID < 0 )
      then delete()
    else insert() 
- View: hfcase_view.php
- ViewModel: HFCase.js

::

  root
  |
  |__application
  |  |
  |  |__controller
  |  |  |  
  |  |  |__CaseReport.php
  |  |
  |  |__views
  |     |
  |     |__hfcase_view.php
  |
  |__media
     |
     |__ViewModel
        |
        |__HFCase.js

MMP
---
Insert/Update/Delete MMP case

Table diagram

::

  +---------------+        +------------------+
  |               |        |                  | 
  |tblMLActivity  |--------|tblMLActivityCases|
  |               |        |                  |
  +---------------+        +------------------+  
          |
          |
          |
  +---------------+
  |               |
  |tblMLCodes     |
  |               |
  +---------------+

- Controller: CaseReport.php

  - ``ml()`` : view MMP page
  - ``mlGetPreData()`` get region, province and treatments list.
  - ``mlGetReport()`` get group and reported months list when you select province.
  - ``mlGetCase()`` get case report when you click on report month of any group.
  - ``mlUpdateCase()`` insert/update/delete case.
  
  ::

    if ( Rec_ID > 0 ) 
      then update()
    else if ( Rec_ID < 0 )
      then delete()
    else insert()
- View: mlcase_view.php
- ViewModel: MLCase.js

::

  root
  |
  |__application
  |  |
  |  |__controller
  |  |  |  
  |  |  |__CaseReport.php
  |  |
  |  |__views
  |     |
  |     |__mlcase_view.php
  |
  |__media
     |
     |__ViewModel
        |
        |__MLCase.js

Police
------
Insert/Update/Delete Police case

Table diagram

::

  +---------------+        +------------------+
  |               |        |                  | 
  |tblPLActivity  |--------|tblPLActivityCases|
  |               |        |                  |
  +---------------+        +------------------+  
          |
          |
          |
  +---------------+
  |               |
  |tblPLCodes     |
  |               |
  +---------------+

- Controller: CaseReport.php

  - ``pl()`` : view police page
  - ``plGetPreData()`` get province, troop, treatment list.
  - ``plGetReport()`` get post, district, month report list.
  - ``plGetCase()`` get case report when you click on report month.
  - ``plUpdateCase()`` insert/update/delete case.
  
  ::

    if ( Rec_ID > 0 ) 
      then update()
    else if ( Rec_ID < 0 )
      then delete()
    else insert()
- View: plcase_view.php
- ViewModel: PLCase.js

::

  root
  |
  |__application
  |  |
  |  |__controller
  |  |  |  
  |  |  |__CaseReport.php
  |  |
  |  |__views
  |     |
  |     |__plcase_view.php
  |
  |__media
     |
     |__ViewModel
        |
        |__PLCase.js

MMP bed net
-----------

Insert/Update/Delete MMP bed net

Tablet diagram

::

  +-------------+
  |             |
  | tblMlBednet |
  |             |
  +-------------+

- Controller: CaseReport.php 

  - ``bednetML()`` : view MMP bed net page.
  - ``mlGetPreData()`` get region, province and treatments list.
  - ``bednetMLGetReport()`` get groups and month report list.
  - ``bednetMLGetCase()`` get bed net report when you click on report month.
  - ``bednetMLUpdateCase()`` insert/update/delete bed net.
  - ``bednetMLDeleteReport()`` delete report.
  
- View: mlbednet_view.php
- ViewModel: MLBednet.js

::

  root
  |
  |__application
  |  |
  |  |__controller
  |  |  |  
  |  |  |__CaseReport.php
  |  |
  |  |__views
  |     |
  |     |__mlbednet_view.php
  |
  |__media
     |
     |__ViewModel
        |
        |__MLBednet.js

Police bed net
--------------

Insert/Update/Delete police bed net report

Tablet diagram

::

    +-------------+         +------------------+
    |             |         |                  |
    | tblPlBednet | --------|tblPLTroopCodes   |
    |             |         |                  |
    +-------------+         +------------------+

- Controller: CaseReport.php 

  - ``bednetPL()`` : view police bed net page.
  - ``plGetPreData()`` get province list.
  - ``bednetPLGetReport()`` get troop and month report list.
  - ``bednetPLGetCase()`` get bed net report when you click on report month.
  - ``bednetPLUpdateCase()`` insert/update/delete bed net.
  - ``bednetPLDeleteReport()`` delete report.
  
- View: plbednet_view.php
- ViewModel: PLBednet.js

::

  root
  |
  |__application
  |  |
  |  |__controller
  |  |  |  
  |  |  |__CaseReport.php
  |  |
  |  |__views
  |     |
  |     |__plbednet_view.php
  |
  |__media
     |
     |__ViewModel
        |
        |__PLBednet.js    