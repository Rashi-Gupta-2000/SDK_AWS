import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
# table = dynamodb.create_table(
#     TableName='users2',
#     KeySchema=[
#         {
#             'AttributeName': 'username',
#             'KeyType': 'HASH'
#         },
#         {
#             'AttributeName': 'last_name',
#             'KeyType': 'RANGE'
#         }
#     ],
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'username',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'last_name',
#             'AttributeType': 'S'
#         },
#     ],
#     ProvisionedThroughput={
#         'ReadCapacityUnits': 5,
#         'WriteCapacityUnits': 5
#     }
# )

# # Wait until the table exists.
# table.wait_until_exists()


table = dynamodb.Table('users')

# Print out some data about the table.
# print(table.item_count)
res = table.scan()
data = res['Items']
print(data)

print(table.creation_date_time)

# table.put_item(
#     TableName='users2',
#     Item={
#         'username': 'rg1',
#         'first_name': 'r',
#         'last_name': 'g1',
#         'age': 25,
#         'account_type': 'standard_user',
#     }
# )

# response = table.get_item(
#     TableName='users2',
#     Key={
#         'username': 'rg1',
#         'last_name': 'g1'
#     }
# )
# item = response['Item']
# print(item)


# table.delete_item(
#     TableName='users2',
#     Key={
#         'username': 'rg1',
#         'last_name': 'g1'
#     }
# )

# table.delete()