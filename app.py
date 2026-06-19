from ecosortvision.logger import logging
from ecosortvision.exception import AppException
import sys

try:
    a = 3 / "s"

except Exception as e:
        raise AppException(e, sys)