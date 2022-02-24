import os
import logging
from src.switch import use_settings
#use_settings = "dev"

if use_settings  == "dev":
    from .dev import *
    logging.warn("You are using development settings if you are using it in production server please switch to production settings")
elif use_settings == "prod":
    from .production import *
    logging.warn("Production settings")
