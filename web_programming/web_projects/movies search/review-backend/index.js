import app from "./server.js";
import { MongoClient } from "mongodb";

const username = "server07052006_db_user";
const pwd = "cwtRRu2iR9Z1tKA0";
const uri = `mongodb+srv://${username}:${pwd}@cluster0.wf8g2uj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0`;

const port = 8000;

async function start() {
  try {
    const client = new MongoClient(uri, {
      maxPoolSize: 50,
    });

    await client.connect();
    console.log("✅ Connected to MongoDB");

    app.listen(port, () => {
      console.log(`🚀 Server listening on port ${port}`);
    });
  } catch (err) {
    console.error("❌ Failed to connect to MongoDB:", err);
    process.exit(1);
  }
}

start();
