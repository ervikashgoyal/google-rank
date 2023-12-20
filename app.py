import streamlit as st
from googlesearch import search
import pandas as pd
import itertools
import time

def get_top_results(keyword, num_results=100, delay=2):
    results = []
    for url in itertools.islice(search(keyword, num_results=num_results), num_results):
        results.append(url)
        time.sleep(delay)  # Introduce a delay to avoid rate limiting

    return results

def create_dataframe(results):
    data = {'URL': results, 'Title': []}
    for url in results:
        data['Title'].append('')  # Placeholder for title, you can extract title using additional code

    df = pd.DataFrame(data)
    return df

def main():
    st.title("Top 100 Search Results Viewer")

    search_keyword = st.text_input("Enter the keyword:")
    
    if st.button("Search"):
        st.info("Searching... Please wait.")
        search_results = get_top_results(search_keyword)
        df = create_dataframe(search_results)

        st.success("Search complete!")
        st.write("Top 100 Results:")
        st.write(df)

if __name__ == "__main__":
    main()
