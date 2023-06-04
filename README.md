## Zappa

Create a IAM aws user 
Attach policies directly
```
AmazonS3FullAccess
```
Set up aws and check 
```
aws --version
```
Then set up your user credentials
```
aws configure
```
Then setup zappa
```
pip install zappa
zappa init
zappa deploy
```

## Set staticfiles to AWS
#### Paste these environment variables into `.env` file inside the project

```sh
S3_DEFAULT_BUCKET = config("S3_DEFAULT_BUCKET", your_bucket_dev_name)
S3_FILE_BUCKET = config("S3_FILE_BUCKET", your_bucket_files_name)

STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"
AWS_S3_BUCKET_NAME_STATIC = S3_DEFAULT_BUCKET

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % S3_DEFAULT_BUCKET
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

AWS_ACCESS_KEY_ID = config("SERVER_AWS_ACCESS_KEY_ID", '')
AWS_SECRET_ACCESS_KEY = config('SERVER_AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = config('SERVER_AWS_STORAGE_BUCKET_NAME', your_bucket_dev_name)
AWS_S3_REGION_NAME = 'us-east-1'

AWS_S3_ADDRESSING_STYLE = "virtual"
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_DEFAULT_ACL = None
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
```
#### Set AWS Bucket's permissions: 
Set public permission and turn off 'Block all public access'
#### Set bucket policy
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:PutObject",
                "s3:PutObjectAcl",
                "s3:GetObject",
                "s3:GetObjectAcl",
                "s3:DeleteObject"
            ],
            "Resource": [
                "arn:aws:s3:::your_bucket_name",
                "arn:aws:s3:::your_bucket_name/*"
            ]
        }
    ]
}
```
Bucket Ownership
```sh
Permissions -> Ownership -> ACLs enabled 
```
#### Run in terminal for collect static files
```sh
 python manage.py collectstatic
```
Restart your terminal and deploy zappa again for changes to take effect.