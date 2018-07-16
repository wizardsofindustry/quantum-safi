"""Declares :class:`SubjectFinder`."""
import sqlalchemy

from ...orm import OneTimePassword
from .base import BaseSubjectFinder


class SubjectFinder(BaseSubjectFinder):
    """Provides an API to retrieve information on **Factors** in relation to a
    specific **Subject**.
    """

    def available_challenges(self, gsid):
        """Returns a Data Transfer Object (DTO) containing the factors that are
        available for interim authentication challenges against the Subject
        identified by string `gsid`.
        """
        sub1 = sqlalchemy.select([sqlalchemy.literal('otp').label('type')])\
            .where(OneTimePassword.gsid == gsid)\
            .alias('otp')

        return self.dto(factors=[row.type for row in self.session.query(sub1)])