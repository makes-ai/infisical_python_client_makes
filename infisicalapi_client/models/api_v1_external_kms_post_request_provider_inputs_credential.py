# coding: utf-8

"""
    Infisical API

    List of all available APIs that can be consumed

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from infisicalapi_client.models.api_v1_external_kms_post_request_provider_inputs_credential_any_of import ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf
from infisicalapi_client.models.api_v1_external_kms_post_request_provider_inputs_credential_any_of1 import ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf1
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

APIV1EXTERNALKMSPOSTREQUESTPROVIDERINPUTSCREDENTIAL_ANY_OF_SCHEMAS = ["ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf", "ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf1"]

class ApiV1ExternalKmsPostRequestProviderInputsCredential(BaseModel):
    """
    AWS credential information to connect
    """

    # data type: ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf
    anyof_schema_1_validator: Optional[ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf] = None
    # data type: ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf1
    anyof_schema_2_validator: Optional[ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf1] = None
    if TYPE_CHECKING:
        actual_instance: Union[ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf, ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf1]
    else:
        actual_instance: Any
    any_of_schemas: List[str] = Field(APIV1EXTERNALKMSPOSTREQUESTPROVIDERINPUTSCREDENTIAL_ANY_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = ApiV1ExternalKmsPostRequestProviderInputsCredential.construct()
        error_messages = []
        # validate data type: ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf
        if not isinstance(v, ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf`")
        else:
            return v

        # validate data type: ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf1
        if not isinstance(v, ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf1`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in ApiV1ExternalKmsPostRequestProviderInputsCredential with anyOf schemas: ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf, ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf1. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1ExternalKmsPostRequestProviderInputsCredential:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1ExternalKmsPostRequestProviderInputsCredential:
        """Returns the object represented by the json string"""
        instance = ApiV1ExternalKmsPostRequestProviderInputsCredential.construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf] = None
        try:
            instance.actual_instance = ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf1] = None
        try:
            instance.actual_instance = ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf1.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ApiV1ExternalKmsPostRequestProviderInputsCredential with anyOf schemas: ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf, ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf1. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_dict()
        else:
            return json.dumps(self.actual_instance)

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())

