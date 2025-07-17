from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import *

# Spark Session
spark = SparkSession.builder \
    .appName("KafkaToPostgres") \
    .config("spark.jars", "C:\\Users\\Lenovo\\Desktop\\data platform project\\postgresql-42.7.7.jar") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.13:3.5.1") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

#  schema 
schemas = {
    "crm_events": StructType([
        StructField("event", StringType()),
        StructField("lead_id", IntegerType()),
        StructField("agent", StringType()),
        StructField("timestamp", StringType())
    ]),

    "erp_events": StructType([
        StructField("event_type", StringType()),
        StructField("property_id", StringType()),
        StructField("address", StringType()),
        StructField("listing_price", DoubleType()),
        StructField("currency", StringType()),
        StructField("agent", StringType()),
        StructField("buyer_id", StringType()),
        StructField("buyer_name", StringType()),
        StructField("contract_value", DoubleType()),
        StructField("status", StringType()),
        StructField("legal_team", StringType()),
        StructField("amount", DoubleType()),
        StructField("payment_method", StringType()),
        StructField("transaction_ref", StringType()),
        StructField("timestamp", StringType()),
        StructField("sap_transaction_id", StringType())
    ]),

    "website_events": StructType([
        StructField("log_id", StringType()),
        StructField("event_type", StringType()),
        StructField("user_id", StringType()),
        StructField("timestamp", StringType())
    ]),

    "app_events": StructType([
        StructField("event_type", StringType()),
        StructField("data", MapType(StringType(), StringType())),
        StructField("timestamp", StringType())
    ])
}

# PostgreSQL config
pg_url = "jdbc:postgresql://localhost:5432/Data Platform Project"
pg_properties = {
    "user": "",
    "password": "",
    "driver": "org.postgresql.Driver"
}

# Kafka topics
topics = list(schemas.keys())

raw_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", ",".join(topics)) \
    .option("startingOffsets", "earliest") \
    .load()

value_df = raw_df.selectExpr("CAST(topic AS STRING)", "CAST(value AS STRING)")

streams = []

def write_to_postgres_and_report(batch_df, batch_id, table_name):
    input_count = batch_df.count()
    print(f"[{table_name}] Batch {batch_id} received → {input_count} records")

    batch_df.write \
        .mode("append") \
        .option("createTableOptions", "") \
        .jdbc(pg_url, table=table_name, properties=pg_properties)

    try:
        pg_df = spark.read.jdbc(pg_url, table_name, properties=pg_properties)
        total_count = pg_df.count()
        print(f"[{table_name}] Batch {batch_id} ✔ PostgreSQL row count = {total_count}")
    except Exception as e:
        print(f"[{table_name}] Batch {batch_id} ⚠ Failed to count rows: {e}")

for topic in topics:
    schema = schemas[topic]

    df = value_df.filter(col("topic") == topic)
    parsed = df.select(from_json(col("value"), schema).alias("data")).select("data.*")
    cleaned = parsed.na.drop("all")

    json_query = cleaned.writeStream \
        .format("json") \
        .option("path", f"output/{topic}") \
        .option("checkpointLocation", f"output/checkpoints/{topic}") \
        .outputMode("append") \
        .start()

    streams.append(json_query)

    pg_query = cleaned.writeStream \
        .foreachBatch(lambda df, bid: write_to_postgres_and_report(df, bid, topic)) \
        .outputMode("append") \
        .option("checkpointLocation", f"output/checkpoints/pg_{topic}") \
        .start()

    streams.append(pg_query)

for q in streams:
    q.awaitTermination()
