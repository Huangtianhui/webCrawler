import pymongo 
connection=pymongo.MongoClient();
tdb=connection.MongoProject
post_info=tdb.test;

jike={'name':'jike','age':'5','skill':'python'}

post_info.insert(jike)
#post_info.remove()