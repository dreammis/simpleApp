import requests
import logging
try:
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    url = 'http://8.cqwt.crsky.com/201601/RouterOS6X-v2.1.zip'
    r =requests.get(url)
    logging.debug('malgebide')
    logging.info('malgebidetoo')
    logging.warning('caonima')

except:
    print 'malegebide shibaile!!!!!!'
