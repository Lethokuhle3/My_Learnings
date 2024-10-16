**LOGGING**

logging module is a great way to keep track of events in your program. It helps you identify issues, understand program flow, and can be invaluable for troubleshooting in production environments. You can further customize logging by creating loggers, handlers, and formatters as needed!

>>import logging

```py
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
```

Log messages: You can log messages at different severity levels:

DEBUG: Detailed information, typically for diagnosing problems.
INFO: General information about the program's operation.
WARNING: An indication that something unexpected happened, but the program is still working.
ERROR: A serious problem that prevented the program from performing a function.
CRITICAL: A very serious error that may prevent the program from continuing to run.

```py
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Log messages at various levels
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

#This is the output 

2024-10-13 12:00:00,000 - DEBUG - This is a debug message
2024-10-13 12:00:00,000 - INFO - This is an info message
2024-10-13 12:00:00,000 - WARNING - This is a warning message
2024-10-13 12:00:00,000 - ERROR - This is an error message
2024-10-13 12:00:00,000 - CRITICAL - This is a critical message

```

You can also log messages to a file instead of the console.
```py
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Log messages
logging.info("Logging to a file!")
```


