const {MongoClient} = require('mongodb')

const uri = "mongodb+srv://admin:Fattycakes69!@cluster0.5vabn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
client.connect(err => {
  if (err) console.log(err)
  else console.log('connected')
  const collection = client.db("test").collection("devices");
  // perform actions on the collection object
  client.close();
})