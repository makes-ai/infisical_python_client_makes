# coding: utf-8

"""
    Infisical API

    List of all available APIs that can be consumed

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, Optional
from pydantic import ConfigDict, BaseModel, Field, StrictBool, StrictStr

class ApiV1IntegrationPost200ResponseIntegration(BaseModel):
    """
    ApiV1IntegrationPost200ResponseIntegration
    """
    id: StrictStr = Field(...)
    is_active: StrictBool = Field(default=..., alias="isActive")
    url: Optional[StrictStr] = None
    app: Optional[StrictStr] = None
    app_id: Optional[StrictStr] = Field(default=None, alias="appId")
    target_environment: Optional[StrictStr] = Field(default=None, alias="targetEnvironment")
    target_environment_id: Optional[StrictStr] = Field(default=None, alias="targetEnvironmentId")
    target_service: Optional[StrictStr] = Field(default=None, alias="targetService")
    target_service_id: Optional[StrictStr] = Field(default=None, alias="targetServiceId")
    owner: Optional[StrictStr] = None
    path: Optional[StrictStr] = None
    region: Optional[StrictStr] = None
    scope: Optional[StrictStr] = None
    integration: StrictStr = Field(...)
    metadata: Optional[Any] = None
    integration_auth_id: StrictStr = Field(default=..., alias="integrationAuthId")
    env_id: StrictStr = Field(default=..., alias="envId")
    secret_path: Optional[StrictStr] = Field(default='/', alias="secretPath")
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    last_used: Optional[datetime] = Field(default=None, alias="lastUsed")
    is_synced: Optional[StrictBool] = Field(default=None, alias="isSynced")
    sync_message: Optional[StrictStr] = Field(default=None, alias="syncMessage")
    last_sync_job_id: Optional[StrictStr] = Field(default=None, alias="lastSyncJobId")
    __properties = ["id", "isActive", "url", "app", "appId", "targetEnvironment", "targetEnvironmentId", "targetService", "targetServiceId", "owner", "path", "region", "scope", "integration", "metadata", "integrationAuthId", "envId", "secretPath", "createdAt", "updatedAt", "lastUsed", "isSynced", "syncMessage", "lastSyncJobId"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1IntegrationPost200ResponseIntegration:
        """Create an instance of ApiV1IntegrationPost200ResponseIntegration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if url (nullable) is None
        # and __fields_set__ contains the field
        if self.url is None and "url" in self.__fields_set__:
            _dict['url'] = None

        # set to None if app (nullable) is None
        # and __fields_set__ contains the field
        if self.app is None and "app" in self.__fields_set__:
            _dict['app'] = None

        # set to None if app_id (nullable) is None
        # and __fields_set__ contains the field
        if self.app_id is None and "app_id" in self.__fields_set__:
            _dict['appId'] = None

        # set to None if target_environment (nullable) is None
        # and __fields_set__ contains the field
        if self.target_environment is None and "target_environment" in self.__fields_set__:
            _dict['targetEnvironment'] = None

        # set to None if target_environment_id (nullable) is None
        # and __fields_set__ contains the field
        if self.target_environment_id is None and "target_environment_id" in self.__fields_set__:
            _dict['targetEnvironmentId'] = None

        # set to None if target_service (nullable) is None
        # and __fields_set__ contains the field
        if self.target_service is None and "target_service" in self.__fields_set__:
            _dict['targetService'] = None

        # set to None if target_service_id (nullable) is None
        # and __fields_set__ contains the field
        if self.target_service_id is None and "target_service_id" in self.__fields_set__:
            _dict['targetServiceId'] = None

        # set to None if owner (nullable) is None
        # and __fields_set__ contains the field
        if self.owner is None and "owner" in self.__fields_set__:
            _dict['owner'] = None

        # set to None if path (nullable) is None
        # and __fields_set__ contains the field
        if self.path is None and "path" in self.__fields_set__:
            _dict['path'] = None

        # set to None if region (nullable) is None
        # and __fields_set__ contains the field
        if self.region is None and "region" in self.__fields_set__:
            _dict['region'] = None

        # set to None if scope (nullable) is None
        # and __fields_set__ contains the field
        if self.scope is None and "scope" in self.__fields_set__:
            _dict['scope'] = None

        # set to None if metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.metadata is None and "metadata" in self.__fields_set__:
            _dict['metadata'] = None

        # set to None if last_used (nullable) is None
        # and __fields_set__ contains the field
        if self.last_used is None and "last_used" in self.__fields_set__:
            _dict['lastUsed'] = None

        # set to None if is_synced (nullable) is None
        # and __fields_set__ contains the field
        if self.is_synced is None and "is_synced" in self.__fields_set__:
            _dict['isSynced'] = None

        # set to None if sync_message (nullable) is None
        # and __fields_set__ contains the field
        if self.sync_message is None and "sync_message" in self.__fields_set__:
            _dict['syncMessage'] = None

        # set to None if last_sync_job_id (nullable) is None
        # and __fields_set__ contains the field
        if self.last_sync_job_id is None and "last_sync_job_id" in self.__fields_set__:
            _dict['lastSyncJobId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1IntegrationPost200ResponseIntegration:
        """Create an instance of ApiV1IntegrationPost200ResponseIntegration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1IntegrationPost200ResponseIntegration.parse_obj(obj)

        _obj = ApiV1IntegrationPost200ResponseIntegration.parse_obj({
            "id": obj.get("id"),
            "is_active": obj.get("isActive"),
            "url": obj.get("url"),
            "app": obj.get("app"),
            "app_id": obj.get("appId"),
            "target_environment": obj.get("targetEnvironment"),
            "target_environment_id": obj.get("targetEnvironmentId"),
            "target_service": obj.get("targetService"),
            "target_service_id": obj.get("targetServiceId"),
            "owner": obj.get("owner"),
            "path": obj.get("path"),
            "region": obj.get("region"),
            "scope": obj.get("scope"),
            "integration": obj.get("integration"),
            "metadata": obj.get("metadata"),
            "integration_auth_id": obj.get("integrationAuthId"),
            "env_id": obj.get("envId"),
            "secret_path": obj.get("secretPath") if obj.get("secretPath") is not None else '/',
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "last_used": obj.get("lastUsed"),
            "is_synced": obj.get("isSynced"),
            "sync_message": obj.get("syncMessage"),
            "last_sync_job_id": obj.get("lastSyncJobId")
        })
        return _obj


