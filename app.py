import streamlit as st
import pandas as pd

# Configuração da Página
st.set_page_config(
    page_title="Prof. Dr(a). [Seu Nome] | Fisioterapia & Docência",
    page_icon="🩺",
    layout="wide"
)

# Estilização visual para os espaços de imagem
st.markdown("""
    <style>
    .placeholder-img { 
        background-color: #f0f2f6; 
        color: #555; 
        padding: 40px; 
        text-align: center; 
        border: 2px dashed #b0c4de; 
        border-radius: 8px;
        margin-bottom: 15px; 
        font-weight: 500;
    }
    .main-header { font-size: 2.5rem; color: #004a80; }
    </style>
""", unsafe_allow_html=True)

# Função para carregar os dados da sua planilha do Google Sheets
@st.cache_data(ttl=600) # Atualiza os dados a cada 10 minutos
def carregar_dados_planilha():
    # Substitua o link abaixo pelo link CSV público da sua planilha do Google Sheets
    # Dica: No Google Planilhas, pegue o link de compartilhamento e ajuste o final para /export?format=csv
    url_csv = "COLE_O_LINK_CSV_DA_ SUA_PLANILHA_AQUI"
    try:
        df = pd.read_csv(url_csv)
        return df
    except:
        return pd.DataFrame(columns=["Secao", "Titulo", "Descricao", "Link"])

df_site = carregar_dados_planilha()

# ==========================================
# 1. FOTO DE CAPA DO SITE
# ==========================================
st.markdown('<div class="placeholder-img">🖼️ Coloque sua foto de capa aqui (Sugestão: 1200x300px)</div>', unsafe_allow_html=True)

st.markdown('<h1 class="main-header">Prof. Dr(a). [Seu Nome Completo]</h1>', unsafe_allow_html=True)
st.markdown("### Fisioterapeuta | Coordenação do Curso de Fisioterapia — PUC Goiás[cite: 1]")
st.markdown("---")

# Abas de Navegação
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📂 Sobre & Lattes", 
    "💼 Serviços", 
    "🎓 Cursos & Palestras", 
    "🔍 Validar Certificado", 
    "📚 E-books"
])

# ==========================================
# ABA 1: SOBRE & LATTES (Puxando dados da planilha se houver)
# ==========================================
with tab1:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown('<div class="placeholder-img" style="padding: 60px 10px;">📷 Foto de Perfil</div>', unsafe_allow_html=True)
        st.caption("Fisioterapeuta - PUC Goiás[cite: 1]")
        
    with col2:
        st.header("Sobre Mim")
        
        # Filtra dados da seção 'sobre' na planilha, se preenchidos
        dados_sobre = df_site[df_site['Secao'] == 'sobre'] if not df_site.empty else pd.DataFrame()
        
        if not dados_sobre.empty:
            for _, row in dados_sobre.iterrows():
                st.subheader(row['Titulo'])
                st.write(row['Descricao'])
                if pd.notna(row['Link']) and row['Link'] != "":
                    st.link_button(f"🔗 Acessar Link Oficial", row['Link'])
        else:
            # Texto padrão caso a planilha ainda esteja vazia
            st.write("""
            Atuação dedicada à reabilitação funcional, pesquisa científica e gestão acadêmica 
            na Pontifícia Universidade Católica de Goiás (PUC Goiás). Foco na coordenação pedagógica, 
            desenvolvimento motor e práticas baseadas em evidências[cite: 1].
            """)
        
        # Pilares institucionais fixos ou dinâmicos baseados no seu perfil
        c1, c2, c3 = st.columns(3)
        c1.metric("Docência", "PUC Goiás[cite: 1]")
        c2.metric("Coordenação", "Fisioterapia[cite: 1]")
        c3.metric("Atuação", "Clínica[cite: 1]")
        
        st.markdown("---")
        st.link_button("📄 Ver Currículo Lattes Completo", "https://lattes.cnpq.br/SEU_ID_LATTES")

# ==========================================
# ABA 2: SERVIÇOS
# ==========================================
with tab2:
    st.header("Contratação de Serviços")
    st.write("Agende avaliações especializadas, mentorias clínicas ou consultorias na área de Fisioterapia.")
    st.markdown('<div class="placeholder-img">🖼️ Coloque a imagem ilustrativa dos serviços aqui</div>', unsafe_allow_html=True)
    
    with st.form("form_servico"):
        st.subheader("Formulário de Solicitação")
        nome_servico = st.text_input("Seu Nome Completo")
        email_servico = st.text_input("Seu E-mail")
        tel_servico = st.text_input("Telefone / WhatsApp")
        tipo_atendimento = st.selectbox("Selecione o Serviço", ["Fisioterapia Especializada", "Consultoria Científica", "Mentoria Acadêmica", "Outros"])
        mensagem_servico = st.text_area("Descreva sua necessidade")
        
        if st.form_submit_button("Enviar Solicitação de Contato"):
            if nome_servico and email_servico:
                st.success("Solicitação enviada com sucesso! Entraremos em contato em breve.")
            else:
                st.warning("Por favor, preencha pelo menos o seu nome e e-mail.")

# ==========================================
# ABA 3: CURSOS E PALESTRAS
# ==========================================
with tab3:
    st.header("Cursos, Capacitações e Palestras")
    st.write("Confira a agenda de eventos presenciais na PUC Goiás e online.")
    st.markdown('<div class="placeholder-img">🖼️ Coloque a imagem do próximo evento ou banner aqui</div>', unsafe_allow_html=True)
    
    # Exibindo cursos dinâmicos da planilha se houver
    dados_cursos = df_site[df_site['Secao'] == 'cursos'] if not df_site.empty else pd.DataFrame()
    if not dados_cursos.empty:
        for _, row in dados_cursos.iterrows():
            with st.container(border=True):
                st.subheader(row['Titulo'])
                st.write(row['Descricao'])
                if pd.notna(row['Link']):
                    st.link_button("Inscrever-se no Evento", row['Link'])
    else:
        st.info("Nenhum curso cadastrado no momento. Atualize sua planilha para adicionar eventos.")

# ==========================================
# ABA 4: VERIFICAÇÃO DE CERTIFICADOS
# ==========================================
with tab4:
    st.header("Verificação de Autenticidade de Certificados")
    st.write("Digite o código alfanumérico impresso no seu certificado para comprovar sua validade na PUC Goiás.")
    st.markdown('<div class="placeholder-img">🖼️ Coloque uma imagem ilustrativa de validação/certificados aqui</div>', unsafe_allow_html=True)
    
    codigo_input = st.text_input("Código do Certificado (Ex: PUC-FISIO-2026-001)").strip()
    
    if st.button("Verificar Autenticidade"):
        base_certificados = {
            "PUC-FISIO-001": {"valido": True, "curso": "Atualidades em Fisioterapia", "data": "2026", "carga": "20h"}
        }
        if codigo_input in base_certificados:
            cert = base_certificados[codigo_input]
            st.success("✅ **Certificado Válido e Autêntico!**")
            st.write(f"- **Curso/Evento:** {cert['curso']}")
            st.write(f"- **Instituição:** PUC Goiás")
        elif codigo_input == "":
            st.warning("⚠️ Insira um código no campo acima.")
        else:
            st.error("❌ **Certificado não encontrado.**")

# ==========================================
# ABA 5: E-BOOKS E PUBLICAÇÕES
# ==========================================
with tab5:
    st.header("E-books e Materiais Acadêmicos")
    st.write("Materiais didáticos, guias práticos e e-books publicados para suporte acadêmico e profissional.")
    
    dados_ebooks = df_site[df_site['Secao'] == 'ebooks'] if not df_site.empty else pd.DataFrame()
    
    if not dados_ebooks.empty:
        cols = st.columns(2)
        idx = 0
        for _, row in dados_ebooks.iterrows():
            with cols[idx % 2]:
                st.markdown('<div class="placeholder-img" style="padding: 30px;">📖 Capa do E-book</div>', unsafe_allow_html=True)
                st.subheader(row['Titulo'])
                st.write(row['Descricao'])
                if pd.notna(row['Link']):
                    st.link_button("📥 Baixar / Acessar E-book", row['Link'])
            idx += 1
    else:
        st.write("Nenhum e-book cadastrado na planilha no momento.")

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>© 2026 Prof. Dr(a). [Seu Nome] • Coordenação de Fisioterapia PUC Goiás[cite: 1] • Todos os direitos reservados.</p>", 
    unsafe_allow_html=True
)
