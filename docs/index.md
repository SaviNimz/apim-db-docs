# WSO2 API Manager: Database Guide

This site explains **what WSO2 API Manager (APIM) stores in its database, and why**. It covers what each table is for and how the tables connect. It also shows which rows get written when someone creates an API, subscribes to it, generates keys or calls it.

It's written for developers, support engineers and DBAs who are new to APIM. It uses plain language and small diagrams. For the exact columns, see the [table reference](apim-4/reference/index.md).

<div class="grid cards" markdown>

-   :material-numeric-4-box:{ .lg .middle } **APIM 4.x series**

    ---

    Documented from **WSO2 API Manager 4.7.0**. Covers revisions, gateway environments, organizations, operation policies, governance and AI APIs.

    [:octicons-arrow-right-24: Start with 4.x](apim-4/index.md)

-   :material-numeric-3-box:{ .lg .middle } **APIM 3.x series**

    ---

    Documented from **WSO2 API Manager 3.2.0**. Covers the classic model, where APIs are published to gateway labels and the API's identity lives in the registry.

    [:octicons-arrow-right-24: Start with 3.x](apim-3/index.md)

-   :material-compare-horizontal:{ .lg .middle } **3.x vs 4.x**

    ---

    What changed between the two series, table by table and flow by flow. Useful when you're migrating.

    [:octicons-arrow-right-24: Compare](comparison.md)

-   :material-book-open-variant:{ .lg .middle } **New here?**

    ---

    Learn how to read the diagrams, and look up APIM terms such as *subscription*, *key manager* or *revision*.

    [:octicons-arrow-right-24: How to read this site](how-to-read.md)

</div>

## How to use this site

1. **Get the big picture.** Read the series *Overview* and *The databases* pages.
2. **Follow a flow.** The *Core flows* pages tell the story of APIM step by step, e.g. "a developer subscribes to an API", and show exactly which tables are touched.
3. **Go deep on a domain.** The *Domains* pages explain groups of related tables, such as applications and subscriptions, or keys and tokens.
4. **Look up a table.** The *Table reference* lists every table and column, generated straight from the product's database scripts.

!!! info "Where this comes from"
    Everything here is derived from the database scripts shipped with each product (`dbscripts/apimgt/mysql.sql` and `dbscripts/mysql.sql`). The other database vendors (Oracle, PostgreSQL, MSSQL, DB2, H2) use the same logical schema.
