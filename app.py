import src.awstools as aws
import datetime
from dateutil.tz import tzutc

def get_new_temporary_session(**kwargs):
    temp_mfa_token = aws.authenticate_mfa_session_token(**kwargs)
    return aws.generate_authorized_session(temp_mfa_token)

if __name__ == "__main__":
    cxn = {
        'DurationSeconds': 3600,
        'SerialNumber': 'arn:aws:iam::<awsaccount>:mfa/username',
        'TokenCode': '<tokencode>'
    }
    temporary_sts_token = aws.authenticate_mfa_session_token(**cxn)
    session = aws.generate_authorized_session(temporary_sts_token)
    ec2 = aws.new_session_resource(session, 'ec2')
    filters = [{'Name': 'tag:env', 'Values': ['staging']}]
    subnets = aws.get_subnets(ec2, filters)
    parsed_subnets = aws.parse_subnet_data(subnets)
    print(parsed_subnets)