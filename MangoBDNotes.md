**MangoDB**

MongoDB is a document database. It stores data in a type of JSON format called BSON.
A record in MongoDB is a document, which is a data structure composed of key value pairs similar to the structure of JSON objects.



What is SQL?

Structured query language is used to communicate with database. Allows the user to access ad manipulate data stored in the database

```py

{
	title: "Post Title 1",
	body: "Body of post.",
	category: "News",
	likes: 1,
	tags: ["news", "events"],
	date: Date()
}
```

1.Create Database using mongosh

2.To see all available databases, in your terminal type show dbs.

3.You can create a collection using the createCollection() database method.... db.createCollection("posts")
Method 2:
You can also create a collection during the insert process.
...

4. db.posts.insertOne(object)
 insertOne()..
```py
 db.posts.insertOne({
  title: "Post Title 1",
  body: "Body of post.",
  category: "News",
  likes: 1,
  tags: ["news", "events"],
  date: Date()
})
```
5.InsertMany()
To insert multiple documents at once, use the insertMany() method.
```py
db.posts.insertMany([  
  {
    title: "Post Title 2",
    body: "Body of post.",
    category: "Event",
    likes: 2,
    tags: ["news", "events"],
    date: Date()
  },
  {
    title: "Post Title 3",
    body: "Body of post.",
    category: "Technology",
    likes: 3,
    tags: ["news", "events"],
    date: Date()
  },
  {
    title: "Post Title 4",
    body: "Body of post.",
    category: "Event",
    likes: 4,
    tags: ["news", "events"],
    date: Date()
  }
])
```
find()
To select data from a collection in MongoDB, we can use the find() method.
```py
db.posts.find()
```
```py
db.posts.findOne()
```

Querying Data
To query, or filter, data we can include a query in our find() or findOne() methods.
```py
db.posts.find( {category: "News"} )
```

How to do an end query
```py
db.users.find({age:{$gte:40, $lte :20}})

db.users.find({$and: [{age:26}, {name:kyle}]})
#and takes an array.. age and name are objects