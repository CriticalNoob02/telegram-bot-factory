import logging
import os
from rich.logging import RichHandler

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
format = "%(message)s"

logging.basicConfig(
    level=LOG_LEVEL,
    format=format,
    datefmt="[%X]",
    handlers=[RichHandler()]
)

LOG = logging.getLogger("rich")
