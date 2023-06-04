# Databricks notebook source
sql(f"drop table if exists tmp")

sql(
    f""" create or replace table tmp(
   col1 string,
   col2 string)
using delta location '/tables/tmp'"""
)

# COMMAND ----------

# MAGIC %sql
# MAGIC alter table
# MAGIC   delta.`/tables/tmp`
# MAGIC set
# MAGIC   tblproperties (
# MAGIC     'delta.columnMapping.mode' = 'name',
# MAGIC     'delta.minReaderVersion' = '2',
# MAGIC     'delta.minWriterVersion' = '5'
# MAGIC   )

# COMMAND ----------

# MAGIC %sql
# MAGIC alter table
# MAGIC   delta.`/tables/tmp` rename column col1 to `col 1`

# COMMAND ----------

# MAGIC %sql
# MAGIC select
# MAGIC   *
# MAGIC from
# MAGIC   delta.`/tables/tmp`
