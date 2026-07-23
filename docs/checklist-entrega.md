# ✅ Checklist de Validação Pré-Entrega

> Marque todos os itens antes de colar o HTML no Moodle.

## Estrutura e Segurança

- [ ] **Apenas `<body>`**: O código NÃO contém `<html>`, `<head>`, `<body>` ou `<!DOCTYPE>`
- [ ] **Container correto**: Usa `<div class="container py-4 vagalume-pagina">`
- [ ] **Sem `<style>`**: Nenhuma tag `<style>` ou `<link>` no HTML
- [ ] **Sem `onclick`**: Nenhum atributo `onclick=""` inline
- [ ] **Sem CDN**: Nenhum link para Bootstrap, Font Awesome ou outras CDNs
- [ ] **Placeholders**: Toda imagem em teste tem `src=""` (vazio)
- [ ] **Formato de imagens**: PNG ou JPEG (nunca WebP)
- [ ] **Atributos de imagem**: Todas têm `width`, `height` e `loading="lazy"`

## Preservação e Higienização

- [ ] **Comentários preservados**: Todos os `<!-- -->` do storyboard foram mantidos intactos
- [ ] **Sem `contenteditable="false"`**: Removido de todas as tags (exceto `.h5p-placeholder`)
- [ ] **Sem CAIXA ALTA**: Títulos e textos decorativos estão em formato Capitalize
- [ ] **Sem `font-size` inline**: Usa classes Bootstrap (`.h1`–`.h6`, `.font-weight-bold`, etc.)

## Identidade Visual

- [ ] **Cores Vaga Lume**: Botões usam `#D96F1A`, textos usam `#261810` ou `#5B3925`
- [ ] **Classes `.vagalume-`**: Prefira classes globais a CSS inline
- [ ] **Fonte**: Mantida a font-family do `.vagalume-pagina`
- [ ] **Títulos**: Cor `#5B3925`, weight `700`

## Acessibilidade

- [ ] **Hierarquia de headings**: h1 → h2 → h3 (sem pular)
- [ ] **Alt de imagens**: Preenchido ou vazio com `role="presentation"` (se houver descrição longa)
- [ ] **Imagens clicáveis**: Têm `style="cursor: zoom-in;"`, `role="link"`, `tabindex="0"`
- [ ] **Descrição longa**: Se houver `<p class="sr-only">`, a imagem tem `alt=""` + `aria-labelledby`
- [ ] **Destaques verdes**: Apenas em `<span>` e **fora** de blocos bege (sinopse/jumbotron)
- [ ] **Contraste em blocos bege**: Usar `<strong>` em vez de `.vagalume-destaque` dentro de sinopse/jumbotron
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
- [ ] **Links externos**: Têm `target="_blank"` + `rel="noopener noreferrer"` + classe `.nomediaplugin`
- [ ] **E-mails com `.nomediaplugin`**: Para evitar conversão automática em blocos

## Final

- [ ] **Arquivo salvo**: Em `templates/pages/` com nome descritivo
- [ ] **Componente novo**: Se criou, registrou em `components-library.md`
- [ ] **Imagens novas**: Estão em `assets/images/(capas|ilustracoes|personagens)/`

---

> **Dica**: Se o Moodle acusar erro `storedfileproblem` ao salvar, verifique:
> 1. Se há `src` com caminho inválido em alguma imagem
> 2. Se há tag `<style>` ou `<link>` no HTML
> 3. Se há links sem `.nomediaplugin` que o Moodle está tentando converter
