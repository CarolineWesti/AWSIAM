import boto3
import datetime
import time

sts = boto3.client("sts")
account_id = sts.get_caller_identity()["Account"]
client = boto3.client("iam")

calls = [
    ("get_user", {}),
    ("get_user", {"UserName": "admin"}),
    ("get_user", {"UserName": "root"}),
    ("get_user", {"UserName": "deploy"}),
    ("get_user", {"UserName": "terraform"}),
    ("get_user", {"UserName": "jenkins"}),
    ("get_user", {"UserName": "devops"}),
    ("get_user", {"UserName": "backup"}),
    ("get_user", {"UserName": "monitoring"}),
    ("get_user", {"UserName": "security"}),
    ("get_account_summary", {}),
    ("get_account_password_policy", {}),
    ("get_account_authorization_details", {}),
    ("get_credential_report", {}),
    ("get_login_profile", {"UserName": "admin"}),
    ("get_login_profile", {"UserName": "root"}),
    ("get_login_profile", {"UserName": "deploy"}),
    ("get_login_profile", {"UserName": "terraform"}),
    ("get_login_profile", {"UserName": "jenkins"}),
    ("get_login_profile", {"UserName": "devops"}),
    ("get_role", {"RoleName": "admin"}),
    ("get_role", {"RoleName": "AdminRole"}),
    ("get_role", {"RoleName": "PowerUserRole"}),
    ("get_role", {"RoleName": "LambdaExecutionRole"}),
    ("get_role", {"RoleName": "EC2Role"}),
    ("get_group", {"GroupName": "Admins"}),
    ("get_group", {"GroupName": "Developers"}),
    ("get_group", {"GroupName": "DevOps"}),
    ("get_group", {"GroupName": "Security"}),
    ("get_group", {"GroupName": "ReadOnly"}),
    ("get_policy", {"PolicyArn": f"arn:aws:iam::{account_id}:policy/admin"}),
    ("get_policy", {"PolicyArn": f"arn:aws:iam::{account_id}:policy/deploy"}),
    ("get_policy", {"PolicyArn": f"arn:aws:iam::{account_id}:policy/readonly"}),
    ("get_policy", {"PolicyArn": f"arn:aws:iam::{account_id}:policy/security"}),
    ("get_policy", {"PolicyArn": f"arn:aws:iam::{account_id}:policy/lambda-policy"}),
    ("get_instance_profile", {"InstanceProfileName": "admin"}),
    ("get_instance_profile", {"InstanceProfileName": "ec2-profile"}),
    ("get_instance_profile", {"InstanceProfileName": "web-server"}),
    ("get_server_certificate", {"ServerCertificateName": "web-cert"}),
    ("get_server_certificate", {"ServerCertificateName": "api-cert"}),
    ("get_saml_provider", {"SAMLProviderArn": f"arn:aws:iam::{account_id}:saml-provider/ADFS"}),
    ("get_saml_provider", {"SAMLProviderArn": f"arn:aws:iam::{account_id}:saml-provider/Okta"}),
    ("get_ssh_public_key", {"UserName": "admin", "SSHPublicKeyId": "APKA00000000000000000", "Encoding": "SSH"}),
    ("get_ssh_public_key", {"UserName": "deploy", "SSHPublicKeyId": "APKA00000000000000000", "Encoding": "SSH"}),
]

count = 0
for method, params in calls:
    count += 1
    ts = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        result = getattr(client, method)(**params)
        print(f"{ts} [{count}] iam.{method} - ALLOWED")
    except Exception as e:
        error = str(e)[:80]
        print(f"{ts} [{count}] iam.{method} - DENIED/FAILED - {error}")
    time.sleep(1)

print(f"\nTotal IAM Get API calls: {count}")
