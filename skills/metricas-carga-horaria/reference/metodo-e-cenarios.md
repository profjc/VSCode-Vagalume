# Método, cenários e regras anti-dupla-contagem

> Como transformar o **inventário** (quantidades) em **tempo**. Genérico e reutilizável.
> **Versão 1.1.1 (14/10/2026)** — projeto de origem: Vaga Lume.

## 1 — Fórmula

`tempo(categoria) = quantidade × parâmetro × fator de cenário`

O cálculo é feito **página a página** (uma linha por página na planilha) e depois agregado por
**parte**, **módulo**, **categoria**, **bucket** e **total**. Toda quantidade é **rastreável até o
arquivo** de origem.

## 2 — Buckets (obrigatória × opcional)

| Bucket | Conteúdo típico |
|---|---|
| **A — obrigatória** | leitura das páginas · imagens · vídeos de conteúdo · atividades · fóruns · navegação · encontros (participação) · estudo de caso dos fóruns |
| **B — opcional/complementar** | bibliografia · anexos (PDF) · gravações dos encontros · materiais "sugeridos" |

**Regra:** o número principal do relatório é o **bucket A**; o **B** é apresentado **separado**.

## 3 — Cenários

| Cenário | Como obter |
|---|---|
| **Mínimo** | todos os parâmetros na ponta **rápida** |
| **Referência** | valores da tabela de parâmetros |
| **Máximo** | todos na ponta **lenta** |
| **Recomendado** | **referência + overhead** |

### Overhead de estudo
Percentual acrescido **apenas** ao cenário recomendado, para cobrir pausas, retomadas e espera
(ex.: feedback do fórum). **O ideal é ancorá-lo no próprio curso** (ex.: uma página que ensina o
Método Pomodoro 25+5 ⇒ ~20 % de pausa ⇒ adotar **10 %** é conservador). **Registre e versione a
decisão do cliente.** Faixa considerada: **0 ↔ +20 %**.

## 4 — Regras anti-dupla-contagem (essenciais)

1. **Página × anexo** da mesma atividade didática → **página no A, anexo no B**. Nunca somar os dois.
2. **Vídeo na bibliografia e também no conteúdo** → contar **uma vez** (bucket A); a bibliografia
   registra o item e a nota de sobreposição.
3. **Labels / páginas de navegação** → contam **só** na navegação (não são leitura de conteúdo).
4. **Vídeo sugerido** ("Quer saber mais?") → **registrado**, mas **não conta**.
5. **Fórum** → valor **por fórum** (ciclo completo exigido), **não** por postagem.
6. **Estudo de caso do fórum** → o **vídeo** conta pela regra "instruído conta"; o **texto/artigo**
   entra como **leitura computada** — em ambos os casos **sem** somar de novo o "ler instruções".
7. **Páginas de abertura, síntese e referências** → **leitura normal** (bucket A).

## 5 — Agregações de saída

Por **página** → por **parte** → por **módulo** → por **categoria** → por **bucket** → **total**
(com os cenários). A planilha de cálculo deve ter **uma linha por página** e colunas de
quantidades + tempos por cenário.

### Dicionário de dados — CSV do inventário (a interface do Passo 4)

| Coluna | O que é |
|---|---|
| `arquivo` | caminho relativo da página (**chave de rastreabilidade**) |
| `modulo` / `parte` / `licao` | sigla do módulo e posição na estrutura |
| `tipo_pagina` | `conteudo` · `abertura` · `sintese` · `referencias` · `forum` |
| `palavras` | palavras **visíveis** (sem tags, comentários, `<script>`/`<style>`) |
| `imagens` | marcadores da imagem oficial (**a imagem** é contada, não o arquivo) |
| `imagens_bloco_temp` | blocos temporários/placeholder a apagar — **não são conteúdo** |
| `videos_embedados` | vídeos em `iframe` |
| `videos_instruidos` | vídeos em link, **instruídos** na página/fórum (**contam**) |
| `videos_sugeridos` | “Quer saber mais?”/bibliografia — **não contam** |
| `video_segundos` | soma das durações **que contam** (embedados + instruídos + trechos) |
| `h5p_atividades` | nº de atividades na página |
| `h5p_itens` | soma dos itens/questões lidos dos pacotes (ver `h5p-tipos.md`) |
| `forum` | título do fórum (vazio quando não é fórum) |
| `links_externos` | links com `target="_blank"` (insumo de fórum/bibliografia) |
| `pdf` | `sim` quando existe anexo PDF com o nome da página |

**Regra de ouro:** a planilha de **cálculo** (Passo 4) **nasce deste CSV** — copie as colunas de
quantidade e acrescente, por linha, o tempo de cada categoria nos 4 cenários e o bucket (A/B).
**Nunca** recalcule o inventário “de cabeça”, nem edite as quantidades à mão sem refazer o passo 1.

## 6 — Natureza e limitações (declarar no relatório)

- É **estimativa, não medição**. Se houver **relatório oficial de duração** do Moodle, **medir** e
  usar a estimativa apenas como comparação de sanidade.
- Módulos/atividades **ainda não produzidos** ficam **fora** e são reincorporados na reexecução.
- Itens sem duração localizada são marcados **"duração não localizada"** — **nunca** estimar no escuro.
