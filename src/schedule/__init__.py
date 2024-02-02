import logging

from initialization import action_loader
from utils import get_summary


def get_action_with_summary(action):
    """Given an action, return the string 'action_name - summary'."""
    action_fn = action_loader.actions[action]
    summary = get_summary(action_fn)
    action_with_summary = action
    if summary:
        action_with_summary += f" - {summary}"

    return action_with_summary


logger = logging.getLogger(__name__)
logger.debug("********** Initializing schedule **********")
