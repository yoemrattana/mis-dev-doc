Module
++++++

VMW
===

::

                                      +-----------+
                                +-----| Load Bal  |------+
                                |     +-----------+      |
                                |                        |
                           +---------+              +---------+
       +-------------+     |         |              |         |    +--------------+
       |             |-----| Nginx   |              | Nginx   |----|              |
       |  File       |     +---------+              +---------+    |  File        |
       |  System     |          |                        |         |  System      |
       +-------------+     +---------+  +--------+  +---------+    +--------------+
              |  |         |Gunicorn |  |        |  |Gunicorn |        |   |
              |  +---------|(Django) |--|Postgres|--|(Django) |--------+   |
              |            +---------+  +--------+  +---------+            |
              |                 |                        |                 |
              |                 |                        |                 |
              |                 -----------API------------                 |
              |                             |                              |
              |                             |                              |
              |                     +------------------+                   |
              |                     |                  |                   |
              +---------------------|  Build Server    |-------------------+
                                    |                  |
                                    +------------------+


HC
==