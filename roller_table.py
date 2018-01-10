#!/usr/bin/python

import time
import os
import subprocess
import logging
import sys
import datetime

from datetime import datetime
from dateutil.relativedelta import relativedelta

date_after_day = datetime.today()+ relativedelta(days=1)
date  = date_after_day.strftime('%Y-%m-%d')

date_after_day = datetime.today()+ relativedelta(days=1)
padate = date_after_day.strftime('%Y%m%d')

date_after_day = datetime.today()+ relativedelta(days=2)
padate1 = date_after_day.strftime('%Y-%m-%d')


date_after_day = datetime.today()+ relativedelta(days=-8)
padate15 = date_after_day.strftime('%Y%m%d')


print "CREATE PARTITION FOR TOMORROW"

os.system('/usr/bin/mysql -u root -pyourpasswd -e "ALTER TABLE adtag_trans.log_adtag reorganize PARTITION pmax into (PARTITION p' + padate + ' VALUES LESS THAN (' + padate1 + '),partition pmax values less than (MAXVALUE));"')
print 'NEW PARTITION p' + padate + ' IS READY'
print "DELETE PARTITION OLDER THAN 15 DAYS"
os.system('/usr/bin/mysql -u root -pyourpasswd -e "ALTER TABLE adtag_trans.log_adtag truncate partition P' + padate15 +';"')
print 'PARTITION p' + padate15 + '  HAS BEEN DELETE'



print "CREATE PARTITION FOR TOMORROW"
os.system('/usr/bin/mysql -u root -pyourpasswd -e "ALTER TABLE adtag_trans.log_trace reorganize PARTITION pmax into (PARTITION p' + padate + ' VALUES LESS THAN (' + padate1 + '),partition pmax values less than (MAXVALUE));"')
print 'NEW PARTITION p' + padate + ' IS READY'
print "DELETE PARTITION OLDER THAN 15 DAYS"
os.system('/usr/bin/mysql -u root -pyourpasswd -e "ALTER TABLE adtag_trans.log_trace truncate partition P' + padate15 +';"')
print 'PARTITION p' + padate15 + '  HAS BEEN DELETE'



print "CREATE PARTITION FOR TOMORROW"
os.system('/usr/bin/mysql -u root -pyourpasswd -e "ALTER TABLE adtag_trans.log_trace_adtaganalyzer reorganize PARTITION pmax into (PARTITION p' + padate + ' VALUES LESS THAN (' + padate1 + '),partition pmax values less than (MAXVALUE));"')
print 'NEW PARTITION p' + padate + ' IS READY'
print "DELETE PARTITION OLDER THAN 15 DAYS"
os.system('/usr/bin/mysql -u root -pyourpasswd -e "ALTER TABLE adtag_trans.log_trace_adtaganalyzer truncate partition P' + padate15 +';"')
print 'PARTITION p' + padate15 + '  HAS BEEN DELETE'

