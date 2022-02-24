import string
import random
from django.conf import settings

SIZE = getattr(settings, "RANDOM_ID_SIZE")


def random_id(size=10):
    size = SIZE
    chars = string.ascii_uppercase + string.digits
    return "".join(random.choice(chars) for _ in range(size))
