# SQL Server (per readme, no longer used and not needed)
db_name = "database"
db_username = "usre@machine"
db_password = "americawasgreatalready"
db_server = "tcp:somemachine,1433"
_driver = "{ODBC Driver 13 for SQL Server}"
db_tablename = "tablaname"
db_connection_string = "Driver={driver};Server={server};Database={database};Uid={db_username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;".format(server=db_server, driver=_driver, database=db_name, db_username=db_username, password=db_password)

# Azure Table
table_name = 'courtreminder' # can use this value
storage_account = 'account'
table_connection_string = 'connectionstring'

# Used for azure blob store, where we upload raw files.
# blob_accountname is used in server/admin_app and storage/filestorage, passed as an argument to BlockBlobStorage
# Per the documentation here https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python#configure-your-storage-connection-string
# it appears that this corresponds to the storage account name, which is also stored under the variable storage_account
blob_accountname = "court" # not mentioned in readme, but appears to be used (maybe storage_account name?)
blob_key = "mah_blob"
blob_container = "somecontainer"
local_tmp_dir = "/tmp"

# sentry (nothing in the readme about this, but it's used in extract_runner.py and runners.py)
sentry_dsn = ''
