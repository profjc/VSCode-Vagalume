# Esteira de documento — instância de exemplo (Vaga Lume)

> **O que é esta pasta.** Os arquivos aqui são a **esteira comprovada** que gerou o relatório e o resumo
> executivo de carga horária do **projeto de origem (Vaga Lume)**, doados **como estão** (escopo **A** da
> v1.2). Eles **funcionam no projeto de origem**; para outro projeto, ajuste **caminhos, produto e marca**.
> O **método** (como usar, comandos, armadilhas) está em `reference/esteira-documento.md`.

## Mapa dos arquivos

| Arquivo | Papel |
|---|---|
| `espelho-relatorio.html` | **espelho A4** do relatório (identidade: logos, cores, `@page A4`, badges `.cg/.cb/.ch`) |
| `espelho-resumo-executivo.html` | **espelho A4** do resumo (cabeçalho compacto, sem capa) |
| `gerar-relatorio.sh` | `.md` → corpo HTML → injeta no espelho → **PDF** (Chrome headless) |
| `gerar-relatorio-docx.sh` | **DOCX** (pandoc + `--reference-doc` + pós-processadores) + **XLSX** (`soffice`) |
| `gerar-resumo-executivo.sh` | **PDF** do resumo (idem, espelho compacto) |
| `gerar-resumo-executivo-docx.sh` | **DOCX** do resumo (fluxo natural, **sem** quebra forçada) |
| `gerar-reference-docx.py` | gera o `reference-docx` da marca (fonte Segoe UI + cores dos títulos) |
| `ajustar-tabelas-docx.py` | conserta o `<w:tblGrid />` **vazio** do pandoc 2.9 (colunas colapsavam) |
| `adicionar-logos-docx.py` | insere os logos no topo do DOCX |
| `gerar-graficos-relatorio.py` | 2 gráficos PNG (matplotlib) a partir do `.csv` de cálculo |

## O que trocar ao exportar

- **Caminhos** (`docs/relatorios/...`, `templates/documentos/...`, `assets/...`) — os scripts usam
  `RAIZ="$(dirname ...)/.."` e caminhos **do projeto de origem**.
- **Marca**: logos (`assets/images/logos/*.png`), cores (`#D96F1A`, `#5B3925`, `#FAEBDD`) e a fonte.
- **Produto**: título do curso, responsável e nomes de arquivo de saída.
- **`reference-docx`**: sai em **Letter** por padrão — o **entregável de impressão é o PDF A4**
  (ver `reference/esteira-documento.md` §4, trava 2).

> ⚠️ **Nenhum destes scripts deve ser rodado “no escuro”**: todos **escrevem** arquivos. Em teste,
> redirecione **as saídas** para fora do repositório (`/tmp`) e confirme com `git status`
> (armadilha nº 26). O **caminho padrão é o arquivo oficial** do projeto.
