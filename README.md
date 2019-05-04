# PYNETCAP

Read *Netcap* audit records from Python!

Currently it is possible to retrieve the audit records as python dictionary:

```python
#!/usr/bin/python

import pynetcap as nc

reader = nc.NCReader('pcaps/HTTP.ncap.gz')

reader.read(dataframe=False)
print("RECORDS:")
print(reader.records)
```

or as pandas dataframe:

```python
#!/usr/bin/python

import pynetcap as nc

reader = nc.NCReader('pcaps/HTTP.ncap.gz')

reader.read(dataframe=True)
print("[INFO] completed reading the audit record file:", reader.filepath)
print("DATAFRAME:")
print(reader.df)
```