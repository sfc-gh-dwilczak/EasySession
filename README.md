# Snowauth.
A package for the simple local management of snowpark for python connections.

# Example:



### Setup:
Install the python package.
```
pip install snowauth
```

Create a file name ``creds.conf``.
```
[connection]
account   = "ACCOUNT"
user      = "USER"
password  = "PASSWORD"
role      = "ROLE"
warehouse = "WAREHOUSE"
```

### Usage

```py
import snowauth

# creds.conf is the default. It can be change to whatever name you want.
session = snowauth.connect('connection','creds.conf')

print(session)
```

### Output:
```
<snowflake.snowpark.session.Session: account=...>
```
