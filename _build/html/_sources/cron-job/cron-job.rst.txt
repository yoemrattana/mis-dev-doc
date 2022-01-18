Cron Job
========

- To run cron job on windows server we need ``wget.exe``.
- Click here to `Download <http://gnuwin32.sourceforge.net/packages/wget.htm>`_

Setup cron job
--------------

#. Install ``wget.exe``
#. Go to :guilabel:`Task Scheduler`
#. Righ click on task area then click on :guilabel:`Create New Task`
#. Click on :guilabel:`Actions`
#. Click on :guilabel:`New...`
#. Click on :guilabel:`Browse...`> go to ``wget.exe`` (directory that installed wget.exe) > click on :guilabel:`Open`
#. In textbox :guilabel:`Add arguments (optional):` fill in URL of task, e.g: ``/cron/notifyVMWFU/Day3``

List of cron job
----------------

VMW follow up patient notification (Pv radical cure)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Purpose: Send message notification to VMW's smart phone about date of follow up.
- Type: run everyday.
- URL ``/cron/notifyVMWFU/parameter``
- **parameter** (*string*) -- :guilabel:`Day3` / :guilabel:`Day7` / :guilabel:`Day14`.

HC follow up patient notification (Pv radical cure)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Purpose: Send message notification to HC's tablet about follow up.
- Type: run everyday.
- URL ``/cron/notifyHFFU/parameter``
- **parameter** (*string*) -- :guilabel:`Day3` / :guilabel:`Day7` / :guilabel:`Day14`.

Foci reminder notification
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Purpose: send message notification to VMW, HC, OD, PHD, CSO.
- Type: run everyday.
- URL ``/cron/remindFoci``

.. note::
  if malaria case that not yet do foci investigation in during 5 days, system will produce notification.

Reactive case reminder notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Purpose: send message notification to HC and VMW.
- Type: run everyday.
- URL ``/cron/remindReactive``

.. note::
  if malaria case that not yet do reactive case in during 3 days, system will produce notification.

Hight risk village reminder notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Purpose: send message notification to HC, OD, PHP, CSO.
- Type: run every.
- URL ``/cron/remindHighRiskVillage``

.. note::
  - Retrieve positive last 12 months.
  - Retrieve positive last month.
  - Calculate STD, AVG.
  - If Positive last month > STD + AVG => High risk.

Stock out notification
~~~~~~~~~~~~~~~~~~~~~~

- Purpose: send message notification to OD, PHP, CSO
- Type: run everyday.
- URL ``/cron/notifyNonStock``