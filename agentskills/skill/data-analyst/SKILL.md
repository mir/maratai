---
name: data-analyst
description: Data analysis master. Use when asked to query a database, explore schema, analyze data, run SQL, or investigate tables.
---
# Database Analytics Skill

Query databases for data analysis using command-line clients, e.g.:
- PostgreSQL: `psql`
- MySQL: `mysql`
- ClickHouse: `clickhouse-client`
- BigQuery: `bq`
- Snowflake: `snowsql`
or any other database.


# Connection

Connect using environment variables:

| Variable | Description | Example |
|---|---|---|
| `DB_HOST` | Database hostname | `localhost` |
| `DB_PORT` | Port number | `5432` |
| `DB_DATABASE` | Database name | `analytics` |
| `DB_USER` | Username | `analyst` |
| `DB_PASSWORD` | Password | (set in env) |

Verify connectivity before running queries:
```bash
psql -c "SELECT 1"
```

# Prepare metadata
Explore database structure before writing any queries.

1. Explore which datasets there are
2. Explore which tables there are in db
3. Using db-specific queries fetch the schema of a table
4. If the table is small enough for each column
fetch 10 most common distinct values.
If the table is too large, use sampling specific to db.

# SQL Best Practices

- Use CTEs over subqueries
- Select specific columns, never SELECT *
- ORDER BY <date> DESC
- Always add `LIMIT 10` (or less) when exploring data. Only remove the limit once you understand the result set size. Otherwise prefer outputting to a file
in csv, parquet, json, or other formats
- Use descriptive aliases, never one-symbol short abbreviations
- Before building complex analytics, verify assumptions doing MIN/MAX/COUNT aggregations for columns
- EXPLAIN ANALYZE for expensive queries
- Default time conditions
When the user does not specify a time range, use sensible defaults:

| Query type | Default range |
|---|---|
| Trend / time-series | Last 30 days |
| Snapshot / current state | Last 7 days |
| Comparison (MoM, WoW) | Current vs previous period |
| "Recent" | Last 7 days |

Use `CURRENT_DATE - INTERVAL '...'` for relative date filters
- Data freshness. Analytical databases may have ETL lag. If results look unexpectedly empty for recent dates - exclude it and report to the user

# Error resolution

When a query returns zero rows, too many nulls, all-zeros columns
1. **Check column range** - verify with `min/max` that data exists for the period
2. **Relax filters** - remove one filter at a time to find which condition excludes all rows
3. **COUNT confirmation** - run a simple `count(*)` with each filter added incrementally
4. **Explain to the user** - state clearly that no data matched and why
5. **Never fabricate data** - do not invent rows, approximate, or guess values

# Output Guidelines
- Markdown tables for small results
- Shortened numbers
Use human-readable formats for large numbers:
    - 1,234,567 -> 1.23M
    - 45,678 -> 45.7K
    - 0.1234 -> 12.3%
- Chart recommendations
    - Time series -> line chart
    - Category comparison -> bar chart
    - Proportions -> pie chart or stacked bar
    - Distribution -> histogram
- When the user asks something that resembles common known metrics
    - Suggest the common definition of that metric
    - Shortly explain how it is different from what user asks, PRO/CONs

# Dashboards formats
- ASCII charts directly in the output
- png images using python
- interactive javascript charts
