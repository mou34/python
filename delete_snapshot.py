import boto3

client = boto3.client('ec2')
del_terget = []
snapshots = []

def get_snapshots_descriptions():
  snapshot = client.describe_snapshots(
  Filters=[ { 'Name': 'volume-id', 'Values': ['ボリュームID'] } ] ) 
  snapshots.append(snapshot)
  
  value = snapshots[0]["Snapshots"]
  for desc in value:
    if not 'Tags' in desc.keys():
      del_terget.append(desc)
  print(del_terget)
  del_terget.sort(key=lambda x:x['StartTime'])
  count = (len(del_terget))
  print(count)

  while count >= 2:
    id = del_terget[0]["SnapshotId"]
    output = client.describe_snapshots(SnapshotIds=[id])
    print(output)
    count -= 1

get_snapshots_descriptions()
