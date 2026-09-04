# Databricks notebook source
# MAGIC %md
# MAGIC # BTT Sample Notebook
# MAGIC A minimal notebook so the bundle has a real task to deploy and run.
# MAGIC It reads the deploy target passed in as a job parameter and prints a row.

# COMMAND ----------

# The job passes the current bundle target (dev / prod) as a parameter.
dbutils.widgets.text("target", "dev")
target = dbutils.widgets.get("target")

# COMMAND ----------

import datetime

print(f"BTT DABs sample job running in target: {target}")
print(f"Run timestamp: {datetime.datetime.utcnow().isoformat()}Z")

# COMMAND ----------

# A tiny bit of real work so the run produces output.
df = spark.createDataFrame(
    [(target, "hello-from-dabs", datetime.datetime.utcnow().isoformat())],
    ["target", "message", "run_ts"],
)
df.show(truncate=False)
