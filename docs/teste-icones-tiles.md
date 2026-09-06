# 🧪 Teste dos Ícones Personalizados dos Tiles (Cards) — Passo-a-passo

> **Objetivo:** validar no Moodle real a substituição dos ícones padrão do formato **Tiles** pelos cards personalizados do curso Vaga Lume.
> **Fonte:** `temp/Cards personalizados.docx` (especificação técnica) + imagens de teste em `temp/Cards/`.
> **Relacionado:** pendência 1 do projeto (ícones dos cards dos módulos para a capa do curso).

---

## 0. Contexto e decisões já tomadas

- O formato de curso é **Tiles**. O mecanismo é **CSS que esconde o ícone original** (o `i.icon` do Tiles) e **injeta a imagem escolhida** como `background-image` no contêiner `.tile-icon`, bloco por bloco (`#tileicon_N`).
- **Imagens escolhidas:** versão **01 (bege `#FAEBDD`)** — cor exata da paleta Vaga Lume; a versão 02 (rosa/lilás) está **fora da paleta** e foi descartada.
- **6 tiles cobertos:** Boas-vindas (00), M1 Primeira Infância (01), M2 Leitura (02), M3 Bibliotecas Comunitárias (03), M4 Mão na massa (04), Encerramento/Certificação (05).

### Verificação técnica das imagens (todas ✅)
| Critério | Especificação | Obtido |
|---|---|---|
| Dimensão | 128×128 px | 128×128 ✅ |
| Proporção | 1:1 | Quadrada ✅ |
| Formato | PNG-24 com transparência | sRGBA (alfa) ✅ |
| Peso | < 20 KB | 3,6–8,1 KB ✅ |
| Cor | RGB | sRGB ✅ |
| Margem interna (~10%/13px) | ⚠️ | "Boas-vindas" e "Certificação" têm só ~5 px no topo (aceitável; atentar no card) |

---

## 1. Passos no Moodle (responsabilidade do MESTRE)

1. **Localizar o número do curso.** Abrir a home do curso → F12 / inspecionar o `<body>` → anotar a classe `course-N` (ex.: `course-2`). Este número vai no seletor `.course-N .tile-icon`.
   - ✅ **Confirmado em 06/09/2026:** o curso é **`course-2`**.
2. **Criar uma página oculta para hospedar as imagens.** Ex.: curso → Adicionar um recurso → Página → nome "Recursos – Ícones dos Tiles" → deixar **oculta**.
   - ✅ **Feito de outra forma pelo mestre (06/09/2026):** as 6 imagens foram subidas em um **bloco HTML na home do curso**. URLs via `pluginfile.php/145/block_html/content/` (ver §1.1).
3. **Subir as 6 imagens** (versão 01) para essa página. Em cada arquivo de imagem: **Adicionar** → selecionar o PNG.
   - ✅ **Feito.**
4. **Copiar as 6 URLs.** Depois de anexadas, clicar com botão direito sobre cada imagem → **"Copiar endereço do link"** → obter as URLs `.../pluginfile.php/<context>/...`. Enviar as 6 URLs ao DI.
   - ✅ **Feito (ver §1.1).**
5. **Receber o CSS final do DI** e colar em: **Administração do curso → Aparência → CSS personalizado** (campo equivalente no tema Trema).
   - 📄 **CSS final pronto:** `docs/css-icones-tiles-para-colar.css` (usar seletor `.course-2`).
6. **Verificar a home do curso.** Confirmar que os 6 cards mostram os ícones novos e que o ícone original do Font Awesome desapareceu. Analisar **nitidez** (desktop + smartphone) e **contraste** do bege sobre o fundo colorido de cada tile.

> 💡 Se o bege ficar com pouco contraste em algum tile de fundo claro, alternativa: usar ícones **escuros** (marrom `#5B3925`) — **não** usar a versão 02 (rosa).

---

## 1.1 URLs reais das imagens (registro — 06/09/2026)

Contexto: `pluginfile.php/145/block_html/content/`. Base: `https://vagalume.educagir.com.br/pluginfile.php/145/block_html/content/`

| Tile | Arquivo original | Nome no repositório (`assets/images/icones-tiles/`) | URL (Moodle) |
|---|---|---|---|
| 1 — Boas-vindas | `00 - Boas-vindas! - 01.png` | `tile-00-boas-vindas.png` | `.../tile-00-boas-vindas.png` |
| 2 — M1 (Primeira Infância) | `01 - Primeira Infância - 01.png` | `tile-01-primeira-infancia.png` | `.../tile-01-primeira-infancia.png` |
| 3 — M2 (Leitura) | `02 - Leitura e Primeira Infância - 01.png` | `tile-02-leitura-primeira-infancia.png` | `.../tile-02-leitura-primeira-infancia.png` |
| 4 — M3 (Bibliotecas) | `03 - Bibliotecas Comunitárias - 01.png` | `tile-03-bibliotecas-comunitarias.png` | `.../tile-03-bibliotecas-comunitarias.png` |
| 5 — M4 (Mão na massa) | `04 - Mão na massa - 01.png` | `tile-04-mao-na-massa.png` | `.../tile-04-mao-na-massa.png` |
| 6 — Encerramento (Certificação) | `05 - Certificação e Avaliação do curso - 01.png` | `tile-05-certificacao-avaliacao.png` | `.../tile-05-certificacao-avaliacao.png` |

**URLs completas:**
```
https://vagalume.educagir.com.br/pluginfile.php/145/block_html/content/tile-00-boas-vindas.png
https://vagalume.educagir.com.br/pluginfile.php/145/block_html/content/tile-01-primeira-infancia.png
https://vagalume.educagir.com.br/pluginfile.php/145/block_html/content/tile-02-leitura-primeira-infancia.png
https://vagalume.educagir.com.br/pluginfile.php/145/block_html/content/tile-03-bibliotecas-comunitarias.png
https://vagalume.educagir.com.br/pluginfile.php/145/block_html/content/tile-04-mao-na-massa.png
https://vagalume.educagir.com.br/pluginfile.php/145/block_html/content/tile-05-certificacao-avaliacao.png
```
> ⚠️ **Atenção:** as imagens estão em um **bloco HTML da home**. Se o bloco for **ocultado/excluído**, as URLs podem quebrar. Durante o teste, manter o bloco visível ou, se preciso escondê-lo, reposicionar discretamente.

---

## 2. Passos no repositório (responsabilidade do DI)

1. Copiar as 6 imagens da versão 01 para `assets/images/icones-tiles/` com nomes limpos:
   - ✅ **Feito (06/09/2026).** Arquivos: `tile-00-boas-vindas.png`, `tile-01-primeira-infancia.png`, `tile-02-leitura-primeira-infancia.png`, `tile-03-bibliotecas-comunitarias.png`, `tile-04-mao-na-massa.png`, `tile-05-certificacao-avaliacao.png`.
2. Montar o **CSS final** do mecanismo usando o `course-N` e as URLs reais (modelo do docx):
   - ✅ **Feito (06/09/2026).** Arquivo: **`docs/css-icones-tiles-para-colar.css`** (seletor `.course-2`, URLs reais, `tileicon_1`–`tileicon_6`).
3. Registrar este procedimento no `Onde-paramos.md` (pendência 1 do projeto).
   - ✅ **Feito (06/09/2026).**

Modelo de referência (substituído pelo arquivo final):
```css
/* Esconde o ícone original dos tiles deste curso */
.YOUR-COURSE .tile-icon i.icon { display: none !important; }

/* Base da imagem nos tiles */
.YOUR-COURSE .tile-icon {
  background-size: contain !important;
  background-repeat: no-repeat !important;
  background-position: center !important;
  width: 40px !important;
  height: 40px !important;
  display: inline-block !important;
}

/* tileicon_1 = Boas-vindas ' */
.YOUR-COURSE #tileicon_1 .tile-icon {
  background-image: url('URL_IMAGEM_1') !important;
}
/* ... um bloco por tile, associando tileicon_N à URL correspondente */
```
3. Registrar este procedimento no `Onde-paramos.md` (pendência 1 do projeto).

---

## 3. Critérios de aceite (✅ APROVADO em 06/09/2026)

- [x] Os 6 cards exibem os ícones personalizados (bege `#FAEBDD`).
- [x] Ícone original (Font Awesome) não aparece mais.
- [x] Ícones nítidos em desktop e em smartphone (128px para ~36–40px de exibição).
- [x] Nenhum ícone parece "colado" na borda do círculo do card (margem interna ok).
- [x] Carregamento da home não sofreu impacto perceptível (peso < 20 KB ✅).
- [x] **Ícones na ordem correta** (`tileicon_1`–`tileicon_6`).

> ✅ **RESULTADO: TESTE APROVADO pelo mestre (06/09/2026).** Bloco HTML ocultado dos alunos sem derrubar os ícones — confirmada a lição de `pluginfile` de bloco oculto continuar acessível via CSS.

---

## 4. Após o teste (✅ CONCLUÍDO)

- ✅ **Aprovado** e replicado o mecanismo: bloco dos ícones acrescentado ao INÍCIO de `assets/css/vagalume-tema.css` (único CSS do tema) + imagens finais em `assets/images/icones-tiles/`. `Onde-paramos.md` atualizado — **pendência 1 encerrada**.
- Reprovação não ocorreu.

---
*Criado em 06/09/2026 · fonte `temp/Cards personalizados.docx` · imagens em `temp/Cards/`.*