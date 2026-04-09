# Fluxograma do Sistema

## TELOS CONSULTORIA – FLUXOS PRINCIPAIS

### FLUXO 1: AUTENTICAÇÃO
Usuário (operador/gerente) → Login (email/senha) → Session Manager → Token gerado → Acesso a Dashboard

### FLUXO 2: FATURAMENTO RH (Processo Principal)
1. Acesso a [/billing] página
2. Operador seleciona:
   - Empresa (Company)
   - Período (Mês/Ano)
3. Sistema:
   - Conecta ao banco MSSQL do Senior via SOAP
   - Extrai eventos de folha (salários, encargos, benefícios)
   - Classifica por tipo: SALARIO_DIA, HORA_EXTRA, VALE_TRANSPORTE, etc.
   - Agrupa por funcionário e centro de custo
4. Operador:
   - Revisa período em draft
   - Upload de arquivo de exames médicos (opcional)
   - Upload de arquivo de EPIs (opcional)
5. Sistema:
   - Processa validações dos dados
   - Busca exames de MedicalExam por matrícula
   - Busca EPIs de EpiPurchasePackage por período
   - Monta planilha FEMSA com:
     * Identificação do funcionário
     * Proventos (salários, extras, adicionais)
     * Descontos (vale transporte, tributos)
     * Exames médicos
     * EPIs (se houver)
     * Centros de custo
6. Resultado:
   - Download .xlsx (planilha FEMSA)
   - OU Download .zip (FEMSA + documentos de EPI)

### FLUXO 3: GESTÃO DE EXAMES MÉDICOS
Cadastro → Busca por matrícula → Link automático na fatura
[Endpoints: GET/POST/PUT/DELETE /api/medical-exams]

### FLUXO 4: GESTÃO DE EPIS
Criar pacote de compra → Adicionar itens → Upload de documentos → Incluir em ZIP com fatura
[Endpoints: CRUD /api/epi-purchases]

### FLUXO 5: GESTÃO DE CLIENTES
CRUD de clientes → Atribuição de funcionários → Rastreamento de receita
[Endpoints: GET/POST/PUT/DELETE /api/customers]

### FLUXO 6: GERAÇÃO DE RELATÓRIOS
Seleção de tipo de relatório → Processamento assíncrono → Armazenamento → Download
[Endpoints: GET/POST /api/reports]