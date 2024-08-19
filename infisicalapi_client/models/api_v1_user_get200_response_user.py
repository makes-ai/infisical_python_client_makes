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
from typing import Any, List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist

class ApiV1UserGet200ResponseUser(BaseModel):
    """
    ApiV1UserGet200ResponseUser
    """
    id: StrictStr = Field(...)
    email: Optional[StrictStr] = None
    auth_methods: Optional[conlist(StrictStr)] = Field(default=None, alias="authMethods")
    super_admin: Optional[StrictBool] = Field(default=False, alias="superAdmin")
    first_name: Optional[StrictStr] = Field(default=None, alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, alias="lastName")
    is_accepted: Optional[StrictBool] = Field(default=False, alias="isAccepted")
    is_mfa_enabled: Optional[StrictBool] = Field(default=False, alias="isMfaEnabled")
    mfa_methods: Optional[conlist(StrictStr)] = Field(default=None, alias="mfaMethods")
    devices: Optional[Any] = None
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    is_ghost: Optional[StrictBool] = Field(default=False, alias="isGhost")
    username: StrictStr = Field(...)
    is_email_verified: Optional[StrictBool] = Field(default=False, alias="isEmailVerified")
    consecutive_failed_mfa_attempts: Optional[Union[StrictFloat, StrictInt]] = Field(default=0, alias="consecutiveFailedMfaAttempts")
    is_locked: Optional[StrictBool] = Field(default=False, alias="isLocked")
    temporary_lock_date_end: Optional[datetime] = Field(default=None, alias="temporaryLockDateEnd")
    consecutive_failed_password_attempts: Optional[Union[StrictFloat, StrictInt]] = Field(default=0, alias="consecutiveFailedPasswordAttempts")
    client_public_key: Optional[StrictStr] = Field(default=None, alias="clientPublicKey")
    server_private_key: Optional[StrictStr] = Field(default=None, alias="serverPrivateKey")
    encryption_version: Optional[Union[StrictFloat, StrictInt]] = Field(default=2, alias="encryptionVersion")
    protected_key: Optional[StrictStr] = Field(default=None, alias="protectedKey")
    protected_key_iv: Optional[StrictStr] = Field(default=None, alias="protectedKeyIV")
    protected_key_tag: Optional[StrictStr] = Field(default=None, alias="protectedKeyTag")
    public_key: StrictStr = Field(default=..., alias="publicKey")
    encrypted_private_key: StrictStr = Field(default=..., alias="encryptedPrivateKey")
    iv: StrictStr = Field(...)
    tag: StrictStr = Field(...)
    salt: StrictStr = Field(...)
    verifier: StrictStr = Field(...)
    user_id: StrictStr = Field(default=..., alias="userId")
    __properties = ["id", "email", "authMethods", "superAdmin", "firstName", "lastName", "isAccepted", "isMfaEnabled", "mfaMethods", "devices", "createdAt", "updatedAt", "isGhost", "username", "isEmailVerified", "consecutiveFailedMfaAttempts", "isLocked", "temporaryLockDateEnd", "consecutiveFailedPasswordAttempts", "clientPublicKey", "serverPrivateKey", "encryptionVersion", "protectedKey", "protectedKeyIV", "protectedKeyTag", "publicKey", "encryptedPrivateKey", "iv", "tag", "salt", "verifier", "userId"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1UserGet200ResponseUser:
        """Create an instance of ApiV1UserGet200ResponseUser from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if email (nullable) is None
        # and __fields_set__ contains the field
        if self.email is None and "email" in self.__fields_set__:
            _dict['email'] = None

        # set to None if auth_methods (nullable) is None
        # and __fields_set__ contains the field
        if self.auth_methods is None and "auth_methods" in self.__fields_set__:
            _dict['authMethods'] = None

        # set to None if super_admin (nullable) is None
        # and __fields_set__ contains the field
        if self.super_admin is None and "super_admin" in self.__fields_set__:
            _dict['superAdmin'] = None

        # set to None if first_name (nullable) is None
        # and __fields_set__ contains the field
        if self.first_name is None and "first_name" in self.__fields_set__:
            _dict['firstName'] = None

        # set to None if last_name (nullable) is None
        # and __fields_set__ contains the field
        if self.last_name is None and "last_name" in self.__fields_set__:
            _dict['lastName'] = None

        # set to None if is_accepted (nullable) is None
        # and __fields_set__ contains the field
        if self.is_accepted is None and "is_accepted" in self.__fields_set__:
            _dict['isAccepted'] = None

        # set to None if is_mfa_enabled (nullable) is None
        # and __fields_set__ contains the field
        if self.is_mfa_enabled is None and "is_mfa_enabled" in self.__fields_set__:
            _dict['isMfaEnabled'] = None

        # set to None if mfa_methods (nullable) is None
        # and __fields_set__ contains the field
        if self.mfa_methods is None and "mfa_methods" in self.__fields_set__:
            _dict['mfaMethods'] = None

        # set to None if devices (nullable) is None
        # and __fields_set__ contains the field
        if self.devices is None and "devices" in self.__fields_set__:
            _dict['devices'] = None

        # set to None if is_email_verified (nullable) is None
        # and __fields_set__ contains the field
        if self.is_email_verified is None and "is_email_verified" in self.__fields_set__:
            _dict['isEmailVerified'] = None

        # set to None if consecutive_failed_mfa_attempts (nullable) is None
        # and __fields_set__ contains the field
        if self.consecutive_failed_mfa_attempts is None and "consecutive_failed_mfa_attempts" in self.__fields_set__:
            _dict['consecutiveFailedMfaAttempts'] = None

        # set to None if is_locked (nullable) is None
        # and __fields_set__ contains the field
        if self.is_locked is None and "is_locked" in self.__fields_set__:
            _dict['isLocked'] = None

        # set to None if temporary_lock_date_end (nullable) is None
        # and __fields_set__ contains the field
        if self.temporary_lock_date_end is None and "temporary_lock_date_end" in self.__fields_set__:
            _dict['temporaryLockDateEnd'] = None

        # set to None if consecutive_failed_password_attempts (nullable) is None
        # and __fields_set__ contains the field
        if self.consecutive_failed_password_attempts is None and "consecutive_failed_password_attempts" in self.__fields_set__:
            _dict['consecutiveFailedPasswordAttempts'] = None

        # set to None if client_public_key (nullable) is None
        # and __fields_set__ contains the field
        if self.client_public_key is None and "client_public_key" in self.__fields_set__:
            _dict['clientPublicKey'] = None

        # set to None if server_private_key (nullable) is None
        # and __fields_set__ contains the field
        if self.server_private_key is None and "server_private_key" in self.__fields_set__:
            _dict['serverPrivateKey'] = None

        # set to None if encryption_version (nullable) is None
        # and __fields_set__ contains the field
        if self.encryption_version is None and "encryption_version" in self.__fields_set__:
            _dict['encryptionVersion'] = None

        # set to None if protected_key (nullable) is None
        # and __fields_set__ contains the field
        if self.protected_key is None and "protected_key" in self.__fields_set__:
            _dict['protectedKey'] = None

        # set to None if protected_key_iv (nullable) is None
        # and __fields_set__ contains the field
        if self.protected_key_iv is None and "protected_key_iv" in self.__fields_set__:
            _dict['protectedKeyIV'] = None

        # set to None if protected_key_tag (nullable) is None
        # and __fields_set__ contains the field
        if self.protected_key_tag is None and "protected_key_tag" in self.__fields_set__:
            _dict['protectedKeyTag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1UserGet200ResponseUser:
        """Create an instance of ApiV1UserGet200ResponseUser from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1UserGet200ResponseUser.parse_obj(obj)

        _obj = ApiV1UserGet200ResponseUser.parse_obj({
            "id": obj.get("id"),
            "email": obj.get("email"),
            "auth_methods": obj.get("authMethods"),
            "super_admin": obj.get("superAdmin") if obj.get("superAdmin") is not None else False,
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "is_accepted": obj.get("isAccepted") if obj.get("isAccepted") is not None else False,
            "is_mfa_enabled": obj.get("isMfaEnabled") if obj.get("isMfaEnabled") is not None else False,
            "mfa_methods": obj.get("mfaMethods"),
            "devices": obj.get("devices"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "is_ghost": obj.get("isGhost") if obj.get("isGhost") is not None else False,
            "username": obj.get("username"),
            "is_email_verified": obj.get("isEmailVerified") if obj.get("isEmailVerified") is not None else False,
            "consecutive_failed_mfa_attempts": obj.get("consecutiveFailedMfaAttempts") if obj.get("consecutiveFailedMfaAttempts") is not None else 0,
            "is_locked": obj.get("isLocked") if obj.get("isLocked") is not None else False,
            "temporary_lock_date_end": obj.get("temporaryLockDateEnd"),
            "consecutive_failed_password_attempts": obj.get("consecutiveFailedPasswordAttempts") if obj.get("consecutiveFailedPasswordAttempts") is not None else 0,
            "client_public_key": obj.get("clientPublicKey"),
            "server_private_key": obj.get("serverPrivateKey"),
            "encryption_version": obj.get("encryptionVersion") if obj.get("encryptionVersion") is not None else 2,
            "protected_key": obj.get("protectedKey"),
            "protected_key_iv": obj.get("protectedKeyIV"),
            "protected_key_tag": obj.get("protectedKeyTag"),
            "public_key": obj.get("publicKey"),
            "encrypted_private_key": obj.get("encryptedPrivateKey"),
            "iv": obj.get("iv"),
            "tag": obj.get("tag"),
            "salt": obj.get("salt"),
            "verifier": obj.get("verifier"),
            "user_id": obj.get("userId")
        })
        return _obj

