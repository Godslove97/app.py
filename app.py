# import streamlit as st
# import pandas as pd
# import graphviz
#
# # Title and Description
# st.title("Genealogy Explorer")
# st.write("An interactive app to explore and visualize family trees.")
#
# # Sidebar: Data Input
# st.sidebar.header("Upload Family Data")
# uploaded_file = st.sidebar.file_uploader("Upload a CSV file with family data", type=["csv"])
#
# # Initialize 'data' as an empty DataFrame
# data = pd.DataFrame()
#
# # Process the uploaded file
# if uploaded_file:
#     try:
#         # Load the uploaded CSV file into a DataFrame
#         data = pd.read_csv(uploaded_file)
#         st.write("Uploaded Family Data:")
#         st.dataframe(data)
#
#         # Family Tree Visualization
#         st.subheader("Family Tree")
#         dot = graphviz.Digraph()
#
#         # Add nodes and edges to the family tree
#         # for _, row in data.iterrows():
#         #     dot.node(str(row["ID"]), row["name": str])
#         #     if not pd.isna(row["ParentID"]):
#         #         dot.edge(str(row["ParentID"]), str(row["ID"]))
#
#         # Render the family tree
#         st.graphviz_chart(dot)
#
#     except Exception as e:
#         st.error(f"Error loading the file: {e}")
# else:
#     st.write("**Please upload a CSV file to explore the family tree.**")
#
# # Search Functionality
# st.subheader("Search for a Relative")
# if not data.empty:  # Ensure 'data' is loaded before searching
#     search_name = st.text_input("Enter a name to search:")
#     if search_name:
#         results = data[data["Name"].str.contains(search_name, case=False, na=False)]
#         if not results.empty:
#             st.write("Search Results:")
#             st.dataframe(results)
#         else:
#             st.write("No relatives found with that name.")
# else:
#     st.write("Search functionality will be available after uploading a file.")





# import streamlit as st
# import pandas as pd
# import graphviz
#
# # Title and Description
# st.title("🌳 Genealogy Explorer")
# st.write("Explore and visualize your family tree with this interactive app!")
#
# # Sidebar: Data Input
# st.sidebar.header("Upload Family Data")
# uploaded_file = st.sidebar.file_uploader("Upload a CSV file with family data", type=["csv"])
#
# # Initialize 'data' as an empty DataFrame
# data = pd.DataFrame()
#
# # Process the uploaded file
# if uploaded_file:
#     try:
#         # Load the uploaded CSV file into a DataFrame
#         data = pd.read_csv(uploaded_file)
#         st.success("Family data successfully loaded!")
#         st.write("### 📋 Uploaded Family Data:")
#         st.dataframe(data)
#
#         # Family Tree Visualization
#         st.write("### 🌟 Family Tree Visualization")
#         dot = graphviz.Digraph(format="png")
#
#         # Customize the graph appearance
#         dot.attr(rankdir="TB", size="10", dpi="100")  # Top-to-bottom layout, larger size
#
#         # Define global node and edge styles
#         dot.attr("node", shape="ellipse", style="filled", color="lightblue", fontname="Arial", fontsize="10")
#         dot.attr("edge", color="gray", arrowsize="0.5")
#
#         # Add nodes and edges to the family tree
#         for _, row in data.iterrows():
#             node_id = str(row["ID"])
#             label = row["Name"]
#
#             # Add nodes with custom labels
#             dot.node(node_id, label)
#
#             # Add edges if ParentID is present
#             if not pd.isna(row["ParentID"]):
#                 dot.edge(str(row["ParentID"]), node_id)
#
#         # Render the family tree
#         st.graphviz_chart(dot)
#
#     except Exception as e:
#         st.error(f"Error loading the file: {e}")
# else:
#     st.write("**📂 Please upload a CSV file to explore the family tree.**")
#
# # Search Functionality
# st.write("### 🔎 Search for a Relative")
# if not data.empty:  # Ensure 'data' is loaded before searching
#     search_name = st.text_input("Enter a name to search:")
#     if search_name:
#         results = data[data["Name"].str.contains(search_name, case=False, na=False)]
#         if not results.empty:
#             st.write("### 🎯 Search Results:")
#             st.dataframe(results)
#         else:
#             st.warning("No relatives found with that name.")
# else:
#     st.info("Search functionality will be available after uploading a file.")



import streamlit as st
import pandas as pd
import plotly.express as px

# Title and Description
st.title("🌳 Genealogy Explorer")
st.write("Explore and visualize your family tree with an interactive tree chart!")

# Sidebar: Data Input
st.sidebar.header("Upload Family Data")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file with family data", type=["csv", "png", "JPG"])

# Initialize 'data' as an empty DataFrame
data = pd.DataFrame()

# Process the uploaded file
if uploaded_file:
    try:
        # Load the uploaded CSV file into a DataFrame
        data = pd.read_csv(uploaded_file)
        st.success("Family data successfully loaded!")
        st.write("### 📋 Uploaded Family Data:")
        st.dataframe(data)

        # Family Tree Visualization
        st.write("### 🌟 Family Tree Visualization")
        if all(col in data.columns for col in ["ID", "Name", "ParentID"]):
            # Prepare data for Plotly tree chart
            data["ParentID"] = data["ParentID"].fillna("")  # Replace NaN with empty strings
            tree_fig = px.treemap(
                data,
                path=["ParentID", "Name"],  # Hierarchical path
                values=None,  # Size of boxes is uniform
                title="Family Tree",
                labels={"Name": "Relative"},
                color_discrete_sequence=px.colors.qualitative.Pastel  # Color scheme
            )
            tree_fig.update_traces(root_color="lightgray")  # Set root node color
            st.plotly_chart(tree_fig, use_container_width=True)
        else:
            st.error("The CSV file must have 'ID', 'Name', and 'ParentID' columns.")
    except Exception as e:
        st.error(f"Error loading the file: {e}")
else:
    st.write("**📂 Please upload a CSV file to explore the family tree.**")

# Search Functionality
st.write("### 🔎 Search for a Relative")
if not data.empty:  # Ensure 'data' is loaded before searching
    search_name = st.text_input("Enter a name to search:")
    if search_name:
        results = data[data["Name"].str.contains(search_name, case=False, na=False)]
        if not results.empty:
            st.write("### 🎯 Search Results:")
            st.dataframe(results)
        else:
            st.warning("No relatives found with that name.")
else:
    st.info("Search functionality will be available after uploading a file.")
