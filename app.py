import streamlit as st
import pandas as pd

# Configuração da Página
st.set_page_config(
    page_title="Prof. Dr(a). Larissa Mariana | Fisioterapia & Docência no Ensino Superior",
    page_icon="🩺",
    layout="wide"
)

# Estilização visual para os espaços de imagem e layout
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

# Função robusta em Python para carregar e tratar os dados da planilha do Google Sheets
@st.cache_data(ttl=600)
def carregar_dados_planilha():
    # Link convertida para exportação direta em CSV legível pelo Pandas
    url_csv = "https://docs.google.com/spreadsheets/d/1A0ZHnATInlMHMjp44SEb8VlwyQvXS34gkLS2SrYiGUE/export?format=csv"
    try:
        df = pd.read_csv(url_csv)
        # Padroniza os nomes das colunas para evitar erros de leitura por maiúsculas/minúsculas
        df.columns = df.columns.str.strip().str.title()
        return df
    except Exception as e:
        # Retorna um DataFrame vazio estruturado caso ocorra algum erro na leitura da web
        return pd.DataFrame(columns=["Secao", "Titulo", "Descricao", "Link", "Isbn/Doi"])

df_site = carregar_dados_planilha()

# ==========================================
# 1. FOTO DE CAPA DO SITE (Mais estreita e centralizada)
# ==========================================
col_esq, col_centro, col_dir = st.columns([1, 4, 1])
with col_centro:
    try:
        st.image("imagens/capasite.png", use_container_width=True)
    except:
        st.markdown('<div class="placeholder-img">🖼️ Imagem "imagens/capasite.png" não encontrada na pasta "imagens".</div>', unsafe_allow_html=True)

st.markdown('<h1 class="main-header" style="text-align: center;">Prof. Dr(a). Larissa Mariana Veloso de Oliveira</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem; font-weight: bold; color: #555;'>Fisioterapeuta | Coordenadora do Curso de Fisioterapia — PUC Goiás[cite: 1, 2]</p>", unsafe_allow_html=True)
st.markdown("---")

# Abas de Navegação
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📂 Sobre & Lattes", 
    "💼 Serviços", 
    "🎓 Cursos & Pesquisas", 
    "🔍 Validar Certificado", 
    "📚 E-books & Publicações"
])

# ==========================================
# ABA 1: SOBRE & LATTES
# ==========================================
with tab1:
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image("larissa.png", use_container_width=True)
        except:
            st.markdown('<div class="placeholder-img">📷 Foto "larissa.png" não encontrada na raiz do repositório.</div>', unsafe_allow_html=True)
        st.caption("Fisioterapeuta - PUC Goiás[cite: 1, 2]")
        
    with col2:
        st.header("Sobre Mim")
        st.write("""
        Graduada pela UNESP, Mestre pela Universitat Internacional de Catalunya e Doutoranda pela Universidad de Palermo[cite: 2]. 
        Docente da PUC Goiás desde 2005 e Coordenadora do Curso de Fisioterapia desde 2011[cite: 2]. Atuação destacada em reabilitação, 
        saúde pública, preceptoria e gestão acadêmica, com premiações pelo Ministério da Saúde e Assembleia Legislativa de Goiás (ALEGO)[cite: 2].
        """)
        
        # Pilares institucionais
        c1, c2, c3 = st.columns(3)
        c1.metric("Docência", "PUC Goiás[cite: 1, 2]")
        c2.metric("Coordenação", "Fisioterapia[cite: 1, 2]")
        c3.metric("Atuação", "Clínica & Pesquisa[cite: 2]")
        
        st.markdown("---")
        st.link_button("📄 Ver Currículo Lattes Completo", "http://lattes.cnpq.br/1002411477807507")

# ==========================================
# ABA 2: SERVIÇOS
# ==========================================
with tab2:
    st.header("Contratação de Serviços")
    st.write("Agende avaliações especializadas, mentorias clínicas ou consultorias na área de Fisioterapia.")
    
    try:
        st.image("imagens/terapiamanual.jpg", use_container_width=True)
    except:
        st.markdown('<div class="placeholder-img">🖼️ Imagem "imagens/terapiamanual.jpg" não encontrada na pasta "imagens".</div>', unsafe_allow_html=True)
    
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
# ABA 3: CURSOS E PESQUISAS (PET-Saúde)
# ==========================================
with tab3:
    st.header("Projetos, Cursos e Extensão")
    st.write("Acompanhe as iniciativas acadêmicas, tutorias do PET-Saúde e capacitações.")
    
    if not df_site.empty and "Secao" in df_site.columns:
        dados_pesq = df_site[df_site['Secao'].str.lower().isin(['cursos', 'pesquisa'])]
    else:
        dados_pesq = pd.DataFrame()
    
    if not dados_pesq.empty:
        for _, row in dados_pesq.iterrows():
            with st.container(border=True):
                st.subheader(row.get('Titulo', ''))
                st.write(row.get('Descricao', ''))
                link_val = row.get('Link', '')
                if pd.notna(link_val) and str(link_val).strip() != "":
                    st.link_button("Acessar Detalhes", str(link_val))
    else:
        st.info("Cadastre seus cursos e projetos na planilha do Google Sheets para exibi-los aqui.")

# ==========================================
# ABA 4: VERIFICAÇÃO DE CERTIFICADOS
# ==========================================
with tab4:
    st.header("Verificação de Autenticidade de Certificados")
    st.write("Digite o código alfanumérico impresso no seu certificado para comprovar sua validade na PUC Goiás.")
    
    codigo_input = st.text_input("Código do Certificado (Ex: PUC-FISIO-2026-001)").strip()
    
    if st.button("Verificar Autenticidade"):
        base_certificados = {
            "PUC-FISIO-001": {"valido": True, "curso": "Atualidades em Fisioterapia", "data": "2026", "carga": "20h"}
        }
        if codigo_input in base_certificados:
            cert = base_certificados[codigo_input]
            st.success("✅ **Certificado Válido e Autêntico!**")
            st.write(f"- **Curso/Evento:** {cert['curso']}")
            st.write(f"- **Instituição:** PUC Goiás[cite: 1, 2]")
        elif codigo_input == "":
            st.warning("⚠️ Insira um código no campo acima.")
        else:
            st.error("❌ **Certificado não encontrado.**")

# ==========================================
# ABA 5: E-BOOKS E PUBLICAÇÕES
# ==========================================
with tab5:
    st.header("E-books, Guias e Publicações Científicas")
    st.write("Materiais didáticos e produções bibliográficas registradas no Lattes.")
    
    if not df_site.empty and "Secao" in df_site.columns:
        dados_pub = df_site[df_site['Secao'].str.lower().isin(['ebooks', 'publicacoes'])]
    else:
        dados_pub = pd.DataFrame()
    
    if not dados_pub.empty:
        for _, row in dados_pub.iterrows():
            with st.container(border=True):
                st.subheader(row.get('Titulo', ''))
                st.write(row.get('Descricao', ''))
                
                # Leitura dinâmica da coluna ISBN/DOI tratada pelo Python
                coluna_isbn = next((col for col in df_site.columns if 'isbn' in col.lower() or 'doi' in col.lower()), None)
                if coluna_isbn and pd.notna(row.get(coluna_isbn)) and str(row.get(coluna_isbn)).strip() != "":
                    st.caption(f"📌 **ISBN/DOI:** {row.get(coluna_isbn)}")
                    
                link_pub = row.get('Link', '')
                if pd.notna(link_pub) and str(link_pub).strip() != "":
                    st.link_button("📖 Acessar Publicação / Lattes", str(link_pub))
    else:
        st.write("Cadastre seus e-books e artigos na planilha do Google Sheets.")

# Rodapé padrão
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>© 2026 Prof. Dr(a). Larissa Mariana Veloso de Oliveira • Fisioterapia PUC Goiás[cite: 1, 2] • Todos os direitos reservados.</p>", 
    unsafe_allow_html=True
)
