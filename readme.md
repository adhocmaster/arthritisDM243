# Overall Goals
1. Data cleaning and transformation
2. Correlation and distribution analysis
3. Identifying potential significant features through visualization
4. Implement a few statistical models and identify significant features
5. Model function based on significant features and their probable correlation.
6. Report on data quality
7. Report on model performance

# Probable list of removable fields

1. Dx_Change
2. New_Dx


# Transformations:

## Disease Name Transformations:
1. Find unique diseases
2. Fix duplicates
3. Convert to short names and transform all diseases in different columns


## Other fiels transformations

There are two kinds of other fields associated with different questions:
1. For some questions, other field is a categorical value
2. For others, other is a NA/1 value (NA means 0 here). And a text field specifying the other value.

We are transforming the values as a single categorical value column having {None, other values}