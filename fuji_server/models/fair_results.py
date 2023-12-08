from datetime import datetime

# from fuji_server.models.any_of_fair_results_results_items import AnyOfFAIRResultsResultsItems
from fuji_server import util
from fuji_server.models.any_of_fair_results_items import AnyOfFAIRResultsResultsItems
from fuji_server.models.base_model_ import Model


class FAIRResults(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self,
        test_id: str | None = None,
        request: dict | None = None,
        resolved_url: str | None = None,
        start_timestamp: datetime | None = None,
        end_timestamp: datetime | None = None,
        expiry_timestamp: datetime | None = None,
        metric_specification: str | None = None,
        metric_version: str | None = None,
        software_version: str | None = None,
        total_metrics: int | None = None,
        summary: dict | None = None,
        results: list[AnyOfFAIRResultsResultsItems] | None = None,
    ):
        """FAIRResults - a model defined in Swagger

        :param test_id: The test_id of this FAIRResults.  # noqa: E501
        :type test_id: str
        :param request: The request of this FAIRResults.  # noqa: E501
        :type request: Dict
        :param resolved_url: The resolved_url of this FAIRResults.  # noqa: E501
        :type resolved_url: str
        :param start_timestamp: The start_timestamp of this FAIRResults.  # noqa: E501
        :type start_timestamp: datetime
        :param end_timestamp: The end_timestamp of this FAIRResults.  # noqa: E501
        :type end_timestamp: datetime
        :param expiry_timestamp: The expiry_timestamp of this FAIRResults.  # noqa: E501
        :type expiry_timestamp: datetime
        :param metric_specification: The metric_specification of this FAIRResults.  # noqa: E501
        :type metric_specification: str
        :param metric_version: The metric_version of this FAIRResults.  # noqa: E501
        :type metric_version: str
        :param software_version: The software_version of this FAIRResults.  # noqa: E501
        :type software_version: str
        :param total_metrics: The total_metrics of this FAIRResults.  # noqa: E501
        :type total_metrics: int
        :param summary: The summary of this FAIRResults.  # noqa: E501
        :type summary: Dict
        :param results: The results of this FAIRResults.  # noqa: E501
        :type results: List[AnyOfFAIRResultsResultsItems]
        """
        self.swagger_types = {
            "test_id": str,
            "request": dict,
            "resolved_url": str,
            "start_timestamp": datetime,
            "end_timestamp": datetime,
            "expiry_timestamp": datetime,
            "metric_specification": str,
            "metric_version": str,
            "software_version": str,
            "total_metrics": int,
            "summary": dict,
            "results": list[AnyOfFAIRResultsResultsItems],
        }

        self.attribute_map = {
            "test_id": "test_id",
            "request": "request",
            "resolved_url": "resolved_url",
            "start_timestamp": "start_timestamp",
            "end_timestamp": "end_timestamp",
            "expiry_timestamp": "expiry_timestamp",
            "metric_specification": "metric_specification",
            "metric_version": "metric_version",
            "software_version": "software_version",
            "total_metrics": "total_metrics",
            "summary": "summary",
            "results": "results",
        }
        self._test_id = test_id
        self._request = request
        self._resolved_url = resolved_url
        self._start_timestamp = start_timestamp
        self._end_timestamp = end_timestamp
        self._expiry_timestamp = expiry_timestamp
        self._metric_specification = metric_specification
        self._metric_version = metric_version
        self._software_version = software_version
        self._total_metrics = total_metrics
        self._summary = summary
        self._results = results

    @classmethod
    def from_dict(cls, dikt) -> "FAIRResults":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FAIRResults of this FAIRResults.  # noqa: E501
        :rtype: FAIRResults
        """
        return util.deserialize_model(dikt, cls)

    @property
    def test_id(self) -> str:
        """Gets the test_id of this FAIRResults.


        :return: The test_id of this FAIRResults.
        :rtype: str
        """
        return self._test_id

    @test_id.setter
    def test_id(self, test_id: str):
        """Sets the test_id of this FAIRResults.


        :param test_id: The test_id of this FAIRResults.
        :type test_id: str
        """

        self._test_id = test_id

    @property
    def request(self) -> dict:
        """Gets the request of this FAIRResults.


        :return: The request of this FAIRResults.
        :rtype: Dict
        """
        return self._request

    @request.setter
    def request(self, request: dict):
        """Sets the request of this FAIRResults.


        :param request: The request of this FAIRResults.
        :type request: Dict
        """

        self._request = request

    @property
    def resolved_url(self) -> str:
        """Gets the resolved_url of this FAIRResults.


        :return: The resolved_url of this FAIRResults.
        :rtype: str
        """
        return self._resolved_url

    @resolved_url.setter
    def resolved_url(self, resolved_url: str):
        """Sets the resolved_url of this FAIRResults.


        :param resolved_url: The resolved_url of this FAIRResults.
        :type resolved_url: str
        """

        self._resolved_url = resolved_url

    @property
    def start_timestamp(self) -> datetime:
        """Gets the start_timestamp of this FAIRResults.


        :return: The start_timestamp of this FAIRResults.
        :rtype: datetime
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp: datetime):
        """Sets the start_timestamp of this FAIRResults.


        :param start_timestamp: The start_timestamp of this FAIRResults.
        :type start_timestamp: datetime
        """

        self._start_timestamp = start_timestamp

    @property
    def end_timestamp(self) -> datetime:
        """Gets the end_timestamp of this FAIRResults.


        :return: The end_timestamp of this FAIRResults.
        :rtype: datetime
        """
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp: datetime):
        """Sets the end_timestamp of this FAIRResults.


        :param end_timestamp: The end_timestamp of this FAIRResults.
        :type end_timestamp: datetime
        """

        self._end_timestamp = end_timestamp

    @property
    def expiry_timestamp(self) -> datetime:
        """Gets the expiry_timestamp of this FAIRResults.


        :return: The expiry_timestamp of this FAIRResults.
        :rtype: datetime
        """
        return self._expiry_timestamp

    @expiry_timestamp.setter
    def expiry_timestamp(self, expiry_timestamp: datetime):
        """Sets the expiry_timestamp of this FAIRResults.


        :param expiry_timestamp: The expiry_timestamp of this FAIRResults.
        :type expiry_timestamp: datetime
        """

        self._expiry_timestamp = expiry_timestamp

    @property
    def metric_specification(self) -> str:
        """Gets the metric_specification of this FAIRResults.


        :return: The metric_specification of this FAIRResults.
        :rtype: str
        """
        return self._metric_specification

    @metric_specification.setter
    def metric_specification(self, metric_specification: str):
        """Sets the metric_specification of this FAIRResults.


        :param metric_specification: The metric_specification of this FAIRResults.
        :type metric_specification: str
        """

        self._metric_specification = metric_specification

    @property
    def metric_version(self) -> str:
        """Gets the metric_version of this FAIRResults.


        :return: The metric_version of this FAIRResults.
        :rtype: str
        """
        return self._metric_version

    @metric_version.setter
    def metric_version(self, metric_version: str):
        """Sets the metric_version of this FAIRResults.


        :param metric_version: The metric_version of this FAIRResults.
        :type metric_version: str
        """

        self._metric_version = metric_version

    @property
    def software_version(self) -> str:
        """Gets the software_version of this FAIRResults.


        :return: The software_version of this FAIRResults.
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version: str):
        """Sets the software_version of this FAIRResults.


        :param software_version: The software_version of this FAIRResults.
        :type software_version: str
        """

        self._software_version = software_version

    @property
    def total_metrics(self) -> int:
        """Gets the total_metrics of this FAIRResults.


        :return: The total_metrics of this FAIRResults.
        :rtype: int
        """
        return self._total_metrics

    @total_metrics.setter
    def total_metrics(self, total_metrics: int):
        """Sets the total_metrics of this FAIRResults.


        :param total_metrics: The total_metrics of this FAIRResults.
        :type total_metrics: int
        """

        self._total_metrics = total_metrics

    @property
    def summary(self) -> dict:
        """Gets the summary of this FAIRResults.


        :return: The summary of this FAIRResults.
        :rtype: Dict
        """
        return self._summary

    @summary.setter
    def summary(self, summary: dict):
        """Sets the summary of this FAIRResults.


        :param summary: The summary of this FAIRResults.
        :type summary: Dict
        """

        self._summary = summary

    @property
    def results(self) -> list[AnyOfFAIRResultsResultsItems]:
        """Gets the results of this FAIRResults.


        :return: The results of this FAIRResults.
        :rtype: List[AnyOfFAIRResultsResultsItems]
        """
        return self._results

    @results.setter
    def results(self, results: list[AnyOfFAIRResultsResultsItems]):
        """Sets the results of this FAIRResults.


        :param results: The results of this FAIRResults.
        :type results: List[AnyOfFAIRResultsResultsItems]
        """

        self._results = results
