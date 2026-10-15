# 🗺️ Mapa do Projeto Vaga Lume

> Referência única de localização de arquivos e recursos. Consultar sempre que precisar saber onde salvar ou buscar algo.

## Estrutura de Pastas

| Local | Guarda | Observações |
|-------|--------|-------------|
| `templates/pages/` | Páginas **finais** HTML (prontas para colar no Moodle) | Subpastas por módulo (ex: `Boas-vindas/`, `M1/`, `M2/`) |
| `templates/pages/base/base.html` | Modelo base (snippet de partida) | — |
| `templates/components/` | Snippets avulsos reutilizáveis | Ex: `forum.html`; a biblioteca de componentes vive em `components-library.md` |
| `templates/documentos/` | **Espelhos A4** de documentos imprimíveis (**não** vão ao Moodle) | `espelho-relatorio.html` · `espelho-resumo-executivo.html` · `espelho-sequencia-didatica.html`; recebem o corpo no marcador `<!-- CONTEUDO -->` e são impressos pelo Chrome headless |
| `components-library.md` | Biblioteca completa de componentes (25 numerados) | Fonte única dos snippets/implementação |
| `content/` | `.md` de trabalho (convertidos do `.docx` do autor) | Subpastas por módulo (ex: `M1/`, `M2/`) |
| `temp/` | Arquivos do usuário para processamento | **"limpar"** = apagar conteúdo mantendo a pasta; **"excluir"** = deletar a pasta |
| `assets/images/capas/` | Imagens de capa | — |
| `assets/images/ilustracoes/` | Imagens de conteúdo | Subpastas por módulo (ex: `M1/`, `M2/`) |
| `assets/images/personagens/` | Personagens | — |
| `assets/images/logos/` | Logos institucionais | Ex: `LOGO_VAGALUME_RGB-transp-pq.png` |
| `assets/h5p/` | Backup local dos `.h5p` de origem | Subpastas por módulo (ex: `M1/`, `M2/`); manter o mesmo nome usado no placeholder (ex: `M2P1L1p3-H5P-question_set.h5p`) para rastreabilidade. Recursos internos do pacote (imagens/svg) ficam na mesma subpasta junto ao `.h5p` |
| `assets/pdf/` | **PDFs anexos das páginas** (ex.: as 13 Sequências Didáticas do M4) | Subpastas por módulo (`M4/`); o nome-base é igual ao da página (`M4P3L2p2.pdf` ↔ `M4P3L2p2.html`) |
| `assets/documentos/` | **Documentos-base da esteira de impressão** | `referencia-relatorio.docx` — o *reference-docx* do pandoc, gerado por `scripts/gerar-reference-docx.py` |
| `assets/images/relatorios/` | **Gráficos dos relatórios** (PNG) | `grafico-modulos.png` · `grafico-categorias.png`, gerados por `scripts/gerar-graficos-relatorio.py` |
| `assets/css/` | CSS global do tema (fonte Trema — **não** redefine classes) | `vagalume-tema.css` — fonte da verdade das classes `.vagalume-*` |
| `docs/` | Documentação do projeto | Workflow, checklist, diretrizes, galeria, backups |
| `docs/backups/` | Backups versionados do `.clinerules` e CSS | Padrão: `clinerules-vN-antes-[descrição].md` |
| `scripts/` | Scripts de apoio do projeto | **Fidelidade/QA:** `check-fidelidade.py` (confere a página HTML contra o trecho do DI: `python3 scripts/check-fidelidade.py <pagina.html> <DI.md> <linha_ini> <linha_fim>`) · **SD em PDF:** `gerar-pdf-sd.sh` (PDF A4 da Sequência Didática, a partir da página + espelho) · **Carga horária — esteira:** `inventario-recursos.py` (inventário de recursos: `python3 scripts/inventario-recursos.py`) · `calculo-carga-horaria.py` (cálculo página a página — lê o inventário + os ajustes finos e gera o `.csv`/`.md`) · `gerar-graficos-relatorio.py` (2 gráficos PNG) · `gerar-relatorio.sh` (relatório: PDF A4 via espelho + Chrome headless) · `gerar-relatorio-docx.sh` (relatório: DOCX + planilha `.xlsx`) · `gerar-resumo-executivo.sh` (resumo executivo: PDF A4) · `gerar-resumo-executivo-docx.sh` (resumo executivo: DOCX) · **pós-processadores DOCX (usados pelos dois `-docx`):** `gerar-reference-docx.py`, `ajustar-tabelas-docx.py`, `adicionar-logos-docx.py` |
| `skills/` | **Skills reutilizáveis do agente** (pacotes exportáveis para outros projetos) | `skills/metricas-carga-horaria/` — skill de **estimativa de carga horária de cursos Moodle** (**v1.2**): `SKILL.md` (método em **6 passos**) + `reference/` (parâmetros+fontes, método/cenários+decisões do cliente, planilha de cálculo, esteira de documento, resumo executivo, armadilhas, tipos de H5P, durações/cruzamento) + `assets/` (scripts de inventário e de cálculo, config+ajustes de exemplo, **2 esqueletos** — relatório e resumo executivo — e a pasta **`esteira/`** com espelhos A4, pós-processadores DOCX e scripts de geração). **Exportar = copiar a pasta** e rodar a **validação de paridade**. **Governança:** a skill é a **fonte do MÉTODO**; cada projeto mantém a sua **instanciação** (decisões do cliente) — aqui, `docs/relatorios/carga-horaria/parametros-carga-horaria.md`. |
| `docs/historico/` | **Arquivo do log de sessões** (blocos antigos do `Onde-paramos.md`) | Rotação: quando o log passar de ~2.000 linhas (~300 KB), mover para cá os blocos anteriores ao front de trabalho atual. **Consulta histórica — não é leitura obrigatória de sessão.** Ex.: `onde-paramos-arquivo-ate-11-10-2026.md` |
| `docs/relatorios/` | **Relatórios do projeto** (produtos para impressão/gestão, fora do fluxo do Moodle) | Subpasta `carga-horaria/`: `PLANO-carga-horaria.md` (plano vivo da estimativa), `inventario-recursos.md`/`.csv` (Ciclo 1 — inventário gerado por script), `parametros-carga-horaria.md` (Ciclo 2 — parâmetros de tempo com fontes citadas), `ajustes-finos.md` (Ciclo 3 — imagens/fóruns/bibliografia/textos externos/SDs), `calculo-carga-horaria.csv`/`.md`/`.xlsx` (Ciclo 4 — cálculo página a página + tabelas-resumo), `Relatorio-carga-horaria.md` + `Relatorio-carga-horaria-vagalume.pdf` (10 pág.)/`.docx` (Ciclo 5) e `Resumo-executivo-carga-horaria.md` + `Resumo-executivo-carga-horaria-vagalume.pdf` (2 pág.)/`.docx` (Ciclo 6) |
| `Onde-paramos.md` | Checkpoint de continuidade entre sessões | Ler ao iniciar sessão; atualizar ao encerrar |

## Nomeação de arquivos — correspondência dos módulos

**Regra (firmada 06/09/2026):** continuamos nomeando arquivos/pastas como `M0`, `M1`, `M2`… (padrão do projeto), mas devemos **sempre manter a correspondência com o nome real do módulo** em legendas, comentários identificadores e nomes visíveis. A ordem dos tiles/cards do curso segue esta tabela.

| Padrão (prefixo) | Nome real do módulo (título exibido no curso) | Pasta/ícone correspondente |
|---|---|---|
| **M0** | **Boas-vindas!** | `templates/pages/Boas-vindas/`, `content/Boas-vindas/`; ícone `tile-00-boas-vindas.png` |
| **M1** | **Primeira Infância** | `templates/pages/M1/`, `content/M1/`; ícone `tile-01-primeira-infancia.png` |
| **M2** | **Leitura e Primeira Infância** | `templates/pages/M2/`, `content/M2/`; ícone `tile-02-leitura-primeira-infancia.png` |
| **M3** | **Bibliotecas Comunitárias** | `templates/pages/M3/`, `content/M3/`; ícone `tile-03-bibliotecas-comunitarias.png` |
| **M4** | **Mãos na massa! (ou nos Livros!)** | `templates/pages/M4/`, `content/M4/`; ícone `tile-04-mao-na-massa.png` |
| **Encerramento** (sem número M5) | **Certificação e Avaliação do curso** | `templates/pages/Encerramento/`, `content/Encerramento/`; ícone `tile-05-certificacao-avaliacao.png` |

> **Observações:** (1) **M0 = Boas-vindas** — embora os arquivos usem `templates/pages/Boas-vindas/`, para fins de numeração de tiles é o módulo **0**. (2) O **Encerramento não tem numeração `M5`** — o ícone é os prefixado `05` (ordem no curso após o M4) e o título real é "Certificação e Avaliação do curso". (3) Ícones dos tiles (versão bege `#FAEBDD`) vivem em `assets/images/icones-tiles/`, mapeados no CSS por `#tileicon_N` (`_1`=M0 … `_6`=Encerramento).

## Storyboards

**NÃO mantemos arquivos separados de storyboard** — apenas o HTML final. O DI pensa o storyboard mentalmente e entrega a página pronta.

## Classes CSS Globais (`.vagalume-*`)

Definidas no CSS global do tema Trema (SCSS Póst). **NÃO redefinir** — apenas usar. A fonte da verdade é `assets/css/vagalume-tema.css`.

| Classe | Descrição |
|--------|-----------|
| `.vagalume-pagina` | Container principal (fonte, cor, espaçamento) |
| `.vagalume-jumbotron` | Bloco de destaque versátil (fundo bege, borda laranja) — boas-vindas, chamadas introdutórias, citações |
| `.vagalume-citacao` | Texto da citação (itálico, marrom) |
| `.vagalume-autora` | Autoria da citação (alinhado à direita) |
| `.vagalume-destaque` | Palavra em destaque no texto (verde, negrito) — apenas em `<span>` |
| `.vagalume-sinopse` | Bloco de sinopse/destaque (fundo bege, borda verde) |
| `.vagalume-destaque-bloco` | Mesmo que `.vagalume-sinopse` |
| `.vagalume-video` | Container de vídeo (max 640px, 16:9) |
| `.vagalume-h5p-card` | Card para atividade H5P (borda laranja) |
| `.vagalume-h5p-header` | Cabeçalho do card H5P (fundo laranja) |
| `.vagalume-h5p-body` | Corpo do card H5P (fundo branco) |

## Arquivos de Consulta Obrigatória

Consultar antes de criar qualquer página:

- **`style-guide.md`** → cores, tipografia e paleta completa
- **`components-library.md`** → snippets e implementação dos componentes
- **`assets/css/vagalume-tema.css`** → classes CSS globais disponíveis
- **`docs/checklist-entrega.md`** → checklist de validação pré-entrega
- **`skills/metricas-carga-horaria/SKILL.md`** → quando o pedido envolver **carga horária / tempo de dedicação / carga efetiva** de um curso (skill exportável para outros projetos; ver a linha `skills/` na tabela acima)