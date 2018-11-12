import boto3
from zipfile import ZipFile
import urllib.request as url

BUCKET_NAME = "openoil.org"
TMP_FILE = "/tmp/historical.zip"

def lambda_handler(event, context):
    file = url.URLopener()
    try:
        file.retrieve("http://www.bogc.dnrc.mt.gov/production/historical.zip", TMP_FILE)

        with ZipFile(TMP_FILE) as zip: 
            file_leaseProd = zip.read('histLeaseProd.tab')
            file_wellProd = zip.read('histprodwell.tab')
            file_wellData = zip.read('histWellData.tab')

            s3 = boto3.resource('s3')
            s3.Bucket(BUCKET_NAME).put_object(Key='MT_leaseProd.tab',
                                              Body=file_leaseProd)
            s3.Bucket(BUCKET_NAME).put_object(Key='MT_wellProd.tab',
                                              Body=file_wellProd)
            s3.Bucket(BUCKET_NAME).put_object(Key='MT_wellData.tab',
                                              Body=file_wellData)
    except Exception as e:
        print(e)
        raise e