import logging

logging.basicConfig(filename="mybugs.log",
                    filemode="a", 
                    format="(time = %(asctime)s) {Log_name = %(name)s} {level_name = %(levelname)s} --> message = %(message)s <--",
                    datefmt="%d / %B / %Y :%H %M %S")


mylogger = logging.getLogger("ugn_Logger")


mylogger.error("This Is Error Message")

mylogger.warning("This Is Warning Message")

mylogger.critical("This Is Critical Message")