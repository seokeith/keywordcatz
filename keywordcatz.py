import streamlit as st
import pandas as pd
import io
import base64

def categorize_keywords(keywords, primary_categories, secondary_categories):
    result = []
    for keyword in keywords:
        category_1 = None
        category_2 = None
        
        for category in primary_categories:
            if category.lower() in keyword.lower():
                category_1 = category
                break
                
        for category in secondary_categories:
            if category.lower() in keyword.lower():
                category_2 = category
                break

        result.append((keyword.strip(), category_1, category_2))
    return result

# Streamlit interface
st.title('Keyword Categorizer')

# 1. Get the list of keywords
keywords = st.text_area('Enter the list of keywords (comma separated)').split(',')

# 2. Get the list of primary categories
primary_categories = st.text_area('Enter the list of PRIMARY categories (comma separated)').split(',')

# 3. Get the list of secondary categories
secondary_categories = st.text_area('Enter the list of SECONDARY categories (comma separated)').split(',')

if st.button('Categorize'):
    results = categorize_keywords(keywords, primary_categories, secondary_categories)
    df = pd.DataFrame(results, columns=["Keyword", "Category 1", "Category 2"])
    
    # Display results in table format
    st.write(df)

    # Provide an option to download the DataFrame as CSV
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="keywords_categories.csv">Download as CSV</a>'
    st.markdown(href, unsafe_allow_html=True)
