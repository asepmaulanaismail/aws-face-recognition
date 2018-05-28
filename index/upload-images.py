import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[
    ('ae01.jpg','Albert Einstein'),
      ('ae02.jpg','Albert Einstein'),
      ('ae03.jpg','Albert Einstein'),
      ('ae04.jpg','Albert Einstein'),
      ('nb01.jpg','Niels Bohr'),
      ('nb02.jpg','Niels Bohr'),
      ('nb03.jpg','Niels Bohr'),
      ('nb04.jpg','Niels Bohr'),
      ('ami01.jpg','Asep Maulana Ismail'),
      ('ami02.jpg','Asep Maulana Ismail'),
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('family-collection-ysr','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]}
                    )