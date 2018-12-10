

import boto3

# import sys
import click

from bucket import BucketManager
# import bucket

session = boto3.Session(profile_name='pythonAutomation')
bucket_manager = BucketManager(session)
# s3 = session.resource('s3')

@click.group()
def cli():
    "Webotron deploys websites to AWS"
    pass

@cli.command('list-buckets')
#@click.command('list_buckets')

def list_buckets():
    "List all s3 buckets"
    # for bucket in bucket_manager.s3.buckets.all():
    for bucket in bucket_manager.all_buckets():
        print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket')
#def list_bucket_objects():
def list_bucket_objects(bucket):
    "List Objects in an S3 bucket"
    for obj in bucket_manager.all_objects(bucket):
        print(obj)
    # for obj in s3.Bucket(bucket).objects.all():
    # for obj in s3.Bucket('sadanand-automationaws').objects.all():

@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    "Create and Configure Bucket"
    s3_bucket = bucket_manager.init_bucket(bucket)
    bucket_manager.set_policy(s3_bucket)
    bucket_manager.configure_website(s3_bucket)
    return


@cli.command('sync')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucket')
def sync(pathname,bucket):
    "Sync Contents of PATHNAME to Bucket"
    bucket_manager.sync(pathname, bucket)

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
