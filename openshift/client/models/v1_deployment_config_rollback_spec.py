# coding: utf-8

"""
    OpenShift API (with Kubernetes)

    OpenShift provides builds, application lifecycle, image content management, and administrative policy on top of Kubernetes. The API allows consistent management of those objects.  All API operations are authenticated via an Authorization bearer token that is provided for service accounts as a generated secret (in JWT form) or via the native OAuth endpoint located at /oauth/authorize. Core infrastructure components may use client certificates that require no authentication.  All API operations return a 'resourceVersion' string that represents the version of the object in the underlying storage. The standard LIST operation performs a snapshot read of the underlying objects, returning a resourceVersion representing a consistent version of the listed objects. The WATCH operation allows all updates to a set of objects after the provided resourceVersion to be observed by a client. By listing and beginning a watch from the returned resourceVersion, clients may observe a consistent view of the state of one or more objects. Note that WATCH always returns the update after the provided resourceVersion. Watch may be extended a limited time in the past - using etcd 2 the watch window is 1000 events (which on a large cluster may only be a few tens of seconds) so clients must explicitly handle the \"watch to old error\" by re-listing.  Objects are divided into two rough categories - those that have a lifecycle and must reflect the state of the cluster, and those that have no state. Objects with lifecycle typically have three main sections:  * 'metadata' common to all objects * a 'spec' that represents the desired state * a 'status' that represents how much of the desired state is reflected on   the cluster at the current time  Objects that have no state have 'metadata' but may lack a 'spec' or 'status' section.  Objects are divided into those that are namespace scoped (only exist inside of a namespace) and those that are cluster scoped (exist outside of a namespace). A namespace scoped resource will be deleted when the namespace is deleted and cannot be created if the namespace has not yet been created or is in the process of deletion. Cluster scoped resources are typically only accessible to admins - resources like nodes, persistent volumes, and cluster policy.  All objects have a schema that is a combination of the 'kind' and 'apiVersion' fields. This schema is additive only for any given version - no backwards incompatible changes are allowed without incrementing the apiVersion. The server will return and accept a number of standard responses that share a common schema - for instance, the common error type is 'unversioned.Status' (described below) and will be returned on any error from the API server.  The API is available in multiple serialization formats - the default is JSON (Accept: application/json and Content-Type: application/json) but clients may also use YAML (application/yaml) or the native Protobuf schema (application/vnd.kubernetes.protobuf). Note that the format of the WATCH API call is slightly different - for JSON it returns newline delimited objects while for Protobuf it returns length-delimited frames (4 bytes in network-order) that contain a 'versioned.Watch' Protobuf object.  See the OpenShift documentation at https://docs.openshift.org for more information. 

    OpenAPI spec version: v3.6.0-alpha.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1DeploymentConfigRollbackSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, _from=None, include_replication_meta=None, include_strategy=None, include_template=None, include_triggers=None, revision=None):
        """
        V1DeploymentConfigRollbackSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            '_from': 'V1ObjectReference',
            'include_replication_meta': 'bool',
            'include_strategy': 'bool',
            'include_template': 'bool',
            'include_triggers': 'bool',
            'revision': 'int'
        }

        self.attribute_map = {
            '_from': 'from',
            'include_replication_meta': 'includeReplicationMeta',
            'include_strategy': 'includeStrategy',
            'include_template': 'includeTemplate',
            'include_triggers': 'includeTriggers',
            'revision': 'revision'
        }

        self.__from = _from
        self._include_replication_meta = include_replication_meta
        self._include_strategy = include_strategy
        self._include_template = include_template
        self._include_triggers = include_triggers
        self._revision = revision

    @property
    def _from(self):
        """
        Gets the _from of this V1DeploymentConfigRollbackSpec.
        From points to a ReplicationController which is a deployment.

        :return: The _from of this V1DeploymentConfigRollbackSpec.
        :rtype: V1ObjectReference
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this V1DeploymentConfigRollbackSpec.
        From points to a ReplicationController which is a deployment.

        :param _from: The _from of this V1DeploymentConfigRollbackSpec.
        :type: V1ObjectReference
        """
        if _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")

        self.__from = _from

    @property
    def include_replication_meta(self):
        """
        Gets the include_replication_meta of this V1DeploymentConfigRollbackSpec.
        IncludeReplicationMeta specifies whether to include the replica count and selector.

        :return: The include_replication_meta of this V1DeploymentConfigRollbackSpec.
        :rtype: bool
        """
        return self._include_replication_meta

    @include_replication_meta.setter
    def include_replication_meta(self, include_replication_meta):
        """
        Sets the include_replication_meta of this V1DeploymentConfigRollbackSpec.
        IncludeReplicationMeta specifies whether to include the replica count and selector.

        :param include_replication_meta: The include_replication_meta of this V1DeploymentConfigRollbackSpec.
        :type: bool
        """
        if include_replication_meta is None:
            raise ValueError("Invalid value for `include_replication_meta`, must not be `None`")

        self._include_replication_meta = include_replication_meta

    @property
    def include_strategy(self):
        """
        Gets the include_strategy of this V1DeploymentConfigRollbackSpec.
        IncludeStrategy specifies whether to include the deployment Strategy.

        :return: The include_strategy of this V1DeploymentConfigRollbackSpec.
        :rtype: bool
        """
        return self._include_strategy

    @include_strategy.setter
    def include_strategy(self, include_strategy):
        """
        Sets the include_strategy of this V1DeploymentConfigRollbackSpec.
        IncludeStrategy specifies whether to include the deployment Strategy.

        :param include_strategy: The include_strategy of this V1DeploymentConfigRollbackSpec.
        :type: bool
        """
        if include_strategy is None:
            raise ValueError("Invalid value for `include_strategy`, must not be `None`")

        self._include_strategy = include_strategy

    @property
    def include_template(self):
        """
        Gets the include_template of this V1DeploymentConfigRollbackSpec.
        IncludeTemplate specifies whether to include the PodTemplateSpec.

        :return: The include_template of this V1DeploymentConfigRollbackSpec.
        :rtype: bool
        """
        return self._include_template

    @include_template.setter
    def include_template(self, include_template):
        """
        Sets the include_template of this V1DeploymentConfigRollbackSpec.
        IncludeTemplate specifies whether to include the PodTemplateSpec.

        :param include_template: The include_template of this V1DeploymentConfigRollbackSpec.
        :type: bool
        """
        if include_template is None:
            raise ValueError("Invalid value for `include_template`, must not be `None`")

        self._include_template = include_template

    @property
    def include_triggers(self):
        """
        Gets the include_triggers of this V1DeploymentConfigRollbackSpec.
        IncludeTriggers specifies whether to include config Triggers.

        :return: The include_triggers of this V1DeploymentConfigRollbackSpec.
        :rtype: bool
        """
        return self._include_triggers

    @include_triggers.setter
    def include_triggers(self, include_triggers):
        """
        Sets the include_triggers of this V1DeploymentConfigRollbackSpec.
        IncludeTriggers specifies whether to include config Triggers.

        :param include_triggers: The include_triggers of this V1DeploymentConfigRollbackSpec.
        :type: bool
        """
        if include_triggers is None:
            raise ValueError("Invalid value for `include_triggers`, must not be `None`")

        self._include_triggers = include_triggers

    @property
    def revision(self):
        """
        Gets the revision of this V1DeploymentConfigRollbackSpec.
        Revision to rollback to. If set to 0, rollback to the last revision.

        :return: The revision of this V1DeploymentConfigRollbackSpec.
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this V1DeploymentConfigRollbackSpec.
        Revision to rollback to. If set to 0, rollback to the last revision.

        :param revision: The revision of this V1DeploymentConfigRollbackSpec.
        :type: int
        """

        self._revision = revision

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1DeploymentConfigRollbackSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
