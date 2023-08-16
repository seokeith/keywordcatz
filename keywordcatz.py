import streamlit as st

def categorize_keywords(keywords, primary_categories, secondary_categories):
    result = {}
    for keyword in keywords:
        keyword_category = "Uncategorized"
        for category in primary_categories:
            if category.lower() in keyword.lower():
                keyword_category = category
                break
        
        if keyword_category == "Uncategorized":
            for category in secondary_categories:
                if category.lower() in keyword.lower():
                    keyword_category = category
                    break

        result[keyword] = keyword_category
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
    
    # Display results in table format
    st.write('Keyword - Category')
    st.write('------------------')
    for keyword, category in results.items():
        st.write(f'{keyword.strip()} - {category.strip()}')
