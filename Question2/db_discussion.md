## Relationship Clarifications
There are several columns presented in the widgets.tsv, that seem like they
could be related but with the small sample dataset do not change.

1. Do we expect that our widgets could come from different suppliers?  If so, 
it is highly likely that the cost will vary by vendor.  For this reason,
I have 2 primary indexes for cost: widget_id and supplier_id since we will likely
need both to uniquely identify the cost.

2.  Is the inventory denoted in the .tsv for the total product available or by 
warehouse?  The current dataset is ambiguous as each product is sourced from
a single supplier and single warehouse combination.  I have defined the schema
to be more restrictive requiring widget, supplier, and warehouse ids as primary key.

3. I do note that Big Traps and Raytheon share a 3-letter warehouse code - MSP.
This means that we need both customer_id and warehouse_code to uniquely identify
the warehouse tied back to a new unique warehouse_id number.  My schema reflects
this need to avoid ambiguity.

4. I have set primary indices for the packaging table, generating a package ID
for each unique combination of widget_id, container, and quantity.  I considered
that bags, boxes, and crates are not necessary the same for all products. Although
this takes up additional storage space where we now have 2 records for a 'bag of 10',
those packaging materials (weight, color, labeling) may differ and this allows
for easier insertion as the database matures.