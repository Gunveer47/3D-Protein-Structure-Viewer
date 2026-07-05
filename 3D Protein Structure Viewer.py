import streamlit as st
import py3Dmol
from stmol import showmol
st.title("Interactive 3D Protein Viewer🧬")
st.write("Enter any 4-character PDB ID to visualize its 3D structure")
st.sidebar.header("Visualization Settings")
pdb_id = st.sidebar.text_input("Enter PDB ID", value = "1A2C").upper()
style = st.sidebar.selectbox("Render Style", ["cartoon", "stick","sphere", "line"])
spin = st.sidebar.checkbox("Spin Molecule", value=False)

if pdb_id:
    try:
        viewer = py3Dmol.view(query=f"pdb:{pdb_id}")
        viewer.setStyle({style: {'color': 'spectrum'}})
        if spin:
            viewer.spin(True)
        else:
            viewer.spin(False)
        
        viewer.zoomTo()

        showmol(viewer, height=500, width=700)
        st.success(f"Successfully loaded PDB: {pdb_id}")

    except Exception as e:
        st.error("Could not fetch the PDB ID. Please check the ID and try again.")