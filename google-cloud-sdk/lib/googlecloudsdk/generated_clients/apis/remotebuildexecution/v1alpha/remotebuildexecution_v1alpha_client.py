"""Generated client library for remotebuildexecution version v1alpha."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.remotebuildexecution.v1alpha import remotebuildexecution_v1alpha_messages as messages


class RemotebuildexecutionV1alpha(base_api.BaseApiClient):
  """Generated client library for service remotebuildexecution version v1alpha."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://admin-remotebuildexecution.googleapis.com/'
  MTLS_BASE_URL = 'https://admin-remotebuildexecution.mtls.googleapis.com/'

  _PACKAGE = 'remotebuildexecution'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1alpha'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'RemotebuildexecutionV1alpha'
  _URL_VERSION = 'v1alpha'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new remotebuildexecution handle."""
    url = url or self.BASE_URL
    super(RemotebuildexecutionV1alpha, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_instances_workerpools = self.ProjectsInstancesWorkerpoolsService(self)
    self.projects_instances = self.ProjectsInstancesService(self)
    self.projects_operations = self.ProjectsOperationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsInstancesWorkerpoolsService(base_api.BaseApiService):
    """Service class for the projects_instances_workerpools resource."""

    _NAME = 'projects_instances_workerpools'

    def __init__(self, client):
      super(RemotebuildexecutionV1alpha.ProjectsInstancesWorkerpoolsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new worker pool with a specified size and configuration. Returns a long running operation which contains a worker pool on completion. While the long running operation is in progress, any call to `GetWorkerPool` returns a worker pool in state `CREATING`.

      Args:
        request: (GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateWorkerPoolRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/instances/{instancesId}/workerpools',
        http_method='POST',
        method_id='remotebuildexecution.projects.instances.workerpools.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1alpha/{+parent}/workerpools',
        request_field='<request>',
        request_type_name='GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateWorkerPoolRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes the specified worker pool. Returns a long running operation, which contains a `google.protobuf.Empty` response on completion. While the long running operation is in progress, any call to `GetWorkerPool` returns a worker pool in state `DELETING`.

      Args:
        request: (RemotebuildexecutionProjectsInstancesWorkerpoolsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/instances/{instancesId}/workerpools/{workerpoolsId}',
        http_method='DELETE',
        method_id='remotebuildexecution.projects.instances.workerpools.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='RemotebuildexecutionProjectsInstancesWorkerpoolsDeleteRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Returns the specified worker pool.

      Args:
        request: (RemotebuildexecutionProjectsInstancesWorkerpoolsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPool) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/instances/{instancesId}/workerpools/{workerpoolsId}',
        http_method='GET',
        method_id='remotebuildexecution.projects.instances.workerpools.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='RemotebuildexecutionProjectsInstancesWorkerpoolsGetRequest',
        response_type_name='GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPool',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists worker pools in an instance.

      Args:
        request: (RemotebuildexecutionProjectsInstancesWorkerpoolsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleDevtoolsRemotebuildexecutionAdminV1alphaListWorkerPoolsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/instances/{instancesId}/workerpools',
        http_method='GET',
        method_id='remotebuildexecution.projects.instances.workerpools.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter'],
        relative_path='v1alpha/{+parent}/workerpools',
        request_field='',
        request_type_name='RemotebuildexecutionProjectsInstancesWorkerpoolsListRequest',
        response_type_name='GoogleDevtoolsRemotebuildexecutionAdminV1alphaListWorkerPoolsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates an existing worker pool with a specified size and/or configuration. Returns a long running operation, which contains a worker pool on completion. While the long running operation is in progress, any call to `GetWorkerPool` returns a worker pool in state `UPDATING`.

      Args:
        request: (RemotebuildexecutionProjectsInstancesWorkerpoolsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/instances/{instancesId}/workerpools/{workerpoolsId}',
        http_method='PATCH',
        method_id='remotebuildexecution.projects.instances.workerpools.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='googleDevtoolsRemotebuildexecutionAdminV1alphaUpdateWorkerPoolRequest',
        request_type_name='RemotebuildexecutionProjectsInstancesWorkerpoolsPatchRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

  class ProjectsInstancesService(base_api.BaseApiService):
    """Service class for the projects_instances resource."""

    _NAME = 'projects_instances'

    def __init__(self, client):
      super(RemotebuildexecutionV1alpha.ProjectsInstancesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new instance in the specified region. Returns a long running operation which contains an instance on completion. While the long running operation is in progress, any call to `GetInstance` returns an instance in state `CREATING`.

      Args:
        request: (GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateInstanceRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/instances',
        http_method='POST',
        method_id='remotebuildexecution.projects.instances.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1alpha/{+parent}/instances',
        request_field='<request>',
        request_type_name='GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateInstanceRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes the specified instance. Returns a long running operation which contains a `google.protobuf.Empty` response on completion. Deleting an instance with worker pools in it will delete these worker pools.

      Args:
        request: (RemotebuildexecutionProjectsInstancesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/instances/{instancesId}',
        http_method='DELETE',
        method_id='remotebuildexecution.projects.instances.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='RemotebuildexecutionProjectsInstancesDeleteRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Returns the specified instance.

      Args:
        request: (RemotebuildexecutionProjectsInstancesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/instances/{instancesId}',
        http_method='GET',
        method_id='remotebuildexecution.projects.instances.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='RemotebuildexecutionProjectsInstancesGetRequest',
        response_type_name='GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists instances in a project.

      Args:
        request: (RemotebuildexecutionProjectsInstancesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleDevtoolsRemotebuildexecutionAdminV1alphaListInstancesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/instances',
        http_method='GET',
        method_id='remotebuildexecution.projects.instances.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1alpha/{+parent}/instances',
        request_field='',
        request_type_name='RemotebuildexecutionProjectsInstancesListRequest',
        response_type_name='GoogleDevtoolsRemotebuildexecutionAdminV1alphaListInstancesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the specified instance. Returns a long running operation which contains the updated instance in the response on completion.

      Args:
        request: (RemotebuildexecutionProjectsInstancesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/instances/{instancesId}',
        http_method='PATCH',
        method_id='remotebuildexecution.projects.instances.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['loggingEnabled', 'name1', 'updateMask'],
        relative_path='v1alpha/{+name}',
        request_field='googleDevtoolsRemotebuildexecutionAdminV1alphaInstance',
        request_type_name='RemotebuildexecutionProjectsInstancesPatchRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def TestNotify(self, request, global_params=None):
      r"""Sends a test notification to the specified instance. Returns a `google.protobuf.Empty` on success.

      Args:
        request: (RemotebuildexecutionProjectsInstancesTestNotifyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleProtobufEmpty) The response message.
      """
      config = self.GetMethodConfig('TestNotify')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestNotify.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/instances/{instancesId}:testNotify',
        http_method='POST',
        method_id='remotebuildexecution.projects.instances.testNotify',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}:testNotify',
        request_field='googleDevtoolsRemotebuildexecutionAdminV1alphaTestNotifyInstanceRequest',
        request_type_name='RemotebuildexecutionProjectsInstancesTestNotifyRequest',
        response_type_name='GoogleProtobufEmpty',
        supports_download=False,
    )

  class ProjectsOperationsService(base_api.BaseApiService):
    """Service class for the projects_operations resource."""

    _NAME = 'projects_operations'

    def __init__(self, client):
      super(RemotebuildexecutionV1alpha.ProjectsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (RemotebuildexecutionProjectsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/operations/{operationsId}',
        http_method='GET',
        method_id='remotebuildexecution.projects.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='RemotebuildexecutionProjectsOperationsGetRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(RemotebuildexecutionV1alpha.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
