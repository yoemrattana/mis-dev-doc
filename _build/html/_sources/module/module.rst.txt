Module
======

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

- Controller: CaseReport.php
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
  |  |
  |  |__vmwcase_view.php
  |
  |__media
    |
    |__ViewModel
      |
      |__VMWCase.js

HC
--
Insert/Update/Delete HC case

Table diagram

::

  +---------------+        +------------------+
  |               |        |                  | 
  |tblHFActivity  |--------|tblHFActivityCases|
  |               |        |                  |
  +---------------+        +------------------+  

- Controller: CaseReport.php
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
  |  |
  |  |__hfcase_view.php
  |
  |__media
    |
    |__ViewModel
      |
      |__HFCase.js