# ✅ Checklist de Validação Pré-Entrega

> Marque todos os itens antes de colar o HTML no Moodle.

## Estrutura e Segurança

- [ ] **Apenas `<body>`**: O código NÃO contém `<html>`, `<head>`, `<body>` ou `<!DOCTYPE>`
- [ ] **Container correto**: Usa `<div class="container py-4 vagalume-pagina">`
- [ ] **Sem `<style>`**: Nenhuma tag `<style>` ou `<link>` no HTML
- [ ] **Sem `onclick`**: Nenhum atributo `onclick=""` inline
- [ ] **Sem CDN**: Nenhum link para Bootstrap, Font Awesome ou outras CDNs
- [ ] **Sem palavras em inglês/discrepantes**: Texto conferido contra o conteúdo-fonte do autor (N2.5.6) — "memory"→"memória", "protection"→"proteção", etc.
- [ ] **Placeholders**: Toda imagem provisória usa `src="[cole a imagem aqui]"` (NUNCA `src=""` vazio — o TinyMCE rejeita) + bloco temporário com imagem do placeholder único (`placeholder-800x600.jpeg`) + marcador "⚠️ APAGAR ESTE BLOCO"
- [ ] **Formato de imagens**: PNG ou JPEG (nunca WebP)
- [ ] **Atributos de imagem**: Todas têm `width`, `height` e `loading="lazy"`

## Preservação e Higienização

- [ ] **Comentários preservados**: Todos os `<!-- -->` do storyboard foram mantidos intactos
- [ ] **Sem `contenteditable="false"`**: Removido de todas as tags (exceto `.h5p-placeholder`)
- [ ] **Sem CAIXA ALTA**: Títulos e textos decorativos estão em formato Capitalize
- [ ] **Sem `font-size` inline**: Usa classes Bootstrap (`.h1`–`.h6`, `.font-weight-bold`, etc.)
- [ ] **Placeholder com URL fixa**: A imagem temporária usa SEMPRE a URL fixa do placeholder único (`https://vagalume.educagir.com.br/pluginfile.php/104/mod_resource/content/1/placeholder-800x600.jpeg`) — NUNCA data URI variável (N2.1.1.3)
- [ ] **Marcador "⚠️ APAGAR ESTE BLOCO" presente**: Todo bloco de imagem temporária tem o `<span>` vermelho de aviso antes da imagem (anti-comentário-solto)
- [ ] **Sem comentário não padrão**: Removido o comentário "Estrutura alinhada ao Manual da Marca Vaga Lume" quando presente (N3.6)
- [ ] **Comentário de abertura correto**: Página começa com `<!-- Módulo X - Parte Y - Lição Z - Página W - [título] -->` (numeração decimal; fóruns usam `Fórum Z -`; síntese/referências sem Lição) — imediatamente antes do container (N2.2.2)
- [ ] **Rodapé de fechamento correto**: Página termina com `<!-- FIM: ... -->` espelhando o comentário de abertura — após o `</div>` final (N2.2.2)
- [ ] **Nomeação de arquivo correta**: Páginas de lição `M2P3L1p2.html`; fóruns `M2P3F1.html`; síntese `M2P6P1.html`; labels `M2_Label_...`; minúsculas, sem acentos/espaços (N3.3)
- [ ] **Mudanças no nome do arquivo/cabeçalhos/rodapés verificadas**: Ao revisar, conferir se os ajustes do autor implicam mudanças no **nome do arquivo HTML**, nos **cabeçalhos/rodapés (`<!-- -->`)** ou em **títulos configurados no Moodle** — incluir na entrega (renomear via `git mv`) e na lista de tarefas do mestre (N3.6, 13/08/2026)
- [ ] **Caixa "Para refletir" (atenção contextual)**: Ficar atento ao contexto nos docs de DI para identificar situações onde vale usar a **Caixa "Para refletir"** (comp. 26 — card branco + borda laranja) — chamadas de reflexão, fechamento, sínteses reflexivas — **mesmo que o autor não tenha sugerido**; confirmar com o mestre antes de aplicar em páginas novas (N3.2.14, 14/08/2026)

## Identidade Visual

- [ ] **Cores Vaga Lume**: Botões usam `#D96F1A`; texto comum/cards usam `#261810` (marrom escuro); caixas creme e títulos usam `#5B3925` (marrom institucional)
- [ ] **Classes `.vagalume-`**: Prefira classes globais a CSS inline
- [ ] **Fonte**: Mantida a font-family do `.vagalume-pagina`
- [ ] **Títulos**: Cor `#5B3925`, weight `700`

## Acessibilidade

- [ ] **Hierarquia de headings**: h1 → h2 → h3 (sem pular)
- [ ] **Alt de imagens**: Preenchido ou vazio com `role="presentation"` (se houver descrição longa)
- [ ] **Imagens clicáveis**: Têm `style="cursor: zoom-in;"`, `role="link"`, `tabindex="0"`
- [ ] **Descrição longa**: Se houver `<p class="sr-only" id="figX-desc">`, a imagem tem `alt=""` + `role="presentation"` + `aria-labelledby="figX-desc"` (N2.4.7)
- [ ] **Sem duplicidade sr-only + alt**: Nunca `<span class="sr-only">` ou `<div class="sr-only">` — usar SEMPRE `<p class="sr-only" id="figX-desc">`; nunca `sr-only` **e** `alt` preenchidos ao mesmo tempo (N2.4.12)
- [ ] **Destaques verdes (`vagalume-destaque`)**: **DESCONTINUADO** como ênfase (§6.2/N2.4.13) — não usar para destacar texto. Onde houver destaque tipográfico do autor, usar `<strong>`.
- [ ] **Negritos sem cor manual (§6.2)**: `<strong>` **nunca** tem `style` nem classe de cor — herda a cor do contexto. No fundo branco/cards = `#261810`; dentro de caixas creme = `#5B3925`.
- [ ] **Caixas creme**: texto/`<strong>` em `.vagalume-destaque-bloco`, `.vagalume-sinopse` ou `.vagalume-jumbotron` deve ser **marrom `#5B3925`** — **sem** `color: #261810` manual.
- [ ] **Títulos `.h5`/`.h6` em `<span>`/`<p>` dentro de caixas**: fixar `color: #5b3925;` explícito (a classe `.h5` NÃO herda o marrom do CSS global — só tags reais h1–h5; precedente "Para participar" no fórum)
- [ ] **VLibras**: Não incluir snippet (já está no Moodle)

## Flutuação e Layout

- [ ] **`flow-root`**: Se houver imagens flutuantes, o container tem `style="display: flow-root;"`
- [ ] **Imagens flutuantes**: Usam `<figure>` com `border-radius: 8px; overflow: hidden;`
- [ ] **Blocos junto com float**: Sinopse/jumbotron ao lado de float encapsulado em `<div class="card border-0 bg-transparent">`

## Funcionamento no Moodle

- [ ] **IDs únicos**: Modais e elementos com `id` não se repetem
- [ ] **Bootstrap 4**: Grids usam `row`, `col-12`, `col-md-*` (não flexbox próprio)
- [ ] **H5P nativo**: Usa `.h5p-placeholder` (NÃO iframe manual)
- [ ] **Vídeos centralizados**: Usam grid `.col-lg-8`, ícone `fa-file-text` na sinopse
- [ ] **Links externos**: Têm `target="_blank"` + `rel="noopener noreferrer"` + classe `.nomediaplugin` + estilização **negrito + sublinhado + `color: #944b11`** (§6.1). Links-botão (`.btn btn-primary`) mantêm laranja `#D96F1A` + texto branco.
- [ ] **E-mails com `.nomediaplugin`**: Para evitar conversão automática em blocos
- [ ] **Zero "|"** em títulos/legendas/texto visível (§4.13): usar ":" como separador padrão
- [ ] **Legenda de vídeo (§4.14)**: formato `Título (minutagem); canal: nome do canal` — sem "(YouTube)", sem ":" redundante após o título, alinhada à esquerda
- [ ] **Fonte em legenda de imagem (§4.15)**: `.figure-caption` com fonte em **texto puro, sem `<a>`** — link só se houver indicação explícita

## Final

- [ ] **Arquivo salvo**: Em `templates/pages/` com nome descritivo
- [ ] **Componente novo**: Se criou, registrou em `components-library.md`
- [ ] **Imagens novas**: Estão em `assets/images/(capas|ilustracoes|personagens)/`

---

> **Dica**: Se o Moodle acusar erro `storedfileproblem` ao salvar, verifique:
> 1. Se há `src` com caminho inválido em alguma imagem
> 2. Se há tag `<style>` ou `<link>` no HTML
> 3. Se há links sem `.nomediaplugin` que o Moodle está tentando converter
