import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Expresso Churn Prediction", layout="centered")

st.title("📊 Expresso Churn Prediction App")
st.write(
    "Cette application permet de prédire si un client Expresso "
    "risque de se désabonner à partir de variables numériques."
)

# Charger le modèle
try:
    model = joblib.load("model/expresso_churn_model.pkl")
except Exception as e:
    st.error(f"Erreur lors du chargement du modèle : {e}")
    st.stop()

st.subheader("🔢 Informations du client")

# Champs utilisateur (principaux)
montant = st.number_input("Montant des recharges", min_value=0.0, value=3000.0)
frequence_rech = st.number_input("Fréquence de recharge", min_value=0.0, value=7.0)
revenue = st.number_input("Revenue", min_value=0.0, value=3000.0)
arpu = st.number_input("ARPU Segment", min_value=0.0, value=1000.0)
frequence = st.number_input("Fréquence d'utilisation", min_value=0.0, value=9.0)
data_volume = st.number_input("Volume de données", min_value=0.0, value=257.0)

# Champs secondaires (valeurs réalistes par défaut)
on_net = st.number_input("ON NET", min_value=0.0, value=27.0)
orange = st.number_input("ORANGE", min_value=0.0, value=29.0)
tigo = st.number_input("TIGO", min_value=0.0, value=6.0)
zone1 = st.number_input("ZONE1", min_value=0.0, value=1.0)
zone2 = st.number_input("ZONE2", min_value=0.0, value=2.0)
regularity = st.number_input("Regularity", min_value=0, value=24)
freq_top_pack = st.number_input("Freq Top Pack", min_value=0.0, value=5.0)

if st.button("🔮 Prédire le churn"):
    input_data = pd.DataFrame([{
        "MONTANT": montant,
        "FREQUENCE_RECH": frequence_rech,
        "REVENUE": revenue,
        "ARPU_SEGMENT": arpu,
        "FREQUENCE": frequence,
        "DATA_VOLUME": data_volume,
        "ON_NET": on_net,
        "ORANGE": orange,
        "TIGO": tigo,
        "ZONE1": zone1,
        "ZONE2": zone2,
        "REGULARITY": regularity,
        "FREQ_TOP_PACK": freq_top_pack
    }])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("❌ Le client risque de se désabonner")
    else:
        st.success("✅ Le client ne risque pas de se désabonner")
