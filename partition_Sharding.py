# you have two choices if your database is scalling and you ar running out of space quickly
# two choices
# make the machine and database bigger aka vertical scalling
# slice the data in peices and save int multiple databases and possibly multiple machines aka horizontal scaling 


# veritcal scaling can only get you sof far. you are limited by the memory and diesk size of a single machine 
# if something goes wrong wit that machine you are toast 
# that is why horizontal scaling is more desirable for large web applications 

# we can partition a large database into smaller databases (shards) according to certain rules 
# naturally there are two ways to partition the databse 
# can partition by row or by column into smaller databases 

# vertical sharding is splitting up the db via columns and horizontal is by rows 
# horizontal sharding is most common used in SQL databases 
# we can shard by certain attributes like region, time of the year or a hash partition 

# in the following example we are going to understand how data partitioning works with SQL databases 
# and do a real example with mySQL


