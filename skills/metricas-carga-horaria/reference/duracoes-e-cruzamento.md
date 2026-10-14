# Durações de vídeo e cruzamento com a bibliografia

> De onde vem a **duração** de cada vídeo e como evitar **dupla contagem** entre o vídeo assistido no
> curso e o **item de vídeo da bibliografia**. **Versão 1.1 (14/10/2026)** — origem: projeto Vaga Lume.

## 1 — Preferir os créditos da própria página

A legenda de créditos quase sempre traz a minutagem: `(22min07s)`, `(1h26min36seg)`, `(48s)`, `(7min08s)`.

**Cuidados:**
- a legenda pode ter **outros parênteses** (ex.: `Bel Mayer — … (2018) (11min42s)`) → use o **último**
  grupo entre parênteses que casar com o padrão de duração, nunca o primeiro;
- a página pode **divergir** do YouTube por 1 s (arredondamento do autor) — o **relatório uniformiza** e
  registra a diferença;
- **não** assuma que a página tem legenda: no projeto de origem, **2 de 19** vídeos não tinham.

## 2 — Quando a duração não está nos créditos (receita)

```bash
ID=TmNf3cDnM1Q     # id do vídeo (extraído do embed ou do link watch?v=)

# (a) conferência de identidade: título + canal
curl -s "https://www.youtube.com/oembed?url=https%3A//www.youtube.com/watch%3Fv%3D$ID&format=json"

# (b) duração real, em segundos
curl -s "https://www.youtube.com/watch?v=$ID" | grep -o '"lengthSeconds":"[0-9]*"' | head -1
```

- **Confira o `author_name`/`title`** do oEmbed contra o item da lista antes de aceitar a duração —
  é assim que se evita pegar o vídeo errado (títulos repetidos entre canais são comuns).
- A duração entra no **config** do projeto (`"duracoes": {"<id>": <segundos>}`) → a próxima execução
  fica **offline e reproduzível**.
- Se não localizar: marcar **“duração não localizada”**. **Nunca** estimar no escuro (armadilha nº 3).

## 3 — Vídeo com instrução de trecho

Instrução do tipo *“assista do minuto 34:29 até 54:15”* → conta **apenas o trecho**:

`segundos = fim − início` (com `MM:SS` já em minutos:segundos, **convertidos uma única vez**).

> ⚠️ **Erro clássico (cometido na 1ª versão do script):** converter `MM:SS` para minutos, subtrair e
> **multiplicar por 60** — dá **60×** o valor (19min46s virou “19h46min”). O correto é
> `34:29 → 2069 s`, `54:15 → 3255 s`, trecho = **1186 s = 19min46s**.
> No projeto de origem esse trecho convive com um vídeo de **1h36min45s**: contar o vídeo inteiro seria
> um erro de **+1h17** na carga.

## 4 — Cruzamento bibliografia × curso (anti-dupla-contagem)

O mesmo vídeo costuma aparecer **duas vezes**: embedado numa página de conteúdo **e** listado nas
Referências. Contar nos dois infla o bucket A.

**Procedimento:**
1. **Catálogo do curso:** para cada página, extraia `id`, título do crédito, canal e as páginas onde aparece.
2. **Itens da bibliografia:** para cada página de Referências, extraia o **canal/autor** (texto até o
   primeiro ponto) e o **título** (conteúdo do `<strong>`).
3. **Compare** com tokens normalizados (sem acentos, minúsculas, sem *stopwords*):
   aceite o casamento se **título ≥ 0,6** **ou** (**título ≥ 0,3** **e** **canal ≥ 0,6**).
4. **Vigie os dois falsos positivos:**
   - **por canal** — três vídeos da *mesma fundação* casam por canal com título diferente
     (título 0,0 / canal 1,0) → **não** é o mesmo vídeo;
   - **por título genérico** — dois vídeos com “mediação de leitura” no título casam entre si
     (título 1,0 / canal 0,0) → confirme o **canal**.
5. **Classifique o resultado:** o item da bibliografia é (a) o **mesmo vídeo já contado** no curso →
   conta **uma vez** (bucket A), ou (b) apenas **sugestão** → **registrado, não conta**
   (`reference/metodo-e-cenarios.md` §4.2 e §4.4).
6. O **inventário em Markdown** (saída do script) já traz essa tabela pronta na seção “Referências
   bibliográficas — cruzamento com os vídeos do curso”.

> **Resultado no projeto de origem:** 21 itens de vídeo na bibliografia → **16 eram o mesmo vídeo já
> contado** no conteúdo e **5 eram sugestões** (3 de um mesmo canal, +ChildFund, +Sesc). Sem o cruzamento,
> o bucket opcional seria contado duas vezes.
