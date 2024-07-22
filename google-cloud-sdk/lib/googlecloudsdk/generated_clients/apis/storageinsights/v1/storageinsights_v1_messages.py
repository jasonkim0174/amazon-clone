"""Generated message classes for storageinsights version v1.

"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'storageinsights'


class CSVOptions(_messages.Message):
  r"""Options to configure CSV formatted reports.

  Fields:
    delimiter: Delimiter characters in CSV.
    headerRequired: If set, will include a header row in the CSV report.
    recordSeparator: Record separator characters in CSV.
  """

  delimiter = _messages.StringField(1)
  headerRequired = _messages.BooleanField(2)
  recordSeparator = _messages.StringField(3)


class CancelOperationRequest(_messages.Message):
  r"""The request message for Operations.CancelOperation."""


class CloudStorageDestinationOptions(_messages.Message):
  r"""Options to store reports in storage systems. Next ID: 3

  Fields:
    bucket: Destination bucket.
    destinationPath: Destination path is the path in the bucket where the
      report should be generated.
  """

  bucket = _messages.StringField(1)
  destinationPath = _messages.StringField(2)


class CloudStorageFilters(_messages.Message):
  r"""Options to filter data on storage systems. Next ID: 2

  Fields:
    bucket: Bucket for which the report will be generated.
  """

  bucket = _messages.StringField(1)


class Date(_messages.Message):
  r"""Represents a whole or partial calendar date, such as a birthday. The
  time of day and time zone are either specified elsewhere or are
  insignificant. The date is relative to the Gregorian Calendar. This can
  represent one of the following: * A full date, with non-zero year, month,
  and day values. * A month and day, with a zero year (for example, an
  anniversary). * A year on its own, with a zero month and a zero day. * A
  year and month, with a zero day (for example, a credit card expiration
  date). Related types: * google.type.TimeOfDay * google.type.DateTime *
  google.protobuf.Timestamp

  Fields:
    day: Day of a month. Must be from 1 to 31 and valid for the year and
      month, or 0 to specify a year by itself or a year and month where the
      day isn't significant.
    month: Month of a year. Must be from 1 to 12, or 0 to specify a year
      without a month and day.
    year: Year of the date. Must be from 1 to 9999, or 0 to specify a date
      without a year.
  """

  day = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  month = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  year = _messages.IntegerField(3, variant=_messages.Variant.INT32)


class DateTime(_messages.Message):
  r"""Represents civil time (or occasionally physical time). This type can
  represent a civil time in one of a few possible ways: * When utc_offset is
  set and time_zone is unset: a civil time on a calendar day with a particular
  offset from UTC. * When time_zone is set and utc_offset is unset: a civil
  time on a calendar day in a particular time zone. * When neither time_zone
  nor utc_offset is set: a civil time on a calendar day in local time. The
  date is relative to the Proleptic Gregorian Calendar. If year, month, or day
  are 0, the DateTime is considered not to have a specific year, month, or day
  respectively. This type may also be used to represent a physical time if all
  the date and time fields are set and either case of the `time_offset` oneof
  is set. Consider using `Timestamp` message for physical time instead. If
  your use case also would like to store the user's timezone, that can be done
  in another field. This type is more flexible than some applications may
  want. Make sure to document and validate your application's limitations.

  Fields:
    day: Optional. Day of month. Must be from 1 to 31 and valid for the year
      and month, or 0 if specifying a datetime without a day.
    hours: Optional. Hours of day in 24 hour format. Should be from 0 to 23,
      defaults to 0 (midnight). An API may choose to allow the value
      "24:00:00" for scenarios like business closing time.
    minutes: Optional. Minutes of hour of day. Must be from 0 to 59, defaults
      to 0.
    month: Optional. Month of year. Must be from 1 to 12, or 0 if specifying a
      datetime without a month.
    nanos: Optional. Fractions of seconds in nanoseconds. Must be from 0 to
      999,999,999, defaults to 0.
    seconds: Optional. Seconds of minutes of the time. Must normally be from 0
      to 59, defaults to 0. An API may allow the value 60 if it allows leap-
      seconds.
    timeZone: Time zone.
    utcOffset: UTC offset. Must be whole seconds, between -18 hours and +18
      hours. For example, a UTC offset of -4:00 would be represented as {
      seconds: -14400 }.
    year: Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a
      datetime without a year.
  """

  day = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  hours = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  minutes = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  month = _messages.IntegerField(4, variant=_messages.Variant.INT32)
  nanos = _messages.IntegerField(5, variant=_messages.Variant.INT32)
  seconds = _messages.IntegerField(6, variant=_messages.Variant.INT32)
  timeZone = _messages.MessageField('TimeZone', 7)
  utcOffset = _messages.StringField(8)
  year = _messages.IntegerField(9, variant=_messages.Variant.INT32)


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance: service Foo { rpc
  Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }
  """



class FrequencyOptions(_messages.Message):
  r"""ReportConfig Resource: Options to setup frequency of report generation.

  Enums:
    FrequencyValueValuesEnum: Frequency of report generation.

  Fields:
    endDate: The date on which report generation should stop (Inclusive). UTC
      time zone.
    frequency: Frequency of report generation.
    startDate: The date from which report generation should start. UTC time
      zone.
  """

  class FrequencyValueValuesEnum(_messages.Enum):
    r"""Frequency of report generation.

    Values:
      FREQUENCY_UNSPECIFIED: Unspecified.
      DAILY: Report will be generated daily.
      WEEKLY: Report will be generated weekly.
    """
    FREQUENCY_UNSPECIFIED = 0
    DAILY = 1
    WEEKLY = 2

  endDate = _messages.MessageField('Date', 1)
  frequency = _messages.EnumField('FrequencyValueValuesEnum', 2)
  startDate = _messages.MessageField('Date', 3)


class ListLocationsResponse(_messages.Message):
  r"""The response message for Locations.ListLocations.

  Fields:
    locations: A list of locations that matches the specified filter in the
      request.
    nextPageToken: The standard List next-page token.
  """

  locations = _messages.MessageField('Location', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListOperationsResponse(_messages.Message):
  r"""The response message for Operations.ListOperations.

  Fields:
    nextPageToken: The standard List next-page token.
    operations: A list of operations that matches the specified filter in the
      request.
  """

  nextPageToken = _messages.StringField(1)
  operations = _messages.MessageField('Operation', 2, repeated=True)


class ListReportConfigsResponse(_messages.Message):
  r"""Message for response to listing ReportConfigs

  Fields:
    nextPageToken: A token identifying a page of results the server should
      return.
    reportConfigs: The list of ReportConfig
    unreachable: Locations that could not be reached.
  """

  nextPageToken = _messages.StringField(1)
  reportConfigs = _messages.MessageField('ReportConfig', 2, repeated=True)
  unreachable = _messages.StringField(3, repeated=True)


class ListReportDetailsResponse(_messages.Message):
  r"""Message for response to listing ReportDetails

  Fields:
    nextPageToken: A token identifying a page of results the server should
      return.
    reportDetails: The list of ReportDetail
    unreachable: Locations that could not be reached.
  """

  nextPageToken = _messages.StringField(1)
  reportDetails = _messages.MessageField('ReportDetail', 2, repeated=True)
  unreachable = _messages.StringField(3, repeated=True)


class Location(_messages.Message):
  r"""A resource that represents Google Cloud Platform location.

  Messages:
    LabelsValue: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    MetadataValue: Service-specific metadata. For example the available
      capacity at the given location.

  Fields:
    displayName: The friendly name for this location, typically a nearby city
      name. For example, "Tokyo".
    labels: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    locationId: The canonical id for this location. For example: `"us-east1"`.
    metadata: Service-specific metadata. For example the available capacity at
      the given location.
    name: Resource name for the location, which may vary between
      implementations. For example: `"projects/example-project/locations/us-
      east1"`
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Cross-service attributes for the location. For example
    {"cloud.googleapis.com/region": "us-east1"}

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata. For example the available capacity at the
    given location.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  displayName = _messages.StringField(1)
  labels = _messages.MessageField('LabelsValue', 2)
  locationId = _messages.StringField(3)
  metadata = _messages.MessageField('MetadataValue', 4)
  name = _messages.StringField(5)


class Metrics(_messages.Message):
  r"""Different metrics associated with the generated report.

  Fields:
    processedRecordsCount: Count of Cloud Storage objects which are part of
      the report.
  """

  processedRecordsCount = _messages.IntegerField(1)


class ObjectMetadataReportOptions(_messages.Message):
  r"""Report specification for exporting object metadata. Next ID: 4

  Fields:
    metadataFields: Metadata fields to be included in the report.
    storageDestinationOptions: Cloud Storage as the storage system.
    storageFilters: Cloud Storage as the storage system.
  """

  metadataFields = _messages.StringField(1, repeated=True)
  storageDestinationOptions = _messages.MessageField('CloudStorageDestinationOptions', 2)
  storageFilters = _messages.MessageField('CloudStorageFilters', 3)


class Operation(_messages.Message):
  r"""This resource represents a long-running operation that is the result of
  a network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation. It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata. Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal response of the operation in case of success. If
      the original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`. If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource. For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name. For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation. It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata. Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should be a resource name ending with
      `operations/{unique_id}`.
    response: The normal response of the operation in case of success. If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`. If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource. For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name. For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata associated with the operation. It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata. Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    r"""The normal response of the operation in case of success. If the
    original method returns no data on success, such as `Delete`, the response
    is `google.protobuf.Empty`. If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource. For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name. For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class OperationMetadata(_messages.Message):
  r"""Represents the metadata of the long-running operation.

  Fields:
    apiVersion: Output only. API version used to start the operation.
    createTime: Output only. The time the operation was created.
    endTime: Output only. The time the operation finished running.
    requestedCancellation: Output only. Identifies whether the user has
      requested cancellation of the operation. Operations that have been
      cancelled successfully have Operation.error value with a
      google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.
    statusMessage: Output only. Human-readable status of the operation, if
      any.
    target: Output only. Server-defined resource path for the target of the
      operation.
    verb: Output only. Name of the verb executed by the operation.
  """

  apiVersion = _messages.StringField(1)
  createTime = _messages.StringField(2)
  endTime = _messages.StringField(3)
  requestedCancellation = _messages.BooleanField(4)
  statusMessage = _messages.StringField(5)
  target = _messages.StringField(6)
  verb = _messages.StringField(7)


class ParquetOptions(_messages.Message):
  r"""Options to configure Parquet formatted reports."""


class ReportConfig(_messages.Message):
  r"""Message describing ReportConfig object. ReportConfig is the
  configuration to generate reports. Next ID: 12

  Messages:
    LabelsValue: Labels as key value pairs

  Fields:
    createTime: Output only. [Output only] Create time stamp
    csvOptions: Options for CSV formatted reports.
    displayName: User provided display name which can be empty and limited to
      256 characters that is editable.
    frequencyOptions: The frequency of report generation.
    labels: Labels as key value pairs
    name: name of resource. It will be of form
      projects//locations//reportConfigs/.
    objectMetadataReportOptions: Report for exporting object metadata.
    parquetOptions: Options for Parquet formatted reports.
    updateTime: Output only. [Output only] Update time stamp
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Labels as key value pairs

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  createTime = _messages.StringField(1)
  csvOptions = _messages.MessageField('CSVOptions', 2)
  displayName = _messages.StringField(3)
  frequencyOptions = _messages.MessageField('FrequencyOptions', 4)
  labels = _messages.MessageField('LabelsValue', 5)
  name = _messages.StringField(6)
  objectMetadataReportOptions = _messages.MessageField('ObjectMetadataReportOptions', 7)
  parquetOptions = _messages.MessageField('ParquetOptions', 8)
  updateTime = _messages.StringField(9)


class ReportDetail(_messages.Message):
  r"""Message describing ReportDetail object. ReportDetail represents metadata
  of generated reports for a ReportConfig. Next ID: 10

  Messages:
    LabelsValue: Labels as key value pairs

  Fields:
    labels: Labels as key value pairs
    name: Name of resource. It will be of form
      projects//locations//reportConfigs//reportDetails/.
    reportMetrics: Metrics of the report.
    reportNames: Generated report's full path with name. It will be of the
      form destination_bucket//.
    reportPathPrefix: Prefix of the object name of each report's shard. This
      will have full prefix except the "extension" and "shard_id". For
      example, if the `destination_path` is "{{report-config-
      id}}/dt={{datetime}}", the shard object name would be "gs://my-insights/
      1A34-F2E456-12B456-1C3D/dt=2022-05-20T06:35/1A34-F2E456-12B456-
      1C3D_2022-05-20T06:35_5.csv" and the value of `report_path_prefix` field
      would be "gs://my-insights/1A34-F2E456-12B456-1C3D/dt=2022-05-
      20T06:35/1A34-F2E456-12B456-1C3D_2022-05-20T06:35_".
    shardsCount: Total shards generated for the report.
    snapshotTime: The snapshot time. All the report data is referenced at this
      point of time.
    status: Status of the ReportDetail.
    targetDatetime: The date for which report is generated. The time part of
      target_datetime will be zero till we support multiple reports per day.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Labels as key value pairs

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  labels = _messages.MessageField('LabelsValue', 1)
  name = _messages.StringField(2)
  reportMetrics = _messages.MessageField('Metrics', 3)
  reportNames = _messages.StringField(4, repeated=True)
  reportPathPrefix = _messages.StringField(5)
  shardsCount = _messages.IntegerField(6)
  snapshotTime = _messages.StringField(7)
  status = _messages.MessageField('Status', 8)
  targetDatetime = _messages.MessageField('DateTime', 9)


class ReportStatsView(_messages.Message):
  r"""Message to encapsulate the various statistics related to the generated
  Report Next ID: 6

  Fields:
    bytesWritten: Actual size in bytes for the report written, as reported by
      the underlying storage system
    projectNumber: Project Number
    recordsProcessed: Actual records processed as reported by the underlying
      storage system
    reportConfigId: ID of the parent ReportConfig for the corresponding
      ReportDetail
    reportDetailId: ID of the ReportDetail for which the stats are generated
  """

  bytesWritten = _messages.IntegerField(1)
  projectNumber = _messages.IntegerField(2)
  recordsProcessed = _messages.IntegerField(3)
  reportConfigId = _messages.StringField(4)
  reportDetailId = _messages.StringField(5)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default='json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class Status(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). Each `Status` message contains
  three pieces of data: error code, error message, and error details. You can
  find out more about this error model and how to work with it in the [API
  Design Guide](https://cloud.google.com/apis/design/errors).

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details. There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


class StorageinsightsProjectsLocationsGetRequest(_messages.Message):
  r"""A StorageinsightsProjectsLocationsGetRequest object.

  Fields:
    name: Resource name for the location.
  """

  name = _messages.StringField(1, required=True)


class StorageinsightsProjectsLocationsListRequest(_messages.Message):
  r"""A StorageinsightsProjectsLocationsListRequest object.

  Fields:
    filter: A filter to narrow down results to a preferred subset. The
      filtering language accepts strings like `"displayName=tokyo"`, and is
      documented in more detail in [AIP-160](https://google.aip.dev/160).
    name: The resource that owns the locations collection, if applicable.
    pageSize: The maximum number of results to return. If not set, the service
      selects a default.
    pageToken: A page token received from the `next_page_token` field in the
      response. Send that page token to receive the subsequent page.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class StorageinsightsProjectsLocationsOperationsCancelRequest(_messages.Message):
  r"""A StorageinsightsProjectsLocationsOperationsCancelRequest object.

  Fields:
    cancelOperationRequest: A CancelOperationRequest resource to be passed as
      the request body.
    name: The name of the operation resource to be cancelled.
  """

  cancelOperationRequest = _messages.MessageField('CancelOperationRequest', 1)
  name = _messages.StringField(2, required=True)


class StorageinsightsProjectsLocationsOperationsDeleteRequest(_messages.Message):
  r"""A StorageinsightsProjectsLocationsOperationsDeleteRequest object.

  Fields:
    name: The name of the operation resource to be deleted.
  """

  name = _messages.StringField(1, required=True)


class StorageinsightsProjectsLocationsOperationsGetRequest(_messages.Message):
  r"""A StorageinsightsProjectsLocationsOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class StorageinsightsProjectsLocationsOperationsListRequest(_messages.Message):
  r"""A StorageinsightsProjectsLocationsOperationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The name of the operation's parent resource.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class StorageinsightsProjectsLocationsReportConfigsCreateRequest(_messages.Message):
  r"""A StorageinsightsProjectsLocationsReportConfigsCreateRequest object.

  Fields:
    parent: Required. Value for parent.
    reportConfig: A ReportConfig resource to be passed as the request body.
    requestId: Optional. An optional request ID to identify requests. Specify
      a unique request ID so that if you must retry your request, the server
      will know to ignore the request if it has already been completed. The
      server will guarantee that for at least 60 minutes since the first
      request. For example, consider a situation where you make an initial
      request and the request times out. If you make the request again with
      the same request ID, the server can check if original operation with the
      same request ID was received, and if so, will ignore the second request.
      This prevents clients from accidentally creating duplicate commitments.
      The request ID must be a valid UUID with the exception that zero UUID is
      not supported (00000000-0000-0000-0000-000000000000).
  """

  parent = _messages.StringField(1, required=True)
  reportConfig = _messages.MessageField('ReportConfig', 2)
  requestId = _messages.StringField(3)


class StorageinsightsProjectsLocationsReportConfigsDeleteRequest(_messages.Message):
  r"""A StorageinsightsProjectsLocationsReportConfigsDeleteRequest object.

  Fields:
    force: Optional. If set, all ReportDetails for this ReportConfig will be
      deleted.
    name: Required. Name of the resource
    requestId: Optional. An optional request ID to identify requests. Specify
      a unique request ID so that if you must retry your request, the server
      will know to ignore the request if it has already been completed. The
      server will guarantee that for at least 60 minutes after the first
      request. For example, consider a situation where you make an initial
      request and the request times out. If you make the request again with
      the same request ID, the server can check if original operation with the
      same request ID was received, and if so, will ignore the second request.
      This prevents clients from accidentally creating duplicate commitments.
      The request ID must be a valid UUID with the exception that zero UUID is
      not supported (00000000-0000-0000-0000-000000000000).
  """

  force = _messages.BooleanField(1)
  name = _messages.StringField(2, required=True)
  requestId = _messages.StringField(3)


class StorageinsightsProjectsLocationsReportConfigsGetRequest(_messages.Message):
  r"""A StorageinsightsProjectsLocationsReportConfigsGetRequest object.

  Fields:
    name: Required. Name of the resource
  """

  name = _messages.StringField(1, required=True)


class StorageinsightsProjectsLocationsReportConfigsListRequest(_messages.Message):
  r"""A StorageinsightsProjectsLocationsReportConfigsListRequest object.

  Fields:
    filter: Filtering results
    orderBy: Hint for how to order the results
    pageSize: Requested page size. Server may return fewer items than
      requested. If unspecified, server will pick an appropriate default.
    pageToken: A token identifying a page of results the server should return.
    parent: Required. Parent value for ListReportConfigsRequest
  """

  filter = _messages.StringField(1)
  orderBy = _messages.StringField(2)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)
  parent = _messages.StringField(5, required=True)


class StorageinsightsProjectsLocationsReportConfigsPatchRequest(_messages.Message):
  r"""A StorageinsightsProjectsLocationsReportConfigsPatchRequest object.

  Fields:
    name: name of resource. It will be of form
      projects//locations//reportConfigs/.
    reportConfig: A ReportConfig resource to be passed as the request body.
    requestId: Optional. An optional request ID to identify requests. Specify
      a unique request ID so that if you must retry your request, the server
      will know to ignore the request if it has already been completed. The
      server will guarantee that for at least 60 minutes since the first
      request. For example, consider a situation where you make an initial
      request and the request times out. If you make the request again with
      the same request ID, the server can check if original operation with the
      same request ID was received, and if so, will ignore the second request.
      This prevents clients from accidentally creating duplicate commitments.
      The request ID must be a valid UUID with the exception that zero UUID is
      not supported (00000000-0000-0000-0000-000000000000).
    updateMask: Required. Field mask is used to specify the fields to be
      overwritten in the ReportConfig resource by the update. The fields
      specified in the update_mask are relative to the resource, not the full
      request. A field will be overwritten if it is in the mask. If the user
      does not provide a mask then all fields will be overwritten.
  """

  name = _messages.StringField(1, required=True)
  reportConfig = _messages.MessageField('ReportConfig', 2)
  requestId = _messages.StringField(3)
  updateMask = _messages.StringField(4)


class StorageinsightsProjectsLocationsReportConfigsReportDetailsGetRequest(_messages.Message):
  r"""A StorageinsightsProjectsLocationsReportConfigsReportDetailsGetRequest
  object.

  Fields:
    name: Required. Name of the resource
  """

  name = _messages.StringField(1, required=True)


class StorageinsightsProjectsLocationsReportConfigsReportDetailsListRequest(_messages.Message):
  r"""A StorageinsightsProjectsLocationsReportConfigsReportDetailsListRequest
  object.

  Fields:
    filter: Filtering results
    orderBy: Hint for how to order the results
    pageSize: Requested page size. Server may return fewer items than
      requested. If unspecified, server will pick an appropriate default.
    pageToken: A token identifying a page of results the server should return.
    parent: Required. Parent value for ListReportDetailsRequest
  """

  filter = _messages.StringField(1)
  orderBy = _messages.StringField(2)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)
  parent = _messages.StringField(5, required=True)


class TimeZone(_messages.Message):
  r"""Represents a time zone from the [IANA Time Zone
  Database](https://www.iana.org/time-zones).

  Fields:
    id: IANA Time Zone Database time zone, e.g. "America/New_York".
    version: Optional. IANA Time Zone Database version number, e.g. "2019a".
  """

  id = _messages.StringField(1)
  version = _messages.StringField(2)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
