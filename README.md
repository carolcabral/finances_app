- [ ] Add_revenue
    - [ ] Como trabalhar com mais de uma tabela no SQLAlchemy
    - [ ] Categorias de receita
    - [x] Mesma pagina que add_expense
        - [ ] new-entry/{form}
    - [ ] Separar categorias no html
    - [ ] Atualizar o balanço geral

- [ ] Lógica para armazenar categorias na base de dados (como pegar parent de optgroup?)
    - [ ] Trasformar input in camelcase (impedir duplicidade)

- [ ] Gerar relatórios com plotly
    - [ ] Escolher intervalo
    - [ ] Fixo vs variável
    - [ ] Pie por parent tag
        - [ ] Pie por child tag dentro da parent tag


- [ ] Gerenciar view para adicionar nova categoria em admin
- [ ] Ajustes de rota para categorias (mudar de admin)
- [ ] Ajuste de rota pra index (armazenar mês e ano)
    - [ ] Mudar input buttons prev/next
- [ ] Quando isFixed, atualizar meses para frente (criar nova tabela com fk? se add despesa, atualiza sozinha?)
- [ ] Status (pago, atrasado, default)
    - [ ] Atualizar no balanço atual

- [ ] Controle de erros
    - [ ] Retornar mensagem
    - [ ] Flash message se campos não estiverem preenchidos
        - [ ] Add_expense
        - [ ] Report
        - [ ] Update
        - [ ] Categoria já adicionada

- [ ] Remover categorias (base de dados depois?)
## Style

- [ ] Prev / Next buttons
- [ ] Delete Icon
- [ ] Linkar página de update na linha inteira da tabela

## Version control 
20-dez | 
- [x] Navbar na página base
- [x] Ajuste de style na tabela principal
    - [x] Balanco real / previsto (sem dados ainda)
- [x] Gerenciar views (revenue/expense)
    - [x] Ajuste de rotas /expense => new-entry 


21-nov | Added categories in add_expense
- [x] Categorias com input select

20-nov | Input type data, isFixed, início de relatórios e categorias e bug fixes 
- [x] Campo para despesas fixas
- [x] Inserir data como calendário
    - [x] Separar por mês (na base de dados e nas páginas)
    - [x] Ordenar por data
    - [x] Limitar meses até 12
    - [x] Armazenar valor da data no update
    - [x] Tags e categorias como json
19-nov | Initial commit 
- [x] Criar base de dados;
- [x] Funções de adicionar, alterar e deletar despesas;
