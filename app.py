import streamlit as st
import pandas as pd

st.set_page_config(page_title="肉鸭采食分析工具", layout="wide")
st.title("肉鸭采食行为 + 生产性能综合分析工具")
st.info("✅ Demo版本，部署测试。后续逐步增加统计、绘图功能")

upload_file = st.file_uploader("上传Excel小样数据", type=["xlsx"])
if upload_file is not None:
    df = pd.read_excel(upload_file)
    st.subheader("数据预览")
    st.dataframe(df)
