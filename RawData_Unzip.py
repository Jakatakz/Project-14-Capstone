
# coding: utf-8

# In[2]:


import gzip
import shutil
with gzip.open('endomondoHR.json.gz', 'rb') as f_in:
    with open('endomondoHR.json', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

