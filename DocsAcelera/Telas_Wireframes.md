# Telas / Wireframes

## 3.1 Tela de Login

**Localização**: [login.html](app/templates/login.html)

**Componentes**:
- Campo de email (input type="email")
- Campo de senha (input type="password")
- Botão "Entrar" (POST /api/auth/login)
- Tema dark/light toggle
- Branding Telos Consultoria (gold + preto)

**Ações**:
- Validação de credenciais
- Criação de token de sessão
- Redirecionamento para dashboard

---

## 3.2 Dashboard Principal

**Localização**: [dashboard_auth.html](app/templates/dashboard_auth.html)

**Componentes**:
- Header: Nome do usuário + último acesso
- Stat cards: Status (Online), Email, Último Acesso
- Ações rápidas:
  - Link para [Clientes]
  - Link para [Faturamento RH]
  - Link para [Relatórios]
- Tabela de informações do usuário (email, nome, status)

**Dados Dinâmicos**:
- `user.full_name`, `user.email`, `user.last_login`

---

## 3.3 Tela de Clientes

**Localização**: [customers_list.html](app/templates/customers_list.html)

**Componentes**:
- Header: "Clientes" + Botão "Novo Cliente"
- Tabela com colunas:
  - ID
  - Nome
  - Descrição
  - Criado em
  - Ações (Ver, Excluir)
- Paginação (skip/limit)

**Campos de Customer**:
- name, email, phone, company
- address, city, state, country, postal_code
- customer_type, status, total_revenue

**Endpoints Vinculados**:
- GET /api/customers (lista)
- GET /api/customers/{id} (detalhe)
- POST /api/customers (criar)
- PUT /api/customers/{id} (atualizar)
- DELETE /api/customers/{id}

---

## 3.4 Tela de Faturamento RH

**Localização**: [billing.html](app/templates/billing.html)

**Estrutura**: Tabs + Upload Areas

**Aba 1: Selecionar Período**
- Dropdown de empresas (Company.name)
- Seletor de período (mes_referencia: YYYY-MM)
- Botão para buscar período

**Aba 2: Upload de Folha de Pagamento**
- Drag & drop / File input (Excel ou CSV)
- Validação de formato
- POST /api/billing/upload-payroll
- Esperado: Colunas de funcionários, eventos, valores

**Aba 3: Upload de Exames Médicos**