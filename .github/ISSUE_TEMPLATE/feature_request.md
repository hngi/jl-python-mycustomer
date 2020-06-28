---
name: Feature request
about: Suggest an idea for this project
title: ''
labels: ''
assignees: ''

---

**What Functionality / Service / Endpoint would you like to add?**
A short statement

**Describe this Functionality / Service / Endpoint**
A clear and concise description of what you want to add.

**Duplicate prevention**
Have you checked that this issue has not been opened by anyone  else?

**Describe how to intend to go about adding this feature**
Describe the approach you will take in adding this feature. 

**Slack username**
Please include your slack username here

**Additional context**
Add any other context or screenshots about the feature request here.



### If you're working on an endpoint
- search the **"swagger.yaml"** file in the base dir for the enpoint you're working on, example:  /store/update/{storeId}

- then uncomment the section of the file under that endpoint

- now change operationId of that endpoint to the full qualifier for your function,

  example:  **operationId: "updateStore"  ==> operationId: endpoints.store.update** 
  
  where **"update"** is the function, **"store"** is the file (store.py) and **"endpoints"** is the directory containing that file
  
  
