# -*- coding: utf-8 -*-
import os
print('Process(%s) start...' % os.getpid())
pid = os.fork()
