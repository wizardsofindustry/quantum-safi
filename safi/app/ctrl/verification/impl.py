"""Contains the concrete implementation of :class:`BaseVerificationCtrl`."""
from .base import BaseVerificationCtrl


class VerificationCtrl(BaseVerificationCtrl):
    """Authenticates Subjects using a TOTP/HOTP."""

    async def post(self, request, *args, **kwargs):
        self.otp.verify(kwargs.get('kind', 'totp'), **request.payload)
        return self.render_to_response({})