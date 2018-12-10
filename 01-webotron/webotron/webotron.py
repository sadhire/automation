
import boto3
#import sys
import click
from botocore.exceptions import ClientError
from pathlib import Path

session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webotron deploys websites to AWS"
    pass

@cli.command('list-buckets')
#@click.command('list_buckets')

def list_buckets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket')
#def list_bucket_objects():
def list_bucket_objects(bucket):
    "List Objects in an S3 bucket"
    for obj in s3.Bucket(bucket).objects.all():
    #for obj in s3.Bucket('sadanand-automationaws').objects.all():
        print(obj)

@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    "Create and Configure Bucket"
    try:
        s3_bucket = s3.create_bucket(
                            Bucket=bucket,
                            CreateBucketConfiguration={'LocationConstraint' : session.region_name}
                        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            s3_bucket = s3.Bucket(bucket)
            print("Bucket Already Owned By You")
        else:
            raise e


    policy = """
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicReadGetObject",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::%s/*"
            }
        ]
    }
    """ % s3_bucket.name

    policy = policy.strip()
    pol = s3_bucket.Policy()
    pol.put(Policy=policy)

    ws = s3_bucket.Website()
    ws.put(WebsiteConfiguration={
                'ErrorDocument': {'Key': 'error.html'},
                'IndexDocument': {'Suffix': 'index.html'}
            })

    return



#def just_test():
#    "Test Function"
#    print("Test Function")

if __name__ == '__main__':
    cli()
    #list_buckets()
    #print("Hello, World!")
    #print(sys.argv)
    #for bucket in s3.buckets.all():
    #    print(bucket)
