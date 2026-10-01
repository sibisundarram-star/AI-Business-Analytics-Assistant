def generate_executive_summary(df, dataset_info, business_profile, context):

    missing = df.isnull().sum().sum()

    summary = f"""
## 📋 Executive Summary

This dataset contains **{dataset_info['rows']:,} records**
across **{dataset_info['columns']} columns**.

### Business Domain
**{context['domain']}**

### Data Quality

• Missing Values: **{missing:,}**

• Duplicate Rows: **{dataset_info['duplicate_rows']}**

### Available Data

• Numeric Columns: **{len(dataset_info['numeric_columns'])}**

• Categorical Columns: **{len(dataset_info['categorical_columns'])}**

### Potential Target Columns

{', '.join(map(str, business_profile["target_candidates"])) if business_profile["target_candidates"] else "No obvious target column detected."}

### Initial Assessment

This dataset appears suitable for exploratory data analysis,
dashboard creation, and machine learning after appropriate
data cleaning.

"""

    return summary