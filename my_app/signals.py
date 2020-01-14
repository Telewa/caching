from django.core.cache import cache
from structlog import get_logger


def flag_updated(sender, instance, **kwargs):
    """
    This receiver will invalidate the key in the cache, forcing the value to be reloaded from db

    :param sender:  The class that sent the signal
    :param instance:    The new data instance
    :param kwargs:  AOB
    :return:    nothing
    """
    logger = get_logger(__file__)
    logger.info(f"invalidating the cache: {instance.name} updated to {instance.enabled}")

    # invalidate the key in cache
    cache.delete(instance.name)
