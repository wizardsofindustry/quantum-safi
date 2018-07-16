"""Contains all controller implementations that are used by the WSGI
appication. See also :class:`~otp.app.wsgi.application.WSGIApplication`.
"""
from .onetimepassword import OneTimePasswordCtrl
from .verification import VerificationCtrl