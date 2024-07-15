from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession \
    .builder \
    .appName("Our first SPARK SQL example") \
    .config("spark.master", "local[*]") \
    .config("spark.sql.catalogImplementation", "in-memory") \
    .getOrCreate()

try:
    # Read CSV file into DataFrame
    path = "file:///D:/M.Sc Data Science and Computing/Data Engineering/exercise03_car_sales_data.csv"
    user_log = spark.read.csv(path, header=True, inferSchema=True)

    # Print schema and show first 5 rows of the DataFrame
    user_log.printSchema()
    user_log.show()

    # Define output path for JSON file
    out_path = "file:///D:/M.Sc Data Science and Computing/Data Engineering/exercise03_car_sales_data.json"

    # Write DataFrame to JSON format
    user_log.write.json(out_path, mode="overwrite")

    # Read JSON file back into DataFrame
    user_log_2 = spark.read.json(out_path)

    # Print schema and show first 5 rows of the DataFrame
    user_log_2.printSchema()
    user_log_2.show()

except Exception as e:
    print("An error occurred:", e)

finally:
    # Stop the SparkSession
    spark.stop()
