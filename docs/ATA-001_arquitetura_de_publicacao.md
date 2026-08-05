# ATA-002 --- Reestruturação da Arquitetura de Publicação

**Data:** 05/08/2026\
**Status:** Encerrada

------------------------------------------------------------------------

# Objetivo

Reestruturar a arquitetura de publicação do QuantImport, separando
definitivamente o processamento, a publicação e o portal.

------------------------------------------------------------------------

# Decisões Tomadas

## 1. Estrutura oficial do projeto

Foi definida a estrutura oficial do projeto:

``` text
quantimport/
├── structure.py
├── core/
├── publisher/
└── pages/
```

O arquivo `structure.py` passa a ser a única fonte oficial de definição
dos caminhos do projeto.

------------------------------------------------------------------------

## 2. Separação entre Core, Publisher e Pages

Foi estabelecida a separação funcional entre:

-   **Core**
-   **Publisher**
-   **Pages**

O **Core** passa a ser responsável exclusivamente pelo processamento dos
dados e pela geração dos artefatos necessários à publicação.

O **Publisher** passa a ser responsável pela leitura desses artefatos,
geração dos gráficos, criação da estrutura do portal, geração das
páginas e publicação.

A pasta **Pages** passa a conter exclusivamente o portal publicado e os
Documentos Oficiais do projeto.

------------------------------------------------------------------------

## 3. Repositório único

Foi eliminada a arquitetura baseada em múltiplos repositórios GitHub
independentes.

O portal passa a utilizar um único repositório:

``` text
QuantImportBrazil/pages
```

Toda a navegação passa a ocorrer através da estrutura de diretórios
desse repositório.

------------------------------------------------------------------------

## 4. Estrutura hierárquica

Foi eliminada a utilização de nomes compostos para representar
hierarquia.

Estrutura anterior:

``` text
uf/ba_mop/
```

Nova estrutura:

``` text
uf/
└── ba/
    └── mop/
```

A estrutura física passa a representar diretamente a estrutura lógica do
portal.

------------------------------------------------------------------------

## 5. Publicação

A função `github_publish()` foi adaptada para publicar exclusivamente o
repositório `pages`.

Ela deixa de criar repositórios individuais e passa a atualizar somente
o portal único.

------------------------------------------------------------------------

## 6. Índice do portal

Foi criado o primeiro índice central do portal:

``` text
pages/index.html
```

Sua função é servir como ponto inicial de navegação para o portal.

------------------------------------------------------------------------

## 7. Primeira publicação

Foi realizada com sucesso a primeira publicação utilizando a nova
arquitetura.

Foram disponibilizadas as páginas:

-   https://quantimportbrazil.github.io/pages/
-   https://quantimportbrazil.github.io/pages/uf/ba/mop/

Confirmando o funcionamento completo do fluxo:

``` text
Core
    ↓
Publisher
    ↓
Pages
    ↓
GitHub Pages
```

------------------------------------------------------------------------

# Assuntos discutidos

Durante a reunião foram discutidos diversos conceitos para evolução
futura da arquitetura, incluindo:

-   navegação em forma de mergulho;
-   agregação geográfica e por produtos;
-   agregação temporal;
-   diferenciação entre conteúdo público e conteúdo mensal não gratuito.

Esses temas permanecem em estudo e não constituem decisões arquiteturais
oficiais nesta ata.

------------------------------------------------------------------------

# Resultado

A arquitetura de publicação do QuantImport foi reestruturada com
sucesso.

O sistema passou de um modelo baseado em múltiplos repositórios
independentes para um portal único, hierárquico e centralizado,
preservando a separação entre processamento, publicação e apresentação.
