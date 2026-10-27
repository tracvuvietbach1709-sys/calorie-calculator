import streamlit as st

st.set_page_config(page_title="FitLife Calorie Deficit Calculator", page_icon="🔥", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-color: #f0fdf4;
        color: #1f2937;
    }
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #059669 0%, #10b981 100%);
        color: white;
        font-weight: bold;
        border-radius: 8px;
        width: 100%;
        padding: 0.6rem;
        border: none;
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #047857 0%, #059669 100%);
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'input'

if st.session_state.page == 'input':
    st.markdown("<p align='center'><span style='background-color: #d1fae5; color: #065f46; padding: 6px 16px; border-radius: 20px; font-weight: 600; font-size: 14px;'>🔥 FitLife Calorie Deficit Calculator</span></p>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #111827; font-size: 2.2rem;'>Tính Thâm Hụt Calo & Thiết Lập Thực Đơn</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #4b5563; font-size: 1.05rem;'>Xác định chính xác lượng calo cần nạp để giảm cân an toàn, khoa học và hiệu quả</p>", unsafe_allow_html=True)
    
    with st.form("core_form"):
        col1, col2 = st.columns(2)
        with col1:
            weight = st.number_input("Cân nặng (kg)", min_value=30.0, max_value=200.0, value=73.0, step=0.5)
            age = st.number_input("Tuổi", min_value=10, max_value=100, value=20, step=1)
        with col2:
            height = st.number_input("Chiều cao (cm)", min_value=100.0, max_value=220.0, value=170.0, step=1.0)
            gender = st.selectbox("Giới tính", ["Nam", "Nữ"])

        activity_level = st.selectbox(
            "Tần suất tập luyện",
            [
                "Ít vận động (Ít hoặc không tập thể thao, ngồi nhiều)",
                "Vừa phải (Tập gym/thể thao 3-4 buổi/tuần)",
                "Năng động (Tập luyện nặng 5-6 buổi/tuần)"
            ]
        )

        weight_loss_speed = st.selectbox(
            "Mức độ giảm cân mong muốn",
            [
                "Giảm chậm, bền vững (~0.3 kg/tuần - Thâm hụt 300 kcal)",
                "Giảm tiêu chuẩn (~0.5 kg/tuần - Thâm hụt 500 kcal)",
                "Giảm nhanh hơn (~0.7 kg/tuần - Thâm hụt 700 kcal)"
            ]
        )

        submitted = st.form_submit_button(label="XEM KẾT QUẢ & THỰC ĐƠN")

        if submitted:
            st.session_state.weight = weight
            st.session_state.height = height
            st.session_state.age = age
            st.session_state.gender = gender
            st.session_state.activity_level = activity_level
            st.session_state.weight_loss_speed = weight_loss_speed
            st.session_state.page = 'result'
            st.rerun()

elif st.session_state.page == 'result':
    st.markdown("<p align='center'><span style='background-color: #d1fae5; color: #065f46; padding: 6px 16px; border-radius: 20px; font-weight: 600; font-size: 14px;'>🔥 FitLife Calorie Deficit Calculator</span></p>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #111827; font-size: 2.2rem;'>Tính Thâm Hụt Calo & Thiết Lập Thực Đơn</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #4b5563; font-size: 1.05rem;'>Xác định chính xác lượng calo cần nạp để giảm cân an toàn, khoa học và hiệu quả</p>", unsafe_allow_html=True)

    w = st.session_state.weight
    h = st.session_state.height
    a = st.session_state.age
    g = st.session_state.gender
    act = st.session_state.activity_level
    spd = st.session_state.weight_loss_speed

    if g == "Nam":
        bmr = (10 * w) + (6.25 * h) - (5 * a) + 5
    else:
        bmr = (10 * w) + (6.25 * h) - (5 * a) - 161

    if "Ít vận động" in act:
        tdee = bmr * 1.2
    elif "Vừa phải" in act:
        tdee = bmr * 1.55
    else:
        tdee = bmr * 1.725

    if "chậm" in spd:
        dfc = 300
        loss_kg = 0.3
    elif "tiêu chuẩn" in spd:
        dfc = 500
        loss_kg = 0.45
    else:
        dfc = 700
        loss_kg = 0.65

    target = max(1200, tdee - dfc)
    
    protein_g = w * 2.0
    protein_kcal = protein_g * 4
    
    fat_g = w * 0.8
    fat_kcal = fat_g * 9
    
    carb_kcal = target - (protein_kcal + fat_kcal)
    carb_g = max(50, carb_kcal / 4)
    carb_kcal = carb_g * 4

    st.markdown(f"""
        <div style='background: linear-gradient(135deg, #059669 0%, #0284c7 100%); padding: 30px; border-radius: 16px; color: white; text-align: center; margin: 20px 0;'>
            <div style='font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; font-weight: bold; opacity: 0.9;'>MỤC TIÊU CALO HÀNG NGÀY CỦA BẠN</div>
            <div style='font-size: 3.2rem; font-weight: bold; margin: 10px 0;'>{int(target)} <span style='font-size: 1.5rem; font-weight: normal;'>kcal/ngày</span></div>
            <div style='font-size: 0.9rem; opacity: 0.9;'>Để đạt mục tiêu giảm cân an toàn mà không gây mất cơ hay mệt mỏi.</div>
        </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
            <div style='border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px; text-align: center; background-color: white;'>
                <div style='font-size: 0.75rem; color: #6b7280; font-weight: bold; text-transform: uppercase;'>BMR</div>
                <div style='font-size: 1.6rem; font-weight: bold; color: #111827; margin: 8px 0;'>{int(bmr)} kcal</div>
                <div style='font-size: 0.75rem; color: #9ca3af;'>Nghỉ ngơi hoàn toàn</div>
            </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
            <div style='border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px; text-align: center; background-color: white;'>
                <div style='font-size: 0.75rem; color: #6b7280; font-weight: bold; text-transform: uppercase;'>TDEE</div>
                <div style='font-size: 1.6rem; font-weight: bold; color: #111827; margin: 8px 0;'>{int(tdee)} kcal</div>
                <div style='font-size: 0.75rem; color: #9ca3af;'>Tiêu thụ kèm vận động</div>
            </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
            <div style='border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px; text-align: center; background-color: white;'>
                <div style='font-size: 0.75rem; color: #6b7280; font-weight: bold; text-transform: uppercase;'>DỰ ĐOÁN GIẢM</div>
                <div style='font-size: 1.5rem; font-weight: bold; color: #059669; margin: 8px 0;'>~{loss_kg} kg/tuần</div>
                <div style='font-size: 0.75rem; color: #9ca3af;'>~{round(loss_kg * 4.3, 1)} kg / tháng</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<h3 style='color: #065f46; font-size: 1.2rem; margin-top: 25px; margin-bottom: 15px;'>🌿 Phân Bổ Dưỡng Chất (Macros) Đề Xuất</h3>", unsafe_allow_html=True)
    
    mc1, mc2, mc3 = st.columns(3)
    with mc1:
        st.markdown(f"""
            <div style='background-color: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 12px; padding: 20px;'>
                <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;'>
                    <span style='font-weight: bold; color: #065f46;'>Protein</span>
                    <span style='background-color: #d1fae5; color: #065f46; padding: 2px 8px; border-radius: 10px; font-size: 0.75rem; font-weight: bold;'>30%</span>
                </div>
                <div style='font-size: 1.6rem; font-weight: bold; color: #111827;'>{int(protein_g)} g</div>
                <div style='font-size: 0.75rem; color: #059669; margin-top: 5px;'>{int(protein_kcal)} kcal</div>
            </div>
        """, unsafe_allow_html=True)
    with mc2:
        st.markdown(f"""
            <div style='background-color: #f0f9ff; border: 1px solid #bae6fd; border-radius: 12px; padding: 20px;'>
                <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;'>
                    <span style='font-weight: bold; color: #0369a1;'>Carbs</span>
                    <span style='background-color: #e0f2fe; color: #0369a1; padding: 2px 8px; border-radius: 10px; font-size: 0.75rem; font-weight: bold;'>45%</span>
                </div>
                <div style='font-size: 1.6rem; font-weight: bold; color: #111827;'>{int(carb_g)} g</div>
                <div style='font-size: 0.75rem; color: #0284c7; margin-top: 5px;'>{int(carb_kcal)} kcal</div>
            </div>
        """, unsafe_allow_html=True)
    with mc3:
        st.markdown(f"""
            <div style='background-color: #fffbeb; border: 1px solid #fde68a; border-radius: 12px; padding: 20px;'>
                <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;'>
                    <span style='font-weight: bold; color: #b45309;'>Fat</span>
                    <span style='background-color: #fef3c7; color: #b45309; padding: 2px 8px; border-radius: 10px; font-size: 0.75rem; font-weight: bold;'>25%</span>
                </div>
                <div style='font-size: 1.6rem; font-weight: bold; color: #111827;'>{int(fat_g)} g</div>
                <div style='font-size: 0.75rem; color: #d97706; margin-top: 5px;'>{int(fat_kcal)} kcal</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<h3 style='color: #065f46; font-size: 1.2rem; margin-top: 25px; margin-bottom: 10px;'>🥗 Gợi ý thực đơn ăn kiêng mẫu</h3>", unsafe_allow_html=True)
    st.markdown("""
    * **Bữa sáng:** 2 Trứng luộc / ốp la + 1 lát Bánh mì đen + 1 ly Cà phê đen hoặc trà xanh.
    * **Bữa trưa:** 150g ức gà áp chảo (hoặc thịt bò nạc) + 1 củ khoai lang lớn + Rau xanh luộc thoải mái.
    * **Bữa phụ chiều:** 1 hũ sữa chua Hy Lạp không đường hoặc một nhúm hạt dinh dưỡng.
    * **Bữa tối:** 150g cá hồi hoặc cá rô phi hấp/áp chảo + Nửa chén cơm gạo lứt + Salad rau củ.
    """)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⬅️ QUAY LẠI & ĐIỀU CHỈNH THÔNG SỐ"):
        st.session_state.page = 'input'
        st.rerun()