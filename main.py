
import boto3

BUCKET_NAME="my-python-buckets"


access_key='AKIA3DZZXK7JNCKDEHWM'

access_secret_key='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'

client_s3=boto3.client('s3',aws_access_key_id=access_key,aws_secret_access_key=access_secret_key)

#List Buckets
# bucket_response=client_s3.list_buckets()
# for bucket in bucket_response["Buckets"]:
#     print(bucket_response)

#Upload File
# with open ('./burger.jpeg','rb')as f:
#     client_s3.upload_fileobj(f,BUCKET_NAME,"burger_new_upload.jpg")

#Download File (ilk parametre hangi bucketname, indirelecek dosyanın adı,dosyanın indirildikten sonra kayıt edilecek adı)
#client_s3.download_file(BUCKET_NAME,"burger_new_upload.jpg","downloaded_burger.jpg")


# with open('downloaded_burger.jpg','wb')as f:
#     client_s3.download_fileobj(BUCKET_NAME,f,"burger_new_upload")
    #Download File Object(İndirilen dosyayı ön yüze göndermek için kodlar bu kısımda yazılır)


# Delete File
# reponse=client_s3.delete_object(Bucket=BUCKET_NAME,Key='burger_new_upload.jpg')
# print(response)

