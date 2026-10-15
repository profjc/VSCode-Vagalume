# Método, cenários e regras anti-dupla-contagem

> Como transformar o **inventário** (quantidades) em **tempo**. Genérico e reutilizável.
> **Versão 1.2 (15/10/2026)** — projeto de origem: Vaga Lume.

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
8. **Imagem recapitulada / thumb de player** → **0 s**: um mural que **repete** imagens já contadas num
   carrossel, ou a **miniatura de um vídeo já contado**, **não** é conteúdo novo.
9. **Página da Sequência Didática × PDF da SD** → a **página** conta no **A**; o **PDF** conta no **B**
   (é a regra 1 aplicada ao par página × anexo).
10. **Gravação do encontro** → a **página** do encontro **já carrega** as gravações no ar no seu próprio
    vídeo; a **linha de ajuste** traz **só** a gravação **nova/declarada** — nunca as duas de novo
    (*bug real do projeto de origem: as 2 gravações entraram em dobro até o cálculo corrigir*).

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
quantidade e acrescente, por linha, o tempo de cada categoria nos **4 cenários** e o **bucket** (A/B).
**Nunca** recalcule o inventário “de cabeça”, nem edite as quantidades à mão sem refazer o passo 1.

> **O dicionário do CSV de CÁLCULO** (as colunas de tempo por cenário, as **linhas de ajuste** e a
> **reconciliação com âncoras**) está em **`reference/calculo-e-planilha.md`** — é o Passo 4 detalhado.

## 6 — Natureza, limitações e estimativa por analogia (declarar no relatório)

- É **estimativa, não medição**. Se houver **relatório oficial de duração** do Moodle, **medir** e
  usar a estimativa apenas como comparação de sanidade.
- Itens sem duração localizada são marcados **"duração não localizada"** — **nunca** estimar no escuro.
- **Módulo previsto e ainda não produzido → estimativa POR ANALOGIA:** use um **módulo existente (medido)**
  como **modelo** e copie dele o tempo **categoria a categoria**, **declarando a ressalva** ("estimativa de
  ordem de grandeza, a substituir pela medição"). **Nunca** apresentar a analogia como se fosse medição.
  - O que **não** tiver quantidades definidas (um bloco ainda não produzido) fica **fora** do cálculo, com
    **nota**, e é **reincorporado na reexecução**.
  - A linha de analogia entra na planilha como uma **linha de ajuste** (`tipo_pagina = estimativa`), separada
    das páginas.
  - *Precedente: o **Módulo de Encerramento** (não produzido) foi estimado = **Módulo 0 (Boas-vindas)** —
    A mín 24min46s · ref 28min01s · máx 57min17s.*

## 7 — Decisões do cliente (registrar e versionar)

Toda escolha metodológica do projeto (**tempo por fórum**, **overhead**, **ppm**, **tipo de imagem**,
**interpretação do parâmetro H5P**, **analogia**…) vai para uma **tabela de decisões** — no projeto de
origem, a **§3 do plano** (`PLANO-carga-horaria.md`), com **número · questão · decisão**, cada linha datada.
Sem essa tabela, **a discussão se repete** a cada reexecução.

**Regra de reexecução — "bloqueio por inércia, revisão por gatilho":** ao reexecutar (Passo 6), os
parâmetros e as decisões **não** se rediscutem por padrão. Reabra **só** com gatilho declarado —
**(a)** pedido do cliente, **(b)** mudança do curso que **invalide** a decisão, ou **(c)** **evidência/fonte
nova**. Ao reabrir: registre **motivo + valor novo + data** na tabela e **refaça a validação de paridade**
(o número muda — e isso fica registrado).
