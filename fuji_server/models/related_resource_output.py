from fuji_server import util
from fuji_server.models.base_model_ import Model
from fuji_server.models.related_resource_output_inner import RelatedResourceOutputInner  # noqa: F401


class RelatedResourceOutput(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self):
        """RelatedResourceOutput - a model defined in Swagger"""
        self.swagger_types = {}

        self.attribute_map = {}

    @classmethod
    def from_dict(cls, dikt) -> "RelatedResourceOutput":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RelatedResource_output of this RelatedResourceOutput.  # noqa: E501
        :rtype: RelatedResourceOutput
        """
        return util.deserialize_model(dikt, cls)
