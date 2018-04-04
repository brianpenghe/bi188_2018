#! /usr/bin/env python

"""
    MoinMoin - CGI Driver Script

    Copyright (c) 2000 by J�rgen Hermann <jh@web.de>
    All rights reserved, see COPYING for details.

    $Id: moin.cgi,v 1.3 2002/11/25 20:23:08 jhermann Exp $
"""

#import sys
#sys.path.append('/usr/local/home/USERNAME/lib/python')

import os
if os.environ.get('QUERY_STRING') == 'test':
    print "Content-Type: text/plain\n\nMoinMoin CGI Diagnosis\n======================\n"

    try:
        from MoinMoin import cgimain
        print 'Package "MoinMoin" successfully imported.\n'
        cgimain.test()
    except:
        import sys, traceback, string, pprint
        type, value, tb = sys.exc_info()
        if type == ImportError:
            print 'Your PYTHONPATH is:\n%s' % pprint.pformat(sys.path)
        print "\nTraceback (innermost last):\n%s" % string.join(
            traceback.format_tb(tb) + traceback.format_exception_only(type, value))
else:
    from MoinMoin import cgimain
    cgimain.run()

