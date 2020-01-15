from google.oauth2.service_account import Credentials
from googleapiclient import discovery
import pymysql
from . import config_parser


def common_api_process(*gcp_credential_file_path):
    _insert_process()
    _auth(gcp_credential_file_path)


def _auth(gcp_credential_file_path):
    _gcp_auth(gcp_credential_file_path)


def _gcp_auth(gcp_credential_file_path):

    credentials = Credentials.from_service_account_file(gcp_credential_file_path)
    compute = discovery.build('compute', 'v1', credentials=credentials)
    project_id = 'mhcml-test'
    zone = 'us-central1-a'

    print(compute.instances().list(project=project_id, zone=zone).execute())


def _create_virtual_machine(instance_type):
    if instance_type == 'gcp':
        _create_gce()
    elif instance_type == 'ec2':
        _create_ec2()


def _create_gce():
    pass


def _create_ec2():
    pass


if __name__ == '__main__':
    common_api_process(input('gcp_credential_file_path: '))
