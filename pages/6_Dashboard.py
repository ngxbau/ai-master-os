import streamlit as st
import pandas as pd
import os
import shutil
from datetime import datetime

st.set_page_config(
    page_title="AI Master Control Center Level 50",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI MASTER CONTROL CENTER — CẤP ĐỘ 50")
st.caption("Trung tâm điều khiển AI • Database • Backup • Export • System Health")

if not os.path.exists("data"):
    os.makedirs("data")

if not os.path.exists("backups"):
    os.makedirs("backups")

csv_path = "data/projects.csv"

def load_data():
    if os.path.exists(csv_path):
        return pd.read_csv(csv_path)
    return pd.DataFrame(columns=["Time", "Project", "Type", "Prompt"])

def save_data(df):
    df.to_csv(csv_path, index=False)

def create_backup():
    if os.path.exists(csv_path):
        backup_name = f"backup_level50_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        backup_path = os.path.join("backups", backup_name)
        shutil.copy(csv_path, backup_path)
        return backup_path
    return None

df = load_data()

st.subheader("📊 MASTER DASHBOARD")

backup_files = [
    f for f in os.listdir("backups")
    if f.endswith(".csv")
] if os.path.exists("backups") else []

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("📁 Projects", len(df))
c2.metric("📂 Types", df["Type"].nunique() if len(df) > 0 and "Type" in df.columns else 0)
c3.metric("🛡️ Backups", len(backup_files))
c4.metric("💾 Database", "ONLINE" if os.path.exists(csv_path) else "EMPTY")
c5.metric("🚀 Level", "50")

st.markdown("---")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💾 Save",
    "🔎 Search",
    "🛡️ Backup",
    "📥 Export",
    "🧠 System Health"
])

with tab1:
    st.subheader("💾 Save New Project")

    project_name = st.text_input("Tên project")
    project_type = st.selectbox(
        "Loại project",
        ["AI Video", "Movie OS", "Brand", "Business", "Automation", "Knowledge", "Template"]
    )
    prompt = st.text_area("Prompt / Ý tưởng")

    if st.button("💾 Save Project + Backup"):
        if project_name.strip() == "":
            st.error("Sếp nhập tên project trước nhé.")
        else:
            new_row = pd.DataFrame({
                "Time": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                "Project": [project_name],
                "Type": [project_type],
                "Prompt": [prompt]
            })

            df_new = pd.concat([load_data(), new_row], ignore_index=True)
            save_data(df_new)
            backup_path = create_backup()

            st.success("✅ Đã lưu project và backup!")
            if backup_path:
                st.info(f"🛡️ Backup: {backup_path}")

with tab2:
    st.subheader("🔎 Search Database")

    if len(df) > 0:
        keyword = st.text_input("Tìm kiếm")

        type_filter = st.selectbox(
            "Lọc theo loại",
            ["Tất cả"] + sorted(df["Type"].dropna().astype(str).unique().tolist())
        )

        filtered = df.copy()

        if keyword.strip():
            filtered = filtered[
                filtered.astype(str).apply(
                    lambda row: row.str.contains(keyword, case=False, na=False).any(),
                    axis=1
                )
            ]

        if type_filter != "Tất cả":
            filtered = filtered[filtered["Type"].astype(str) == type_filter]

        st.write(f"✅ Tìm thấy {len(filtered)} kết quả")
        st.dataframe(filtered, use_container_width=True)

    else:
        st.info("Database đang trống.")

with tab3:
    st.subheader("🛡️ Backup Center")

    if st.button("🛡️ Create Backup Now"):
        backup_path = create_backup()
        if backup_path:
            st.success(f"✅ Đã tạo backup: {backup_path}")
        else:
            st.warning("Chưa có database để backup.")

    if backup_files:
        backup_files = sorted(backup_files, reverse=True)

        selected_backup = st.selectbox("Chọn backup", backup_files)
        backup_path = os.path.join("backups", selected_backup)

        with open(backup_path, "rb") as f:
            st.download_button(
                "📥 Download Selected Backup",
                f,
                file_name=selected_backup,
                mime="text/csv"
            )

        if st.button("♻️ Restore Selected Backup"):
            shutil.copy(backup_path, csv_path)
            st.success("✅ Đã khôi phục backup. Nhấn F5 để cập nhật.")
    else:
        st.info("Chưa có backup nào.")

with tab4:
    st.subheader("📥 Export Center")

    if len(df) > 0:
        export_text = f"""
AI MASTER CONTROL CENTER — LEVEL 50

Generated:
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Total projects:
{len(df)}

Project types:
{df["Type"].nunique() if "Type" in df.columns else 0}

Latest projects:
{df.tail(5).to_string(index=False)}
"""

        st.download_button(
            "📥 Download Report TXT",
            data=export_text,
            file_name="ai_master_control_report_level50.txt",
            mime="text/plain"
        )

        with open(csv_path, "rb") as f:
            st.download_button(
                "📥 Download Database CSV",
                f,
                file_name="ai_master_database_level50.csv",
                mime="text/csv"
            )
    else:
        st.info("Chưa có dữ liệu để export.")

with tab5:
    st.subheader("🧠 System Health")

    health_data = pd.DataFrame({
        "System": [
            "Project Database",
            "Search Engine",
            "Backup System",
            "Export Center",
            "Dashboard",
            "AI Master OS"
        ],
        "Status": [
            "ONLINE" if os.path.exists(csv_path) else "EMPTY",
            "READY",
            "ONLINE",
            "READY",
            "ACTIVE",
            "LEVEL 50"
        ]
    })

    st.dataframe(health_data, use_container_width=True)

    st.markdown("""
### ✅ Level 50 Summary

AI Master Control Center đã có:
- Lưu project
- Tìm kiếm
- Backup
- Restore
- Export
- System Health
- Dashboard tổng hợp
""")