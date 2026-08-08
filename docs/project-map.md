# 🗺️ Mapa do Projeto Vaga Lume

> Referência única de localização de arquivos e recursos. Consultar sempre que precisar saber onde salvar ou buscar algo.

## Estrutura de Pastas

| Local | Guarda | Observações |
|-------|--------|-------------|
| `templates/pages/` | Páginas **finais** HTML (prontas para colar no Moodle) | Subpastas por módulo (ex: `Boas-vindas/`, `M1/`, `M2/`) |
| `templates/pages/base/base.html` | Modelo base (snippet de partida) | — |
| `templates/components/` | Snippets avulsos reutilizáveis | Ex: `forum.html`; a biblioteca de componentes vive em `components-library.md` |
| `components-library.md` | Biblioteca completa de componentes (25 numerados) | Fonte única dos snippets/implementação |
| `content/` | `.md` de trabalho (convertidos do `.docx` do autor) | Subpastas por módulo (ex: `M1/`, `M2/`) |
| `temp/` | Arquivos do usuário para processamento | **"limpar"** = apagar conteúdo mantendo a pasta; **"excluir"** = deletar a pasta |
| `assets/images/capas/` | Imagens de capa | — |
| `assets/images/ilustracoes/` | Imagens de conteúdo | Subpastas por módulo (ex: `M1/`, `M2/`) |
| `assets/images/personagens/` | Personagens | — |
| `assets/images/logos/` | Logos institucionais | Ex: `LOGO_VAGALUME_RGB-transp-pq.png` |
| `assets/h5p/` | Backup local dos `.h5p` de origem | Subpastas por módulo (ex: `M1/`, `M2/`); manter o mesmo nome usado no placeholder (ex: `M2P1L1p3-H5P-question_set.h5p`) para rastreabilidade. Recursos internos do pacote (imagens/svg) ficam na mesma subpasta junto ao `.h5p` |
| `docs/` | Documentação do projeto | Workflow, checklist, diretrizes, galeria, backups |
| `docs/backups/` | Backups versionados do `.clinerules` e CSS | Padrão: `clinerules-vN-antes-[descrição].md` |
| `Onde-paramos.md` | Checkpoint de continuidade entre sessões | Ler ao iniciar sessão; atualizar ao encerrar |

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