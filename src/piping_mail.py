#!/opt/lastlist/apps/python/venv3/bin/python3

from parseMail import mail_parse
import sys
import logging
from logging.handlers import RotatingFileHandler

h = RotatingFileHandler('/home/developer/newdev/logs/mailIn.log',
                        maxBytes=100000000, backupCount=12)
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
logger.addHandler(h)


class SendGrid():
    def __init__(self, hostname='localhost')
        self.hostname = hostname

    def send_mail(self, parsed_mail):
        logger.debug(parsed_mail)


data = []
try:
    for line in sys.stdin:
        data.append(line)

    sg = SendGrid()
    emailMsg = ''.join(data)
    pm = mail_parse(emailMsg)
    logger.debug(pm)
    sg.send_mail(emailMsg)


except Exception as exp:
    logger.exception( exp )