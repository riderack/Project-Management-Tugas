import streamlit as st

from logika import (calculate_statistics, create_task, find_task_by_id, filter_tasks,  next_task_id, sort_tasks, validated_task_data,)

st.set_page_config(page_title="Management Tugas", page_icon="🗂️", layout="wide")

st.title("🗂️ Management Tugas")
st.caption("Applikasi Web untuk management tugas yang mengatur Tugas prioritas tinggi, deadline tugas, dan progres kuliah Mahasiswa")
