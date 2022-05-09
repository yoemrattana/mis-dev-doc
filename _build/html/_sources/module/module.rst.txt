Module
++++++

Use case diagram
================

Use case malaria & ITN data
---------------------------

.. figure:: ../images/use_case_malaria_itn.jpg
  :width: 70%
  :align: center
  :alt: Use case for malaria & ITN data

  Use case for malaria & ITN data

Detail diagram
--------------

.. figure:: ../images/detail-diagram.jpg
  :width: 50%
  :align: center
  :alt: Detail diagram

  Detail diagram

Malaria & ITN Data
==================

VMW
---

Insert/Update/Delete VMW case

- System: Enter data of malaria case that report by VMW
- Primary Actor: OD staff, PHD staff.
- Scenario: When VMW does not report malaria data by smart phone then OD staff will be responsible for entering data.

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

- System: Tool for entering malaria case that report by health center/ referal hospital.
- Actor: OD staff
- Scenario: When HC/RH staff cannot report its case then OD staff will be responsible for entering data.

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

- System: Tool for MMP to enter malaria case.
- Actor: MMP staff.
- Scenario: MMP staff login and go to MMP tool then enter data.

Table diagram

::

  +---------------+        +------------------+
  |               |        |                  | 
  | tblMLActivity |--------|tblMLActivityCases|
  |               |        |                  |
  +---------------+        +------------------+  
          |
          |
          |
  +---------------+
  |               |
  |   tblMLCodes  |
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

- System: Followup tool for enter VMW followup data.
- Primary actor: OD staff.
- Scenario: When VMW report malaria case with Pv or Mix specie then system will create patient code and write to database and create VMW notification log.
  when patient go to health center to get Pv radical cure then Hc staff update case by adding G6PD result and number of primaquine then system will create follow up form for that patient.
  In case Hc does not enter data then OD staff will be responsible for entering data.

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

- System: Followup tool for enter HF followup data.
- Primary actor: OD staff.
- Scenario: When HC report malaria case with Pv or Mix specie then system will write to database and generate patient code.
  If patient come from Village that has VMW system will create VMW Notificatino, otherwise system will create HC notification.
  If that patient get Pv radical cure service then Hc update case by enter result of G6PD and number of primaquine then system will create follow up form.
  in case Hc staff does not enter followup data in time then OD staff will be responsible for entering data.

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
- View his_view.php
- ViewModel: HIS.js

Border malaria case upload
--------------------------

Table

::

  +----------------+
  |                |
  | tblBorderCases |
  |                |
  +----------------+

- Controller: BorderImport.php
- View: borderimport_view.php
- ViewModel: BorderImport.js

VMW QA
------

- System: VMW QA tool for OD/PHD monitor VMW.
- Actor: OD , PHD
- Scenario: When HC/OD/PHP use tablet to enter data, then OD/PHD can use this tool to view questionaire, supervision schedule, Monitor, Report, Dashboard.
  
Table diagram

::

  +---------------------+     +---------------------------+     +-------------------------+
  |                     |     |                           |     |                         |
  | tblVMWQuestionnaire |-----| tblVMWQuestionnaireDetail |-----| tblVMWQuestionnaireItem |
  |                     |     |                           |     |                         |
  +---------------------+     +---------------------------+     +-------------------------+

  
- Controller: VMWQA.php
- View: vmwqa_view.php
- ViewModel: VMWQA.js

Lastmile
--------

- System: Last mile 
- Actor: OD/PHD
- Scenario: When VMW cannot enter data, then OD staff will be responsible for entering data.

Table diagram

::

  +----------------------+     +----------------------------+     +----------------+     
  |                      |     |                            |     |                |     
  | tblLastmileHouseHold |----<| tblLastmileHouseHoldMember |----<| tblLastmileTDA |
  |                      |     |                            |     |                |     
  +----------------------+     +----------------------------+     +----------------+
                                  |                   |
                                  |                   |
                          +----------------+    +----------------+
                          |                |    |                |
                          | tblLastmileIPT |    | tblLastmileAFS |
                          |                |    |                |
                          +----------------+    +----------------+

- Controller: Lastmile.php
- View: lastmile_view.php
- ViewModel: Lastmile.js

.. note::

  TDA1 and TDA2 must be 28 days apart.

  Must complete TDA1/TDA2 before do IPT.

  IPT and TDA1 must be 14 days apart.

  IPT and TDA2 must be 28 days apart.

Check list
----------

Check list HC
~~~~~~~~~~~~~
Table diagram

::

  +----------------+      +----------------------+
  |                |      |                      |
  | tblChecklistHC |-----<| tblChecklistHCDetail |
  |                |      |                      |
  +----------------+      +----------------------+

- Controller: Checklist.php
- View: checklist_hc_view.php
- ViewModel: Checklist_HC.js

Check list OD
~~~~~~~~~~~~~

Table diagram

::

  +----------------+      +----------------------+
  |                |      |                      |
  | tblChecklistOD |-----<| tblChecklistODDetail |
  |                |      |                      |
  +----------------+      +----------------------+

- Controller: Checklist.php
- View: checklist_od_view.php
- ViewModel: Checklist_OD.js

Check list EPI
~~~~~~~~~~~~~~

Table diagram

::

  +-----------------+      +-----------------------+
  |                 |      |                       |
  | tblChecklistEPI |-----<| tblChecklistEPIDetail |
  |                 |      |                       |
  +-----------------+      +-----------------------+

- Controller: Checklist.php
- View: checklist_epi_view.php
- ViewModel: Checklist_EPI.js

Stock
=====

Stock request
-------------

Table diagram

::

  +------------+      +------------+
  |            |      |            |
  | tblStockV2 |-----<| tblHFCodes |
  |            |      |            |
  +------------+      +------------+

- Controller: Stock.php

  - ``request()`` view UI of stock request.
  - ``getRequest()`` get stock request data.
  - ``getDetail()`` get detail stock item of hc.
  - ``offer()`` confirm stock offer.
- View: stockrequest_view.php
- ViewModel: StockRequest.js

Stock Data
----------

Stock HC
~~~~~~~~

::

  +------------+      +------------+
  |            |      |            |
  | tblStockV2 |-----<| tblHFCodes |
  |            |      |            |
  +------------+      +------------+

- Controller: Stock.php

  - ``report()`` view UI of stock data.
  - ``getReportHF()`` get month of report.
  - ``getReportDetailHF()`` get detail sotck item data.
  - ``exportExcel()`` export to excel.
  - ``saveStockHF()`` Insert/Update stock data.

  ::

    if (Rec_ID == 0)
      Insert()
    else Update()  

- View: stockreport_view.php
- ViewModel: StockReport.js

Stock OD
~~~~~~~~

::

  +------------+      +------------+
  |            |      |            |
  | tblStockOD |-----<|    tblOD   |
  |            |      |            |
  +------------+      +------------+

- Controller: Stock.php

  - ``report()`` view UI of stock data.
  - ``getReportOD()`` get month of report.
  - ``getReportDetailOD()`` get detail sotck item data.
  - ``exportExcel()`` export to excel.
  - ``saveStockOD()`` Insert/Update stock data.

  ::
    
    if (Rec_ID == 0)
      Insert()
    else Update()  

- View: stockreport_view.php
- ViewModel: StockReport.js

Stock CNM
---------

Table diagram

::

  +-------------+
  |             |
  | tblStockCNM |
  |             |
  +-------------+

- Controller: Stock.php

  - ``report()`` view UI of stock data.
  - ``getReportCNM()`` get month of report.
  - ``getReportDetailCNM()`` get detail sotck item data.
  - ``exportExcel()`` export to excel.
  - ``saveStockCNM()`` Insert/Update stock data.

  ::
    
    if (Rec_ID == 0)
      Insert()
    else Update()  

- View: stockreportcnm_view.php
- ViewModel: StockReportCNM.js  

Stock item
----------
- System: tool for admin to set up stock item (which item is for OD/HC)
- Actor: Admin
- Scenario: Admin use this tool to Insert/update/Setup stock item.

Table diagram

::

  +--------------+
  |              |
  | tblStockItem |
  |              |
  +--------------+

- Controller: Stock.php

  - ``item()`` view UI of stock data.
  - ``getItem()`` get month of report.
  - ``saveItem()`` Insert/Update stock data.

  ::
    
    if (Id == 0)
      Insert()
    else Update()  

- View: stockitem_view.php
- ViewModel: StockItem.js

Report
======

Dashboard
---------

- Controller: Dashboard.php
- Main View: dashboard_v2_view.php
- Sub view: 

  - dashboard_overview_view.php
  - dashboard_border_view.php
  - dashboard_intensification_view.php
  - dashboard_ipmappopup_view.php
  - dashbarod_map_view.php
  - dashboard_outbreak_view.php
  - dashbaord_overview_view.php
  - dashboard_pfmap_view.php
  - dashboard_stock_view.php
  - dashboard_surveillance_view.php
  - dashboard_table_view.php

- Main ViewModel: Dashboard.js
- Sub ViewModel: 
  
  - Dashboard_Border.js
  - Dashboard_Intensification.js
  - Dashboard_Map.js
  - Dashboard_Outbreak.js
  - Dashboard_PFMap.js
  - Dashboard_Overview.js
  - Dashboard_Stock.js

.. Note::

  We use store procedure to retrieve data

  To improve performance, first load data will read from file. all files is in ``root\media\Dashboard\Preload Data`` directory


Overview
~~~~~~~~

Insecticide Treated Net (ITN)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_OverviewNet``

National Surveillance data (55 ODs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_OverviewCase2``

Top 10 Villages having most cases by species
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_ChartTop30Vill``

Top 10 HFs having most cases by species
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_ChartTop30HF``

Treated malaria cases from HF and VMW by month
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_OverviewChart``

Severe malaria cases and deaths from HF by month
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_OverviewChart``

Malaria test results (HF, VMW) by species
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_OverviewChart``

Number of malaria-reported case and death by year
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_ChartCaseDeathSpecie``

Percentage of malaria cases by species and year
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_ChartCaseDeathSpecie``

Percentage of malaria cases by sex and age group
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_ChartSexAge``

Malaria Cases by Species, Provinces and Year
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_ChartSpecieProvince``

Malaria Incidence and Mortality Rate by Year and Provinces
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_ChartIncidentMortality``

Surveillance
~~~~~~~~~~~~

- Store procedure: ``SP_Dashboard_SurveillanceData2``

Stock
~~~~~

Current Stock HF Info by OD
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Count number of HF by status by OD (out of stock, low stock, Proper stock, congested stock)

- Store procedure: ``SP_Dashboard_Stock``

Current Stock HF info by Province
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Count number of HF by status by province (out of stock, low stock, Proper stock, congested stock)

- Store procedure: ``SP_Dashboard_Stock``

Malaria commodity map
^^^^^^^^^^^^^^^^^^^^^

Map of HF by status (out of stock, low stock, Proper stock, congested stock)

- Store procedure: ``SP_Dashboard_StockMap``

Current stock HF Item by OD
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Count balance of HF's item by OD.

- Store procedure: ``SP_Dashboard_Stock``

Current stock HF Item by province
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Count balance of HF's item by province.

- Store procedure: ``SP_Dashboard_Stock``

Top 30 HFs malaria commodity having most case
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Count RDT, ASMQ, PQ of HFs that having most case.

- Store procedure: ``SP_Dashboard_StockTop30HF``

Discrepancy between malaria cases and commodity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_StockDiscrepancy``

Border
~~~~~~

Trends in border areas
^^^^^^^^^^^^^^^^^^^^^^

number of malaria case of border (Lao, Thailand, Vietnam)

- Store procedure: ``SP_Dashboard_BorderChart``

Malaria cases by commune along the border
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_BorderMap``

Map
~~~~

Annual foci classification and monitoring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_MapFoci``

.. note::

  if duration of foci less than or equal to ``12 months`` then it is ``Active Focus``

  if duration of foci between ``13 months`` and ``36 months`` then it is ``Residual Focus``

  if duration of foci more than ``36 months`` this it is ``Cleared``


Malaria cases by OD
^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_ChartTop10OD``

Malaria hotspot by village
^^^^^^^^^^^^^^^^^^^^^^^^^^

Malaria hotspot by village for last 36 months
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_MapTop30Vill``

.. note::

  - step 1: total positive case by village.
  - step 2: top 30 villages by total positive cases by each month.
  - step 3: top 30 villages that most frequent from second step.

Malaria aber percentage by OD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_MapAber``

.. note:: 

  Aber = total test * 100 / total population

Malaria Incidence by OD
^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_MapODInc``

.. note::

  Incidence = total positive * 1000 / total population

Malaria API Map by Village
^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_APIByVillageMap``

.. note::

  - API = total postive * 1000 / total population
  - if village without population number then total population = 500
  - Annex village doesn't include.

Table
~~~~~~

Monthly malaria cases by species reported by provinces (55 ods)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_TableSpecieProvinceMonth``

Monthly severe malaria cases reported by provinces (55 ods)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_TableSevereMonth``

Number / percentage of malaria cases by age groups and sex by year (55 ods)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_TableAgeSex``

Number of malaria species by age groups and sex (55 ods)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_TableAgeSexSpecie``

Number of malaria severe cases by age groups and sex (55 ods)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_TableAgeSexSevere``

CNM Outbreak detection tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Store procedure: ``SP_Dashboard_OutbreakDetection``

PF Map
~~~~~~

Map
^^^

- Store procedure: ``SP_Dashboard_PFMap``

Number of places that have pf and mix cases
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_Dashboard_PFMapCount``

Reports
-------

- Controller: Report.php
- Model View: Report.js
- View: report_view.php

  Report are able filter by province, OD, Health center, Village, Year, Quarter, Month, Month from and Month to

VMW
~~~~

VMW Report Completeness
^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_V1_VMWReportCompleteness``

  show percentage of data that insert by VMW by month.

VMW Report timeline
^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_V1_VMWReportTimeline``

VMW Data accuracy
^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_V1_VMWDataAccuracy``

VMW Report Received
^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_V1_VMWReportReceived``

show number of report that report by VMW compare with number VMW.

VMW Data (summary)
^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_V1_VMWDataSummary``

Data of VMW sum by level of ``Province``, ``OD``, ``HF``.

.. note:: 
  - ``Passive = 1`` it means outreach

VMW Data (By village)
^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_V1_VMWDataByVillage``

Data of VMW sum by level of ``Province``, ``OD``, ``HF``, ``VMW village``

VMW Data by month
^^^^^^^^^^^^^^^^^

Data of VMW by Month 

- Store procedure: ``SP_V1_VMWDataByMonth``

Filter by:

- Pf + Pv + Mix
- Pf + Mix 
- Pf
- Pv
- Mix

Health Facility
~~~~~~~~~~~~~~~

HF Report Completeness
^^^^^^^^^^^^^^^^^^^^^^

Percentage of report by month

- Store procedure: ``SP_V1_HFReportCompleteness``

HF Report timeline
^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_V1_HFReportTimeline``

HF Report Accuracy
^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_V1_HFDataAccuracy``

HF Report Received
^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_V1_HFReportReceived``

HF Data (Summary)
^^^^^^^^^^^^^^^^^

Data of HF sum by level of ``Province``, ``OD``, ``HF``

- Store procedure: ``SP_V1_HFDataSummary``

HF Data (By Village)
^^^^^^^^^^^^^^^^^^^^

Data of HF sum by level of ``Province``, ``OD``, ``HF``, ``Village``

- Store procedure: ``SP_V1_HFDataByVillage``

HF Data by Month
^^^^^^^^^^^^^^^^

- Store procedure: ``SP_V1_HFDataByMonth``

Filter by:

- Pf + Pv + Mix
- Pf + Mix 
- Pf
- Pv
- Mix

HF + VMW
~~~~~~~~

Top 10 ODs having most cases
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Data of Top 10 ODs having most cases for current and last year

- Store procedure: ``SP_V1_HFVMWTop10OD``

Top 30 HFs Having Most Cases
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Data of top 30 HFs having most cases for current and last year.

- Store procedure: ``SP_V1_HFVMWTop30HF``

HFs having most cases (chart)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_V1_HFVMWTop30HFChart``

Parameter filter

  - Top 10
  - Top 20 
  - Top 30

Villages Having Most Cases (chart)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_V1_HFVMWTop30VillChart``

Parameter filter

  - Top 10
  - Top 20 
  - Top 30

HF + VMW Data (summary)
^^^^^^^^^^^^^^^^^^^^^^^^

Data of HF and VMW level by ``Province``, ``OD``, ``HF``

- Store procedure: ``SP_V1_HFVMWDataSummary``

Pv Radical Cure and Follow up
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_V1_HFVMWPvFollowup``

High Risk Villages
^^^^^^^^^^^^^^^^^^

- Store procedure: ``SP_V1_HighRiskVillage``

Bed Net
~~~~~~~

Bed Net by Province
^^^^^^^^^^^^^^^^^^^^

Parameter filter: 
  - All (value: all)
  - Mobile + Continue (value: mc)

- Store procedure: ``SP_V1_BedNetReport``

Bed Net by OD
^^^^^^^^^^^^^^

Parameter filter:
  -  By Filter (value: 1)
  -  Last 3 Years (value: 3)

- Store procedure: ``SP_V1_BedNetReport``