# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from future import standard_library
standard_library.install_aliases()
from builtins import range
import re
from random import choice
from time import sleep

from pyload.network.request import get_url


def get_ip(n=10):
    """
    Retrieve current ip. try n times for n seconds.
    """
    services = [
        ("http://checkip.dyndns.org", r".*Current IP Address: (\S+)</body>.*"),
        ("http://myexternalip.com/raw", r"(\S+)"),
        ("http://icanhazip.com", r"(\S+)"),
        ("http://ifconfig.me/ip", r"(\S+)")
    ]

    ip = ""
    for i in range(n):
        try:
            sv = choice(services)
            ip = get_url(sv[0])
            ip = re.match(sv[1], ip).group(1)
            break
        except Exception:
            ip = ""
            sleep(1)

    return ip
