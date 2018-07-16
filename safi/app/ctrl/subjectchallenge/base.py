"""Contains the base class for :class:`SubjectChallengeCtrl`."""
from sq.ctrl import EndpointCtrl

class BaseSubjectChallengeCtrl(EndpointCtrl):
    """Generated by SG to serve as an abstract base class for:

        safi.app.ctrl.SubjectChallengeCtrl

    This class encapsulates external dependencies (such as the inversion-of-control
    requirements) and specifies the interface for the concrete implementation.
    """

    async def get(self, request, *args, **kwargs):
        """This method specifies the signature for :meth:`SubjectChallengeCtrl.get()`
        and should be implemented in the following file:

            ./safi/ctrl/subjectchallenge/impl.py
        """
        raise NotImplementedError("Subclasses must override this method.")


#pylint: skip-file
# !!! SG MANAGED FILE -- DO NOT EDIT -- VERSION:  !!!
