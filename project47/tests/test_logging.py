

'''

import logging
def test_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("Test started")
    logging.info("Opening application")
    assert True
    logging.info("Test completed")
    '''
#============================================================
#============================================================

import logging
def test_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s" 
    )
    logging.info("Test Started")
    logging.info("Openinig application")
    assert True
    logging.info("Test completed")