# Django_CRM
This is a basic Costumer relationship manager app for diagnosis lab, built using Django and MySQL
------------
## Contents
* [Banner](#Banner)
* [Folder Structure](#FolderStructure)
* [Installations and Instruction](#Installations)
* [Snapshots](#Snapshots)
* [Support & Contributions](#Support_and_Contributions)
----

### Banner

<img src="https://github.com/debasish2110/Django_CRM/blob/master/snapshots/1_log_in_home.png" width="920" height="420">

-----
### FolderStructure

Folder        | description
--------------| ----------------------------------------------
`CustomerRelationshipManager`        | This folder contains the source code.
`snapshots`                          | screenshots of the code output are placed here.

* Open the **[Project Folder](https://github.com/debasish2110/Django_CRM/tree/master/CustomerRelationshipManager)** folder for the source code...

-----
### Installations

The code is written in Python 3.10 and the Os used is Windows 10. If you dont have python installed you can find it [here](https://www.python.org/downloads/).

mysql shell and server needs to be installed [mySQL-here](https://dev.mysql.com/downloads/installer/).

```
# clone the repo
$ git clone https://github.com/debasish2110/Django_CRM.git

# change the working directory to CustomerRelationshipManager
$ cd CustomerRelationshipManager
=================================
# install the requirements
$ pip3 install -r requirements.txt
=================================

# run the code to create ur database [one time run required.] 
$ python mys_db.py

# push the migrations
$ python manage.py makemigrations
$ python manage.py migrate

# run the code
$ python manage.py runserver
```
-----
* reach me out for any queries:-> [Instagram](https://www.instagram.com/_da_wanderlust_/) | [twitter](https://twitter.com/Debashish2110) | [Linkedin](https://www.linkedin.com/in/debashish98/)

### Snapshots

**Login**

<img src="https://github.com/debasish2110/Django_CRM/blob/master/snapshots/1_log_in_home.png" height="500" width="950">

**Home page and Dashboard**
<img src="https://github.com/debasish2110/Django_CRM/blob/master/snapshots/2_record_dashboard.png" height="500" width="950">

**Home page and Dashboard**
<img src="https://github.com/debasish2110/Django_CRM/blob/master/snapshots/3_complete_details.png" height="500" width="950">

**Add new record**
<img src="https://github.com/debasish2110/Django_CRM/blob/master/snapshots/4_add_record.png" height="500" width="950">

**Log Out**
<img src="https://github.com/debasish2110/Django_CRM/blob/master/snapshots/5_logout.png" height="500" width="950">


### Support_and_Contributions
- Please ⭐️ this repository if this project helped you!
- Contributions of any kind is always welcome!
- Feel free to reach out if you have any query.

