import os
import boto3
import requests
import logging

###### Logging Module #######
#############################
level = {
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG
}.get(os.environ.get('LOG_LEVEL', 'DEBUG'))

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - sample_lib[%(process)s]: %(message)s',
    level=level,
    filename="./sample.log"
)
##############################

###### Global #######
#####################
sts = boto3.client('sts')
#####################

##### Modules #####
###################
def authenticate_mfa_session_token(**kwargs):
    try:
        return sts.get_session_token(**kwargs)
    except Exception as e:
        return e

def generate_authorized_session(sessiontoken):
    try:
        return boto3.Session(
            aws_access_key_id=sessiontoken['Credentials']['AccessKeyId'],
            aws_secret_access_key=sessiontoken['Credentials']['SecretAccessKey'],
            aws_session_token=sessiontoken['Credentials']['SessionToken']
        )
    except Exception as e:
        return e

def new_session_resource(session, res):
    try:
        return session.resource(res)
    except Exception as e:
        return e

def get_security_groups(resource, filters):
    try:
        return resource.security_groups.filter(Filters=filters)
    except Exception as e:
        return e

def get_security_groups_description(resource, filters):
    try:
        return resource.describe_security_groups.filter(Filters=filters)
    except Exception as e:
        return e

def get_ami_data(resource, image):
    try:
        return resource.Image(image)
    except Exception as e:
        return e

def get_subnets(resource, filters):
    ## fix w/ *args
    try:
        return resource.subnets.filter(Filters=filters)
    except Exception as e:
        return e

def get_instances(resource, filters):
    ## fix w/ *args
    try:
        return resource.instances.filter(Filters=filters)
    except Exception as e:
        return e

def parse_security_group_data(security_groups):
    try:
        return [{'id': i.id, 'tags': i.tags, 'rules': i.ip_permissions } for i in security_groups]
    except Exception as e:
        return e

def parse_subnet_data(subnets):
    try:
        return [{
                'subnet_id': i.id, 
                'availability_zone': i.availability_zone, 
                'tags': i.tags,
                'cidr': i.cidr_block } for i in subnets]
    except Exception as e:
        return e

def parse_instance_data(instances):
    ### add tag filter, and extract to output
    """
    def filter_data(string, data):
    try:
        return filter(lambda x : x['Key'] == string, data)
    except Exception as e:
        return e
    """
    try:
        return [{
                'id': i.id, 
                'type': i.instance_type, 
                'state': i.state, 
                'private_ip': i.private_ip_address, 
                'public_ip': i.public_ip_address,
                'tags': i.tags
            } for i in instances]
    except Exception as e:
        return e
######################