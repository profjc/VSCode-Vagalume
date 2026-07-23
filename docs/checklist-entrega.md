# ✅ Checklist de Validação Pré-Entrega

> Marque todos os itens antes de colar o HTML no Moodle.

## Estrutura e Segurança

- [ ] **Apenas `<body>`**: O código NÃO contém `<html>`, `<head>`, `<body>` ou `<!DOCTYPE>`
- [ ] **Sem `<style>`**: Nenhuma tag `<style>` ou `<link>` no HTML
- [ ] **Sem `onclick`**: Nenhum atributo `onclick=""` inline
- [ ] **Sem CDN**: Nenhum link para Bootstrap, Font Awesome ou outras CDNs
- [ ] **Placeholders**: Toda imagem em teste tem `src=""` (vazio)
- [ ] **Formato de imagens**: PNG ou JPEG (nunca WebP)
- [ ] **Atributos de imagem**: Todas têm `width`, `height` e `loading="lazy"`

## Identidade Visual

- [ ] **Container**: Usa `<div class="container py-4 vagalume-pagina">`
- [ ] **Cores Vaga Lume**: Botões usam `#D96F1A`, textos usam `#261810` ou `#5B3925`
- [ ] **Classes `.vagalume-`**: Prefira classes globais a CSS inline
- [ ] **Fonte**: Mantida a font-family do `.vagalume-pagina`
- [ ] **Títulos**: Cor `#5B3925`, weight `700`

## Acessibilidade

- [ ] **Hierarquia de headings**: h1 → h2 → h3 (sem pular)
- [ ] **Alt de imagens**: Preenchido ou vazio com `role="presentation"` (se houver descrição longa)
- [ ] **Imagens clicáveis**: Têm `style="cursor: zoom-in;"`, `role="link"`, `tabindex="0"`
- [ ] **Descrição longa**: Se houver `<p class="sr-only">`, a imagem tem `alt=""` + `aria-labelledby`
- [ ] **VLibras**: Não incluir snippet (já está no Moodle)

## Funcionamento no Moodle

- [ ] **IDs únicos**: Modais e elementos com `id` não se repetem
- [ ] **Bootstrap 4**: Grids usam `row`, `col-12`, `col-md-*` (não flexbox próprio)
- [ ] **H5P**: Código embed dentro de `.vagalume-h5p-body`
- [ ] **Links**: Têm `target="_blank"` + `rel="noopener noreferrer"` se externos

## Final

- [ ] **Arquivo salvo**: Em `templates/pages/` com nome descritivo
- [ ] **Componente novo**: Se criou, registrou em `components-library.md`
- [ ] **Imagens novas**: Estão em `assets/images/(capas|ilustracoes|personagens)/`

---

> **Dica**: Se o Moodle acusar erro `storedfileproblem` ao salvar, verifique:
> 1. Se há `src` com caminho inválido em alguma imagem
> 2. Se há tag `<style>` ou `<link>` no HTML
