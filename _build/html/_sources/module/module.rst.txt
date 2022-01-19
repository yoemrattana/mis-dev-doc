VMW
~~~~
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

HC
~~~~
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