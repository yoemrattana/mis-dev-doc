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

Bed net
-------

Insert/Update/Delete bed net

Tablet diagram

::

  +-----------------+     +---------------+     +---------------+
  |                 |     |               |     |               |
  | tblCensusVillage|-----| tblMalBedNet  |-----| tblHFCodes    |
  |                 |     |               |     |               |
  +-----------------+     +---------------+     +---------------+

- Controller: CaseReport.php 

  - ``bednet()`` : view bed net page.
  - ``bednetGetReport()`` get groups and month report list.
  - ``bednetGetCase()`` get bed net report when you click on report month.
  - ``bednetUpdateCase()`` insert/update/delete bed net.

  ::

    if ( Rec_ID > 0 ) 
      then update()
    else if ( Rec_ID < 0 )
      then delete()
    else insert()

  - ``bednetDeleteReport()`` delete report.
  
- View: bednet_view.php
- ViewModel: Bednet.js

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
  |     |__bednet_view.php
  |
  |__media
     |
     |__ViewModel
        |
        |__Bednet.js


MMP bed net
-----------

Insert/Update/Delete MMP bed net

Tablet diagram

::

  +-------------+    +-------------+ 
  |             |    |             | 
  | tblMLBednet |----| tblMLCodes  |     
  |             |    |             | 
  +-------------+    +-------------+ 

- Controller: CaseReport.php 

  - ``bednetML()`` : view MMP bed net page.
  - ``mlGetPreData()`` get region, province and treatments list.
  - ``bednetMLGetReport()`` get groups and month report list.
  - ``bednetMLGetCase()`` get bed net report when you click on report month.
  - ``bednetMLUpdateCase()`` insert/update bed net.

  ::

    if ( Rec_ID == -1 )
      then insert()
    else update()

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
    | tblPLBednet | --------|tblPLTroopCodes   |
    |             |         |                  |
    +-------------+         +------------------+

- Controller: CaseReport.php 

  - ``bednetPL()`` : view police bed net page.
  - ``plGetPreData()`` get province list.
  - ``bednetPLGetReport()`` get troop and month report list.
  - ``bednetPLGetCase()`` get bed net report when you click on report month.
  - ``bednetPLUpdateCase()`` insert/update bed net.

  ::

    if ( Rec_ID == -1 )
      then insert()
    else update()

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

Bed net other
-------------

Insert/Update/Delete other bed net report

Tablet diagram

::

    +-------------------+
    |                   |
    | tblMalBednetOther |
    |                   |
    +-------------------+

- Controller: CaseReport.php 

  - ``bednetother()`` : view police bed net page.
  - ``bednetOtherGetReport()`` get troop and month report list.
  - ``bednetOtherUpdateReport()`` insert/update/delete bed net.

::

    if ( Rec_ID > 0 ) 
      then update()
    else if ( Rec_ID < 0 )
      then delete()
    else insert()
  
- View: bednetother_view.php
- ViewModel: BednetOther.js

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
  |     |__bednetother_view.php
  |
  |__media
     |
     |__ViewModel
        |
        |__BednetOther.js    

Questionaire
------------

tblQuestion11 , tblQuestion12, tblQuestion21, tblQuestion13, tblQuestion22

Annex 1: Village Selection
~~~~~~~~~~~~~~~~~~~~~~~~~~

Table

::

    +---------------+
    |               |
    | tblQuestion11 |
    |               |
    +---------------+

- Controller: Question.php

  - ``index(Q11)`` view page.
  - getData(tblQuestion11) retrieve data.
- Controller: Direct.php

  - ``insert()``
  - ``update()``
  
- View: question11_view.php
- ViewModel: Question11.js

Annex 2: Hotspot Identification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Table

::

    +---------------+
    |               |
    | tblQuestion12 |
    |               |
    +---------------+

- Controller: Question.php

  - ``index(Q12)`` view page.
  - getData(tblQuestion12) retrieve data.
- Controller: Direct.php

  - ``insert()``
  - ``update()``
  
- View: question12_view.php
- ViewModel: Question12.js

Annex 4: MMW Recruitment
~~~~~~~~~~~~~~~~~~~~~~~~

Table

::

    +---------------+
    |               |
    | tblQuestion21 |
    |               |
    +---------------+

- Controller: Question.php

  - ``index(Q21)`` view page.
  - getData(tblQuestion21) retrieve data.
- Controller: Direct.php

  - ``insert()``
  - ``update()``
  
- View: question21_view.php
- ViewModel: Question21.js

Annex 5, 6: Site Visit Active Screening
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Table

::

    +---------------+
    |               |
    | tblQuestion13 |
    |               |
    +---------------+

- Controller: Question.php

  - ``index(Q13)`` view page.
  - getData(tblQuestion13) retrieve data.
- Controller: Direct.php

  - ``insert()``
  - ``update()``
  
- View: question13_view.php
- ViewModel: Question13.js

Annex 7: Forest Pack
~~~~~~~~~~~~~~~~~~~~

Table

::

    +---------------+
    |               |
    | tblQuestion22 |
    |               |
    +---------------+

- Controller: Question.php

  - ``index(Q22)`` view page.
  - ``getData(tblQuestion22)`` retrieve data.
- Controller: Direct.php

  - ``insert()``
  - ``update()``
  
- View: question22_view.php
- ViewModel: Question22.js

Foci investigation
------------------

Table v1

::

    +-----------------------+     +-------------------+
    |                       |     |                   |
    | tblFociInvestiation   |-----| tblCensusVillage  |
    |                       |     |                   |
    +-----------------------+     +-------------------+

Table v2

::

    +-----------------------+     +-------------------+
    |                       |     |                   |
    | tblFociInvestiation2  |-----| tblCensusVillage  |
    |                       |     |                   |
    +-----------------------+     +-------------------+

List of foci
~~~~~~~~~~~~

- Controller: Foci.php

  - ``index()`` view page
  - ``getData()`` we use store procedure ``SP_Get_FociList`` 
  - ``getDetail()``
- View: foci_view.php
- ViewModel: Foci.js

Detail of foci v1
~~~~~~~~~~~~~~~~~~

- Controller: Foci.php

  - ``open(village_code)`` to open form of foci v1.
  - ``save1()`` to save data of foci v1.

  ::

    if ( Rec_ID == null )
      then insert()
    else update()

  - ``getPatient()``
- View: foci1_view.php
- ViewModel: Foci1.js

Detail of foci v2
~~~~~~~~~~~~~~~~~~

- Controller: Foci.php

  - ``open(village_code)`` to open form of foci v2.
  - ``save2()`` to save data of foci v2.

  ::

    if ( Rec_ID == null )
      then insert()
    else update()

  - ``getClassify()``
- View: foci1_view.php
- ViewModel: Foci1.js

Follow up
---------

VMW follow up
~~~~~~~~~~~~~

Table

::

  +----------------+
  |                |
  | tblVMWFollowup |
  |                |
  +----------------+

- Controller: VMWFollowup.php

  - ``getData()`` get list of VMW follow up
  - ``getDetail()`` get detail of VMW follow up
  - ``delete()`` delete follow up.
  - ``save()`` insert/update

  ::

    if ( empty (Rec_ID) )
      then insert()
    else update()  
- View: vmwfollowup_view.php
- ViewModel: VMWFollowup.js
  
HC follow up
~~~~~~~~~~~~

Table

::

  +---------------+
  |               |
  | tblHCFollowup |
  |               |
  +---------------+

- Controller: HCFollowup.php

  - ``getData()`` get list of follow up
  - ``getDetail()`` get detail of follow up
  - ``delete()`` delete follow up.
  - ``save()`` insert/update

  ::

    if ( empty (Rec_ID) )
      then insert()
    else update()  
- View: hcfollowup_view.php
- ViewModel: HCFollowup.js

HIS data upload
---------------

Table diagram

::

  +-----------------+     +-----------------+     +-----------------+     +-----------------+
  |                 |     |                 |     |                 |     |                 |
  | tblHisDipstick  |     |    tblHisSlide  |     |   tblHisTreat   |     |    tblHisVMW    |
  |                 |     |                 |     |                 |     |                 |
  +-----------------+     +-----------------+     +-----------------+     +-----------------+

- Controller: HIS.php

  - ``getData()`` get list of his report
  - ``getDetail()`` show detail of report by month
  - ``getReport()`` show report of HIS and MIS
  - ``upload()`` upload excel file of HIS
  - ``delete()`` delete report