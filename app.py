import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Prof. Dr(a). [Seu Nome] | Fisioterapia & Docência",
    page_icon="🩺",
    layout="wide"
)

# Estilização visual para destacar os espaços das imagens
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

# ==========================================
# 1. FOTO DE CAPA DO SITE
# ==========================================
# Para substituir pela imagem real, troque o bloco abaixo por: 
# st.image("imagens/capa.jpg", use_container_width=True)
st.markdown('<div class="placeholder-img">🖼️ Coloque sua foto de capa aqui (Sugestão: 1200x300px)</div>', unsafe_allow_html=True)

# Título Principal
st.markdown('<h1 class="main-header">Prof. Dr(a). [Seu Nome Completo]</h1>', unsafe_allow_html=True)
st.markdown("### Fisioterapeuta | Docente e Pesquisador(a) na PUC Goiás")
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
# ABA 1: SOBRE & LATTES
# ==========================================
with tab1:
    col1, col2 = st.columns([1, 2])
    with col1:
        # Para substituir a foto de perfil: st.image("imagens/perfil.jpg", use_container_width=True)
        st.markdown('<div class="placeholder-img" style="padding: 60px 10px;">📷 Coloque sua foto de perfil aqui</div>', unsafe_allow_html=True)
    with col2:
        st.header("Sobre Mim")
        st.write("""
        Atuação dedicada à reabilitação funcional, pesquisa científica e ensino superior na **Pontifícia Universidade Católica de Goiás (PUC Goiás)**. 
        Comprometido(a) com a formação acadêmica de excelência, desenvolvimento motor e práticas clínicas baseadas em evidências.
        """)
        st.markdown("### Currículo Acadêmico")
        st.write("Acesse todas as minhas publicações, orientações e histórico acadêmico completo na plataforma oficial.")
        st.link_button("🔗 Acessar Currículo Lattes", "https://lattes.cnpq.br/SEU_ID_LATTES")

# ==========================================
# ABA 2: SERVIÇOS
# ==========================================
with tab2:
    st.header("Contratação de Serviços")
    st.write("Agende avaliações especializadas, mentorias clínicas ou consultorias na área de Fisioterapia.")
    
    # Para substituir a imagem da aba: st.image("imagens/servicos.jpg", use_container_width=True)
    st.markdown('<div class="placeholder-img">🖼️ Coloque a imagem ilustrativa dos serviços aqui</div>', unsafe_allow_html=True)
    
    with st.form("form_servico"):
        st.subheader("Formulário de Solicitação")
        nome_servico = st.text_input("Seu Nome Completo")
        email_servico = st.text_input("Seu E-mail")
        tel_servico = st.text_input("Telefone / WhatsApp")
        tipo_atendimento = st.selectbox("Selecione o Serviço", ["Fisioterapia Especializada", "Consultoria Científica", "Mentoria para Acadêmicos", "Outros"])
        mensagem_servico = st.text_area("Descreva sua necessidade ou objetivo")
        
        enviar_servico = st.form_submit_button("Enviar Solicitação de Contato")
        if enviar_servico:
            if nome_servico and email_servico:
                st.success("Solicitação enviada com sucesso! Entraremos em contato em breve.")
            $else$:
                st.warning("Por favor, preencha pelo menos o seu nome e e-mail.")

# ==========================================
# ABA 3: CURSOS E PALESTRAS
# ==========================================
with tab3:
    st.header("Cursos, Capacitações e Palestras")
    st.write("Confira a agenda de eventos presenciais na PUC Goiás e online.")
    
    # Para substituir a imagem de eventos: st.image("imagens/cursos.jpg", use_container_width=True)
    st.markdown('<div class="placeholder-img">🖼️ Coloque a imagem do próximo evento ou banner aqui</div>', unsafe_allow_html=True)
    
    st.markdown("### 📌 Próximo Evento em Destaque")
    st.info("**Tema:** Atualizações Clínicas em Fisioterapia e Reabilitação\n\n**Data:** A definir | **Local:** PUC Goiás / Online")
    
    with st.form("form_inscricao_evento"):
        st.subheader("Inscrição para o Evento")
        nome_curso = st.text_input("Nome Completo do Participante")
        email_curso = st.text_input("E-mail para envio de informações")
        crf_ou_vinculo = st.text_input("Nº de Registro profissional (CREFITO) ou Vínculo Acadêmico")
        
        inscrever = st.form_submit_button("Garantir Minha Inscrição")
        if inscrever:
            if nome_curso and email_curso:
                st.success(f"Inscrição realizada com sucesso, {nome_curso}! Um e-mail de confirmação será enviado.")
            else:
                st.warning("Preencha os campos obrigatórios.")

# ==========================================
# ABA 4: VERIFICAÇÃO DE CERTIFICADOS
# ==========================================
with tab4:
    st.header("Verificação de Autenticidade de Certificados")
    st.write("Digite o código alfanumérico impresso no seu certificado para comprovar sua validade na PUC Goiás.")
    
    # Para substituir a imagem da aba: st.image("imagens/certificados.jpg", use_container_width=True)
    st.markdown('<div class="placeholder-img">🖼️ Coloque uma imagem ilustrativa de validação/certificados aqui</div>', unsafe_allow_html=True)
    
    codigo_input = st.text_input("Código do Certificado (Ex: PUC-FISIO-2026-001)").strip()
    
    if st.button("Verificar Autenticidade"):
        # Base de dados simulada de códigos (pode ser ligada ao Google Sheets futuramente)
        base_certificados = {
            "PUC-FISIO-001": {"valido": True, "curso": "Atualidades em Fisioterapia", "data": "Janeiro de 2026", "carga": "20h"},
            "PUC-FISIO-002": {"valido": True, "curso": "Biomecânica Aplicada", "data": "Fevereiro de 2026", "carga": "10h"}
        }
        
        if codigo_input in base_certificados:
            cert = base_certificados[codigo_input]
            st.success("✅ **Certificado Válido e Autêntico!**")
            st.write(f"- **Curso/Evento:** {cert['curso']}")
            st.write(f"- **Carga Horária:** {cert['carga']}")
            st.write(f"- **Data de Emissão:** {cert['data']}")
            st.write("- **Instituição:** PUC Goiás")
        elif codigo_input == "":
            st.warning("⚠️ Insira um código no campo acima.")
        else:
            st.error("❌ **Certificado não encontrado.** Verifique se digitou o código corretamente.")

# ==========================================
# ABA 5: E-BOOKS E PUBLICAÇÕES
# ==========================================
with tab5:
    st.header("E-books e Materiais Acadêmicos")
    st.write("Materiais didáticos, guias práticos e e-books publicados para suporte acadêmico e profissional.")
    
    col_eb1, col_eb2 = st.columns(2)
    
    with col_eb1:
        # Para substituir a capa do ebook: st.image("imagens/ebook1.jpg", width=200)
        st.markdown('<div class="placeholder-img" style="padding: 30px;">📖 Capa do E-book 1</div>', unsafe_allow_html=True)
        st.subheader("Guia Prático de Avaliação Motora")
        st.write("Abordagem detalhada sobre exames físicos e testes funcionais.")
        st.link_button("📥 Baixar / Acessar E-book", "https://link-do-seu-ebook-aqui.com")
        
    with col_eb2:
        # Para substituir a capa do ebook: st.image("imagens/ebook2.jpg", width=200)
        st.markdown('<div class="placeholder-img" style="padding: 30px;">📖 Capa do E-book 2</div>', unsafe_allow_html=True)
        st.subheader("Reabilitação Baseada em Evidências")
        st.write("Artigos compilados e diretrizes clínicas para o cotidiano do fisioterapeuta.")
        st.link_button("📥 Baixar / Acessar E-book", "https://link-do-seu-ebook-aqui.com")

# Rodapé padrão do site
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>© 2026 Prof. Dr(a). [Seu Nome] • Docente da PUC Goiás • Todos os direitos reservados.</p>", 
    unsafe_allow_html=True
)
