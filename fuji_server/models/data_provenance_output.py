# SPDX-FileCopyrightText: 2020 PANGAEA (https://www.pangaea.de/)
#
# SPDX-License-Identifier: MIT

from fuji_server import util
from fuji_server.models.base_model_ import Model
from fuji_server.models.data_provenance_output_inner import DataProvenanceOutputInner


class DataProvenanceOutput(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self,
        provenance_metadata_included: DataProvenanceOutputInner = None,
        structured_provenance_available: DataProvenanceOutputInner = None,
    ):
        """DataProvenanceOutput - a model defined in Swagger

        :param provenance_metadata_included: The provenance_metadata_included of this DataProvenanceOutput.  # noqa: E501
        :type provenance_metadata_included: DataProvenanceOutputInner
        :param structured_provenance_available: The structured_provenance_available of this DataProvenanceOutput.  # noqa: E501
        :type structured_provenance_available: DataProvenanceOutputInner
        """
        self.swagger_types = {
            "provenance_metadata_included": DataProvenanceOutputInner,
            "structured_provenance_available": DataProvenanceOutputInner,
        }

        self.attribute_map = {
            "provenance_metadata_included": "provenance_metadata_included",
            "structured_provenance_available": "structured_provenance_available",
        }
        self._provenance_metadata_included = provenance_metadata_included
        self._structured_provenance_available = structured_provenance_available

    @classmethod
    def from_dict(cls, dikt) -> "DataProvenanceOutput":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DataProvenance_output of this DataProvenanceOutput.  # noqa: E501
        :rtype: DataProvenanceOutput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def provenance_metadata_included(self) -> DataProvenanceOutputInner:
        """Gets the provenance_metadata_included of this DataProvenanceOutput.


        :return: The provenance_metadata_included of this DataProvenanceOutput.
        :rtype: DataProvenanceOutputInner
        """
        return self._provenance_metadata_included

    @provenance_metadata_included.setter
    def provenance_metadata_included(self, provenance_metadata_included: DataProvenanceOutputInner):
        """Sets the provenance_metadata_included of this DataProvenanceOutput.


        :param provenance_metadata_included: The provenance_metadata_included of this DataProvenanceOutput.
        :type provenance_metadata_included: DataProvenanceOutputInner
        """

        self._provenance_metadata_included = provenance_metadata_included

    @property
    def structured_provenance_available(self) -> DataProvenanceOutputInner:
        """Gets the structured_provenance_available of this DataProvenanceOutput.


        :return: The structured_provenance_available of this DataProvenanceOutput.
        :rtype: DataProvenanceOutputInner
        """
        return self._structured_provenance_available

    @structured_provenance_available.setter
    def structured_provenance_available(self, structured_provenance_available: DataProvenanceOutputInner):
        """Sets the structured_provenance_available of this DataProvenanceOutput.


        :param structured_provenance_available: The structured_provenance_available of this DataProvenanceOutput.
        :type structured_provenance_available: DataProvenanceOutputInner
        """

        self._structured_provenance_available = structured_provenance_available
