# coding: utf-8

"""
    Marquez

    Marquez is an open source **metadata service** for the **collection**, **aggregation**, and **visualization** of a data ecosystem's metadata.  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import marquez_codegen_client
from marquez_codegen_client.api.jobs_api import JobsApi  # noqa: E501
from marquez_codegen_client.rest import ApiException


class TestJobsApi(unittest.TestCase):
    """JobsApi unit test stubs"""

    def setUp(self):
        self.api = marquez_codegen_client.api.jobs_api.JobsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_jobs_runs_id_abort_put(self):
        """Test case for jobs_runs_id_abort_put

        Abort a job run  # noqa: E501
        """
        pass

    def test_jobs_runs_id_complete_put(self):
        """Test case for jobs_runs_id_complete_put

        Complete a job run  # noqa: E501
        """
        pass

    def test_jobs_runs_id_fail_put(self):
        """Test case for jobs_runs_id_fail_put

        Fail a job run  # noqa: E501
        """
        pass

    def test_jobs_runs_id_get(self):
        """Test case for jobs_runs_id_get

        Retrieve a job run  # noqa: E501
        """
        pass

    def test_jobs_runs_id_outputs_get(self):
        """Test case for jobs_runs_id_outputs_get

        List all job run outputs  # noqa: E501
        """
        pass

    def test_jobs_runs_id_outputs_put(self):
        """Test case for jobs_runs_id_outputs_put

        Create multiple output datasets  # noqa: E501
        """
        pass

    def test_jobs_runs_id_run_put(self):
        """Test case for jobs_runs_id_run_put

        Start a job run  # noqa: E501
        """
        pass

    def test_namespaces_namespace_jobs_get(self):
        """Test case for namespaces_namespace_jobs_get

        List all jobs  # noqa: E501
        """
        pass

    def test_namespaces_namespace_jobs_job_get(self):
        """Test case for namespaces_namespace_jobs_job_get

        Retrieve a job  # noqa: E501
        """
        pass

    def test_namespaces_namespace_jobs_job_put(self):
        """Test case for namespaces_namespace_jobs_job_put

        Create a job  # noqa: E501
        """
        pass

    def test_namespaces_namespace_jobs_job_runs_get(self):
        """Test case for namespaces_namespace_jobs_job_runs_get

        List all job runs  # noqa: E501
        """
        pass

    def test_namespaces_namespace_jobs_job_runs_post(self):
        """Test case for namespaces_namespace_jobs_job_runs_post

        Create a job run  # noqa: E501
        """
        pass

    def test_namespaces_namespace_jobs_job_versions_get(self):
        """Test case for namespaces_namespace_jobs_job_versions_get

        List all job versions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
