import streamlit as st
from datetime import datetime

# ===========================================================
# 1. AUTHENTICATION SETUP (PLACE THIS AT THE VERY TOP)
# ===========================================================
# Replace with your real usernames and passwords:
VALID_USERS = {
    "hoss": "hoss25",
    "gild": "gild25"
}

# Simple session-based login check
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def show_login():
    """Displays a simple login form and sets logged_in to True if valid."""
    st.title("Restricted Access - Please Log In")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Log In"):
        if username in VALID_USERS and password == VALID_USERS[username]:
            st.session_state.logged_in = True
           
        else:
            st.error("Invalid username or password")

# If not logged in, show the login form and stop execution here
if not st.session_state.logged_in:
    show_login()
    st.stop()

# ===========================================================
# 2. MAIN WIZARD CODE (ONLY ACCESSIBLE IF LOGGED IN)
# ===========================================================

# ----------------------------
# Données statiques pour Départements et Communes
# ----------------------------
departements = [
    "Alibori", "Atakora", "Atlantique", "Borgou", "Collines", "Couffo",
    "Donga", "Littoral", "Mono", "Ouémé", "Plateau", "Zou"
]

communes = [
    # Alibori (6)
    "Banikoara", "Gogounou", "Kandi", "Karimama", "Malanville", "Ségbana",
    # Atakora (9)
    "Boukoumbé", "Cobly", "Kérou", "Kouandé", "Matéri", "Natitingou", "Pehonko", "Tanguiéta", "Toucountouna",
    # Atlantique (8)
    "Abomey-Calavi", "Allada", "Kpomassè", "Ouidah", "Sô-Ava", "Toffo", "Tori-Bossito", "Zè",
    # Borgou (8)
    "Bembèrèkè", "Kalalé", "N’Dali", "Nikki", "Parakou", "Pèrèrè", "Sinendé", "Tchaourou",
    # Collines (6)
    "Bantè", "Dassa-Zoumè", "Glazoué", "Ouèssè", "Savalou", "Savè",
    # Couffo (5)
    "Aplahoué", "Djakotomey", "Klouékanmè", "Lalo", "Toviklin",
    # Donga (5)
    "Bassila", "Copargo", "Ouaké", "Djougou", "Kouandé",
    # Littoral (1)
    "Cotonou",
    # Mono (6)
    "Athiémè", "Bopa", "Comè", "Grand-Popo", "Houéyogbé", "Lokossa",
    # Ouémé (9)
    "Adjarra", "Adjohoun", "Akpro-Missérété", "Avrankou", "Bonou", "Dangbo", "Porto-Novo", "Sèmè-Kpodji", "Aguégués",
    # Plateau (5)
    "Ifangni", "Adja-Ouèrè", "Kétou", "Pobè", "Sakété",
    # Zou (9)
    "Abomey", "Agbangnizoun", "Bohicon", "Covè", "Djidja", "Ouinhi", "Za-Kpota", "Zangnanado", "Zogbodomey"
]

# ----------------------------
# Simuler une banque d'anciennes épreuves (pour illustration)
# ----------------------------
old_exams = {
    2020: ["Math Bac 2020 - Sujet 1", "Math Bac 2020 - Sujet 2"],
    2021: ["Math Bac 2021 - Sujet 1", "Math Bac 2021 - Sujet 2"],
    2022: ["Math Bac 2022 - Sujet 1", "Math Bac 2022 - Sujet 2"],
    2023: ["Math Bac 2023 - Sujet 1", "Math Bac 2023 - Sujet 2"]
}

# ----------------------------
# Initialisation de l'état de session
# ----------------------------
if "step" not in st.session_state:
    st.session_state.step = 1
if "form_data" not in st.session_state:
    st.session_state.form_data = {}
if "pop_dept" not in st.session_state:
    st.session_state.pop_dept = {}
if "pop_commune" not in st.session_state:
    st.session_state.pop_commune = {}
if "exercise_details" not in st.session_state:
    st.session_state.exercise_details = {}

# ----------------------------
# Fonctions de navigation entre étapes
# ----------------------------
def next_step():
    st.session_state.step += 1

def prev_step():
    st.session_state.step -= 1

def save_data(key, value):
    st.session_state.form_data[key] = value

# ----------------------------
# Étape 1 : Informations générales
# ----------------------------
def step1():
    st.header("Étape 1 : Informations générales")
    st.write("Veuillez renseigner les informations générales concernant l'examen et l'établissement.")

    teacher_name = st.text_input("Nom de l’enseignant", st.session_state.form_data.get("teacher_name", ""), key="teacher_name")
    save_data("teacher_name", teacher_name)
    
    nom_ecole = st.text_input("Nom de l'école", st.session_state.form_data.get("nom_ecole", ""), key="nom_ecole")
    save_data("nom_ecole", nom_ecole)
    
    adresse = st.text_input("Adresse de l'école", st.session_state.form_data.get("adresse", ""), key="adresse")
    save_data("adresse", adresse)
    
    telephone = st.text_input("Téléphone", st.session_state.form_data.get("telephone", ""), key="telephone")
    save_data("telephone", telephone)
    
    fax = st.text_input("Fax", st.session_state.form_data.get("fax", ""), key="fax")
    save_data("fax", fax)
    
    boite_postale = st.text_input("Boîte postale", st.session_state.form_data.get("boite_postale", ""), key="boite_postale")
    save_data("boite_postale", boite_postale)
    
    st.markdown("---")
    
    exam_range = st.slider(
        "Sélectionnez la période pour consulter les anciennes épreuves",
        min_value=2000,
        max_value=datetime.today().year,
        value=(2020, 2022),
        key="exam_range_slider"
    )
    save_data("exam_range", exam_range)
    
    available_exams = []
    for year in range(exam_range[0], exam_range[1] + 1):
        if year in old_exams:
            for exam in old_exams[year]:
                available_exams.append(f"{year} - {exam}")
    if available_exams:
        st.subheader("Anciennes épreuves disponibles")
        selected_old_exams = st.multiselect(
            "Sélectionnez les épreuves à consulter ou télécharger",
            available_exams,
            default=st.session_state.form_data.get("selected_old_exams", []),
            key="old_exams"
        )
        save_data("selected_old_exams", selected_old_exams)
        for exam in selected_old_exams:
            st.download_button(
                label=f"Télécharger {exam}",
                data=f"Contenu simulé de {exam}",
                file_name=f"{exam}.txt",
                key=f"download_{exam}"
            )
    else:
        st.info("Aucune ancienne épreuve disponible pour la période sélectionnée.")
    
    st.markdown("---")
    
    selected_depts = st.multiselect(
        "Sélectionnez les Départements",
        departements,
        default=st.session_state.form_data.get("departements", []),
        key="departements"
    )
    save_data("departements", selected_depts)
    
    st.subheader("Population par Département")
    for dept in selected_depts:
        pop = st.number_input(
            f"Population pour {dept}",
            min_value=0,
            step=1000,
            value=st.session_state.pop_dept.get(dept, 0),
            key=f"pop_dept_{dept}"
        )
        st.session_state.pop_dept[dept] = pop
    save_data("pop_dept", st.session_state.pop_dept)
    
    selected_communes = st.multiselect(
        "Sélectionnez les Communes",
        communes,
        default=st.session_state.form_data.get("communes", []),
        key="communes"
    )
    save_data("communes", selected_communes)
    
    st.subheader("Population par Commune")
    for com in selected_communes:
        pop = st.number_input(
            f"Population pour {com}",
            min_value=0,
            step=1000,
            value=st.session_state.pop_commune.get(com, 0),
            key=f"pop_commune_{com}"
        )
        st.session_state.pop_commune[com] = pop
    save_data("pop_commune", st.session_state.pop_commune)
    
    date_examen = st.date_input(
        "Date de l'examen",
        st.session_state.form_data.get("date_examen", datetime.today()),
        key="date_examen"
    )
    duree_examen = st.number_input(
        "Durée de l'examen (en minutes)",
        min_value=30,
        max_value=300,
        value=240,
        step=10,
        key="duree_examen"
    )
    save_data("date_examen", date_examen)
    save_data("duree_examen", duree_examen)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Précédent", key="prev_step1"):
            prev_step()
    with col2:
        if st.button("Suivant", key="next_step1"):
            next_step()

# ----------------------------
# Étape 2 : Choix des thèmes mathématiques
# ----------------------------
def step2():
    st.header("Étape 2 : Choix des thèmes mathématiques")
    st.write("Sélectionnez **plusieurs thèmes** parmi les domaines du programme de mathématiques de Terminale.")
    
    topics = [
        "Analyse (fonctions, limites, dérivées)",
        "Algèbre (équations, inégalités, nombres complexes)",
        "Géométrie plane et dans l'espace",
        "Probabilités et statistiques",
        "Suites numériques"
    ]
    selected_topics = st.multiselect(
        "Choisissez les thèmes",
        topics,
        default=st.session_state.form_data.get("selected_topics", []),
        key="topics"
    )
    save_data("selected_topics", selected_topics)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Précédent", key="prev_step2"):
            prev_step()
    with col2:
        if st.button("Suivant", key="next_step2"):
            next_step()

# ----------------------------
# Étape 3 : Paramètres de l'examen
# ----------------------------
def step3():
    st.header("Étape 3 : Paramètres de l'examen")
    st.write("Définissez la structure de l'épreuve et ajoutez des informations spécifiques pour chaque exercice.")
    
    nb_exercices = st.number_input(
        "Nombre d'exercices dans l'examen",
        min_value=1,
        max_value=10,
        value=3,
        step=1,
        help="Généralement, les examens du Bac en mathématiques comportent 3 exercices.",
        key="nb_exercices"
    )
    save_data("nb_exercices", nb_exercices)
    
    exercice_type = st.radio(
        "Type d'exercices",
        options=["Problème long (étape par étape)", "Exercice court"],
        index=0,
        key="exercice_type"
    )
    save_data("exercice_type", exercice_type)
    
    st.markdown("### Informations complémentaires par exercice")
    # Branching: For each exercise, allow teacher to type details (text, formulas, etc.)
    for i in range(1, int(nb_exercices) + 1):
        detail = st.text_area(
            f"Informations complémentaires pour l'exercice {i}",
            st.session_state.exercise_details.get(f"ex{i}", ""),
            key=f"exercise_detail_{i}"
        )
        st.session_state.exercise_details[f"ex{i}"] = detail
    save_data("exercise_details", st.session_state.exercise_details)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Précédent", key="prev_step3"):
            prev_step()
    with col2:
        if st.button("Suivant", key="next_step3"):
            next_step()

# ----------------------------
# Étape 4 : Contexte d'actualité ou thématique
# ----------------------------
def step4():
    st.header("Étape 4 : Contexte d'actualité ou thématique")
    st.write(
        "Pour le contexte thématique, l’application vous guide en proposant des exemples de domaines historiques d'actualité en République du Bénin. "
        "Sélectionnez le ou les domaines qui vous intéressent pour fouiller les journaux appropriés, puis saisissez un contexte personnalisé ci-dessous."
    )
    
    example_domains = st.multiselect(
        "Sélectionnez un ou plusieurs domaines historiques d'actualité",
        options=[
            "Réformes éducatives et politiques",
            "Événements économiques ou sociaux",
            "Actualités culturelles et sportives",
            "Développements environnementaux",
            "Innovations technologiques"
        ],
        default=st.session_state.form_data.get("example_domains", []),
        key="example_domains"
    )
    save_data("example_domains", example_domains)
    
    actualite = st.text_area(
        "Contexte d'actualité ou thématique personnalisé",
        st.session_state.form_data.get("actualite", ""),
        help="Ces informations orienteront la structure et le contenu des épreuves générées.",
        key="actualite"
    )
    save_data("actualite", actualite)
    
    periode = st.selectbox(
        "Période d'actualité",
        options=["6 derniers mois", "1 an", "Plusieurs années"],
        index=0,
        key="periode"
    )
    save_data("periode", periode)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Précédent", key="prev_step4"):
            prev_step()
    with col2:
        if st.button("Suivant", key="next_step4"):
            next_step()

# ----------------------------
# Étape 5 : Prévisualisation et confirmation
# ----------------------------
def step5():
    st.header("Étape 5 : Prévisualisation et confirmation")
    st.write("Vérifiez et confirmez les paramètres de l'examen généré.")
    
    st.subheader("Récapitulatif des informations fournies")
    st.write("**Nom de l’enseignant :**", st.session_state.form_data.get("teacher_name", ""))
    st.write("**Nom de l'école :**", st.session_state.form_data.get("nom_ecole", ""))
    st.write("**Adresse :**", st.session_state.form_data.get("adresse", ""))
    st.write("**Téléphone :**", st.session_state.form_data.get("telephone", ""))
    st.write("**Fax :**", st.session_state.form_data.get("fax", ""))
    st.write("**Boîte postale :**", st.session_state.form_data.get("boite_postale", ""))
    st.write("**Période des anciennes épreuves :**", st.session_state.form_data.get("exam_range", ""))
    st.write("**Anciennes épreuves sélectionnées :**", st.session_state.form_data.get("selected_old_exams", []))
    st.write("**Départements sélectionnés :**", st.session_state.form_data.get("departements", []))
    st.write("**Population par Département :**", st.session_state.form_data.get("pop_dept", {}))
    st.write("**Communes sélectionnées :**", st.session_state.form_data.get("communes", []))
    st.write("**Population par Commune :**", st.session_state.form_data.get("pop_commune", {}))
    st.write("**Date de l'examen :**", st.session_state.form_data.get("date_examen", ""))
    st.write("**Durée (minutes) :**", st.session_state.form_data.get("duree_examen", ""))
    st.write("**Thèmes sélectionnés :**", st.session_state.form_data.get("selected_topics", []))
    st.write("**Nombre d'exercices :**", st.session_state.form_data.get("nb_exercices", ""))
    st.write("**Type d'exercice :**", st.session_state.form_data.get("exercice_type", ""))
    st.write("**Informations complémentaires par exercice :**", st.session_state.form_data.get("exercise_details", {}))
    st.write("**Domaines historiques d'actualité sélectionnés :**", st.session_state.form_data.get("example_domains", []))
    st.write("**Contexte personnalisé :**", st.session_state.form_data.get("actualite", ""))
    st.write("**Période d'actualité :**", st.session_state.form_data.get("periode", ""))
    
    st.markdown("---")
    st.write("Ces paramètres seront utilisés pour générer l'examen. De plus, toutes ou partie des anciennes épreuves depuis la période indiquée seront accessibles pour consultation.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Précédent", key="prev_step5"):
            prev_step()
    with col2:
        if st.button("Générer l'examen", key="next_step5"):
            st.success("L'examen a été généré avec succès !")
            st.write("**(Ici, le code de génération de l'examen serait exécuté.)**")
            st.write("Examen généré avec les paramètres ci-dessus.")

# ----------------------------
# Rendu principal en fonction de l'étape courante
# ----------------------------
st.sidebar.title("Assistant pour Générer des Epreuves de Mathématiques en Classes de Terminale D & C, Bénin")
steps = {
    1: "Informations générales",
    2: "Choix des thèmes",
    3: "Paramètres de l'examen",
    4: "Contexte d'actualité",
    5: "Prévisualisation"
}
st.sidebar.write("**Étapes du wizard :**")
for i in range(1, 6):
    if i == st.session_state.step:
        st.sidebar.markdown(f"**{i}. {steps[i]}**")
    else:
        st.sidebar.write(f"{i}. {steps[i]}")

if st.session_state.step == 1:
    step1()
elif st.session_state.step == 2:
    step2()
elif st.session_state.step == 3:
    step3()
elif st.session_state.step == 4:
    step4()
elif st.session_state.step == 5:
    step5()

# ----------------------------
# Permanent Chat Box (Fixed at the bottom)
# ----------------------------
chat_css = """
<style>
.fixed-chat {
    position: fixed;
    bottom: 0;
    left: 60%;
    transform: translateX(-50%);
    width: 60%;
    background: #f8f9fa;
    padding: 15px;
    border-top: 1px solid #ccc;
    z-index: 1000;
}
.fixed-chat .chat-row {
    display: flex;
    align-items: flex-start;
}
.fixed-chat textarea {
    width: 80%;
    height: 50px;
    margin-right: 10px;
    box-sizing: border-box;
}
.fixed-chat button {
    height: 50px;
    box-sizing: border-box;
}
</style>
"""
st.markdown(chat_css, unsafe_allow_html=True)

chat_html = """
<div class="fixed-chat">
    <label for="chat_box">Vos commentaires ou détails supplémentaires (affectant chaque section) :</label>
    <div class="chat-row">
        <textarea id="chat_box" name="chat_box"></textarea>
        <button onclick="window.dispatchEvent(new CustomEvent('sendChat'))">Envoyer message</button>
    </div>
</div>
"""
st.markdown(chat_html, unsafe_allow_html=True)

st.text("La boîte de dialogue permanente est fixée en bas de la page.")
