- [ ] Lógica para armazenar categorias na base de dados (como pegar parent de optgroup?)
    - [ ] Trasformar input in camelcase (impedir duplicidade)
- [ ] Gerenciar views (select input categorias, revenue/expense)
- [ ] Add_revenue
    - [ ] Como trabalhar com mais de uma tabela no SQLAlchemy
    - [ ] Categorias de receita
- [ ] Flash message para adicionar nova categoria
- [ ] Ajustes de rota para categorias (mudar de admin)
- [ ] Ajuste de rota pra index (armazenar mês e ano)
- [ ] Quando isFixed, atualizar meses para frente (criar nova tabela com fk? se add despesa, atualiza sozinha?)


- [ ] Gerar relatórios com plotly
    - [ ] Escolher intervalo
    - [ ] Fixo vs variável
    - [ ] Pie por parent tag
        - [ ] Pie por child tag dentro da parent tag


- [ ] Controle de erros
    - [ ] Retornar mensagem
    - [ ] Flash message se campos não estiverem preenchidos
        - [ ] Add_expense
        - [ ] Report
        - [ ] Update
        - [ ] Categoria já adicionada


- [ ] Remover categorias (base de dados depois?)
## Style

- [ ] Navbar
- [ ] Prev / Next buttons
- [ ] Delete Icon
- [ ] Linkar página de update na linha inteira da tabela

## Version control 
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
