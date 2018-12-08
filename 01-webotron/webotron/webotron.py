import boto3
#import sys
import click

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
