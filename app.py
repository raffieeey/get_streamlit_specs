import psutil
import streamlit as st

# Get CPU information
cpu_percent = psutil.cpu_percent()
cpu_cores = psutil.cpu_count(logical=False)

# Get memory information
mem = psutil.virtual_memory()
total_memory = mem.total
available_memory = mem.available
used_memory = mem.used
memory_percent = mem.percent

# Get SSD/HDD information
disk = psutil.disk_usage('/')
total_disk_space = disk.total
used_disk_space = disk.used
free_disk_space = disk.free
disk_space_percent = disk.percent

# Display the system information in Streamlit
st.write("CPU usage:", cpu_percent, "%")
st.write("CPU cores:", cpu_cores)
st.write("Total memory:", total_memory // (1024 ** 3), "GB")
st.write("Available memory:", available_memory // (1024 ** 3), "GB")
st.write("Used memory:", used_memory // (1024 ** 3), "GB")
st.write("Memory usage:", memory_percent, "%")
st.write("Total disk space:", total_disk_space // (1024 ** 3), "GB")
st.write("Used disk space:", used_disk_space // (1024 ** 3), "GB")
st.write("Free disk space:", free_disk_space // (1024 ** 3), "GB")
st.write("Disk usage:", disk_space_percent, "%")
