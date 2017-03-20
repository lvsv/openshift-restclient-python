# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import copy

import pytest

from openshift.helper.exceptions import OpenShiftException


@pytest.fixture()
def create_params(create_tasks, project, object_name):
    parameters = create_tasks['create']
    parameters['namespace'] = project
    parameters['name'] = object_name
    return parameters


@pytest.fixture()
def patch_params(patch_tasks, project, object_name):
    parameters = patch_tasks['patch']
    parameters['namespace'] = project
    parameters['name'] = object_name
    return parameters


@pytest.fixture()
def replace_params(replace_tasks, project, object_name):
    parameters = replace_tasks['replace']
    parameters['namespace'] = project
    parameters['name'] = object_name
    return parameters


@pytest.fixture()
def service(ansible_helper, create_params):
    new_obj = ansible_helper.object_from_params(create_params)
    namespace = create_params.get('namespace')
    name = create_params.get('name')
    k8s_obj = ansible_helper.create_object(namespace, new_obj)

    yield k8s_obj

    try:
        ansible_helper.delete_object(name, namespace)
    except OpenShiftException as ex:
        # Swallow exception if object is already removed
        if ex.value.get('status') != 404:
            raise


def test_create_service(ansible_helper, create_params, service, obj_compare):
    obj_compare(ansible_helper, service, create_params)


def test_get_service(ansible_helper, service):
    name = service.metadata.name
    namespace = service.metadata.namespace
    k8s_obj = ansible_helper.get_object(name, namespace)
    assert k8s_obj is not None


def test_patch_service(ansible_helper, service, patch_params, obj_compare):
    name = patch_params.get('name')
    namespace = patch_params.get('namespace')
    existing_obj = service
    updated_obj = copy.deepcopy(existing_obj)
    ansible_helper.object_from_params(patch_params, obj=updated_obj)
    match = ansible_helper.objects_match(existing_obj, updated_obj)
    assert not match
    new_obj = ansible_helper.patch_object(name, namespace, updated_obj)
    assert new_obj is not None
    obj_compare(ansible_helper, new_obj, patch_params)


def test_replace_service(ansible_helper, service, replace_params, obj_compare):
    name = replace_params.get('name')
    namespace = replace_params.get('namespace')
    existing_obj = service
    ansible_helper.object_from_params(replace_params, obj=existing_obj)
    k8s_obj = ansible_helper.replace_object(name, namespace, existing_obj)
    obj_compare(ansible_helper, k8s_obj, replace_params)


def test_remove_service(ansible_helper, service):
    name = service.metadata.name
    namespace = service.metadata.namespace
    ansible_helper.delete_object(name, namespace)
    k8s_obj = ansible_helper.get_object(name, namespace)
    assert k8s_obj is None