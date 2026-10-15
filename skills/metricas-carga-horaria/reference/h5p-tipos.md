# H5P — onde mora a contagem de itens (por tipo)

> Como o Passo 1 obtém o **nº de itens/questões** de cada atividade, lendo o `content.json` **de dentro**
> do pacote `.h5p` (que é um ZIP). **Versão 1.2 (15/10/2026)** — origem: projeto Vaga Lume.

## Por que isso importa

O parâmetro de atividades (`reference/parametros.md` #6) é **por item/questão**, não por atividade.
Uma atividade de 8 questões vale muito mais tempo que uma de 1 — e **a contagem não está no HTML**, está
dentro do pacote. Este mapa evita o erro de marcar tudo como "n/d" (aconteceu em **2 de 26** pacotes na
primeira versão do script, até tratar `dialogs` e `question.task`).

## Tabela — chave de contagem por tipo

| Tipo de H5P (nome no arquivo do projeto) | Biblioteca por trás | **Chave de contagem** | Exemplos reais | Nota |
|---|---|---|---|---|
| Question Set / Quiz / Múltipla escolha / Verdadeiro-Falso / Associação | `H5P.QuestionSet`, `H5P.MultiChoice` | **`questions`** (lista) | 9 · 8 · 5 · 4 · 3 · 1 | o mais comum |
| Virar cartões (*Dialog Cards*) | `H5P.Dialogcards` | **`dialogs`** (lista) | 3 | **não** usa `cards` |
| Arrastar e soltar (*Drag Question*) | `H5P.DragQuestion` | **`question.task.dropZones`** (nº de zonas) — alternativa `question.task.elements` | 5 zonas / 6 elementos | contagem **aninhada** em `question.task` |
| Arrastar palavras (*Drag Text*) | `H5P.DragText` | **`textField`** — conta os marcadores `*palavra*` | 8 | nº de lacunas, não de distratores |
| Caça-palavras (*Find the Words*) | `H5P.FindTheWords` | **`wordList`** (texto separado por vírgula) | 5 | contar as palavras da lista |
| Outros | — | fallback: `answers`, `choices`, `pairs`, `steps`, `blanks`, `words` | — | se nada casar → **`n/d`** |

## Como inspecionar um pacote (à mão)

```bash
unzip -l  pacote.h5p | head -30                          # ver a estrutura
unzip -p  pacote.h5p content/content.json | python3 -m json.tool | head -60
```

## Como o script decide (ordem exata)

1. percorre `questions` → `cards` → `dialogs` → `answers` → `choices` → `pairs` → `steps` → `blanks` → `words`
   e usa a **primeira lista não vazia**;
2. se não achar, tenta `question.task.dropZones` → `question.task.elements`;
3. depois `wordList` (string → conta os itens separados por `,`/`;`);
4. depois `textField` (conta os `*pares*` de asteriscos);
5. se nada casar, devolve **`n/d`** — **registre no relatório**, porque isso **subestima** o tempo dessa atividade.

> **Regra de honestidade:** `n/d` **não** é zero. Se um pacote não puder ser lido, diga no relatório
> ("atividade X sem contagem de itens") em vez de fingir precisão. Contar à mão pelo conteúdo publicado
> no Moodle é a alternativa.

## O que é do PROJETO (não da skill)

O **mapa página → tipo de H5P** é **da instanciação** (no projeto de origem, o dicionário `H5P_TIPO` no
`calculo-carga-horaria.py`). A skill guarda apenas **onde ler a contagem** (o `content.json`); enquadrar
cada pacote no tipo é uma **decisão do projeto**, auditável na seção de H5P do inventário. O mapeamento
também é o que permite aplicar o **parâmetro por tipo** (ver `reference/parametros.md`, #6, e a
**armadilha nº 24** sobre as duas interpretações possíveis).
