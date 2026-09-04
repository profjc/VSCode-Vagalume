# 🎨 Guia de Estilo - Curso Vaga Lume

> Documento oficial de identidade visual para produção de páginas HTML no Moodle 4.5 (Tema Trema)

---

## Paleta de Cores

| Cor | Hexadecimal | Amostra | Uso |
|-----|-------------|---------|-----|
| Laranja (principal) | `#D96F1A` | 🟠 | Botões, headers, bordas, hover, barras de progresso |
| Marrom (títulos) | `#5B3925` | 🟤 | Títulos, texto institucional, breadcrumb ativo |
| Marrom escuro (texto) | `#261810` | 🟤 | Corpo de texto para leitura confortável |
| Verde (institucional) | `#587C41` | 🟢 | Destaques no texto, borda de blocos de sinopse |
| Verde (fundo frontpage) | `#5D7A3C` | 🟢 | Fundo da página inicial do curso |
| Dourado | `#F8B133` | 🟡 | Títulos grandes em destaque na frontpage |
| Bege (fundo cards) | `#FAEBDD` | 🟡 | Fundo de cards, citações, jumbotrons, navbar |
| Branco | `#FFFFFF` | ⚪ | Fundo padrão de páginas de conteúdo |
| Laranja hover escuro | `#944B11` | 🟤 | Hover de botões |

### Gradientes e Sombras
- **Sombra de card**: `0 4px 12px rgba(217, 111, 26, 0.15)` (comum)
- **Sombra de card hover**: `0 12px 24px rgba(217, 111, 26, 0.25)`
- **Sombra de jumbotron**: `0 2px 8px rgba(0, 0, 0, 0.05)`

---

## Tipografia

| Elemento | Especificação |
|----------|---------------|
| **Font-family** | `'Segoe UI', Roboto, 'Helvetica Neue', sans-serif` |
| **Títulos (h1-h5)** | `font-weight: 700; color: #5B3925; line-height: 1.3` |
| **Corpo de texto** | `font-weight: 400; color: #261810; line-height: 1.5` |
| **Citações (`.vagalume-citacao`)** | `font-size: 1.4rem; font-style: italic; color: #5B3925; font-weight: 500` |
| **Autoria (`.vagalume-autora`)** | `font-size: 0.9rem; text-align: right; font-weight: 500` |
| **Destaque inline (`.vagalume-destaque`)** | ~~`font-weight: 600; color: #587C41`~~ — **DESCONTINUADO como ênfase (04/09/2026)**: usar `<strong>` que herda a cor do contexto (verde não é mais usado p/ destacar) |
| **Links** | `color: #944B11` (laranja-escuro) + negrito + sublinhado (regra §6.1); links-botão `.btn` mantêm laranja `#D96F1A` + texto branco |

### Responsivo
- **Mobile (< 768px)**: Citações: `1.1rem`, Jumbotron padding: `1.5rem 1rem`
- **Mobile (< 768px)**: Sinopses: `0.95rem`, padding: `1rem`

---

## Classes CSS Globais Disponíveis

> Estas classes estão no CSS do tema Trema. **Use-as no HTML, não as redefina.**

| Classe | Descrição |
|--------|-----------|
| `.vagalume-pagina` | Container principal (fonte, cor, espaçamento) |
| `.vagalume-jumbotron` | Citação de destaque (fundo bege, borda laranja, animação fadeInUp) |
| `.vagalume-citacao` | Texto da citação (itálico, marrom) |
| `.vagalume-autora` | Autoria da citação (alinhado à direita) |
| `.vagalume-destaque` | ~~Palavra em destaque (verde, negrito)~~ — **DESCONTINUADO como ênfase (04/09/2026)**: usar `<strong>` |
| `.vagalume-sinopse` | Bloco de sinopse/destaque (fundo bege, borda verde) |
| `.vagalume-destaque-bloco` | Mesmo que `.vagalume-sinopse` |
| `.vagalume-video` | Container de vídeo (max 640px, 16:9) |
| `.vagalume-h5p-card` | Card para atividade H5P (borda laranja) |
| `.vagalume-h5p-header` | Cabeçalho do card H5P (fundo laranja) |
| `.vagalume-h5p-body` | Corpo do card H5P (fundo branco) |

### Elementos Globais Customizados (CSS do Tema)
- **Botões (`.btn-primary`, `.btn-secondary`)**: Fundo `#D96F1A`, hover `#944B11`, border-radius `8px`
- **Breadcrumb**: Fundo bege `#FAEBDD`, texto laranja, separador `›` laranja
- **Navbar**: Fundo `#FAEBDD`, borda inferior laranja `3px solid #D96F1A`
- **Cards de curso**: Borda laranja, sombra laranja, hover com elevação `-8px`
- **Barra de progresso**: Cor laranja `#D96F1A`
- **Rodapé**: Oculto em páginas internas, laranja na frontpage

---

## Estrutura de Páginas

### Página Estática
```html
<div class="container py-4 vagalume-pagina">
    <h1>Título da Página</h1>
    <!-- Conteúdo -->
</div>
```

### Página Dinâmica (com JS)
```html
<div class="container py-4 vagalume-pagina">
    <!-- Conteúdo -->

    <script>
      document.addEventListener('DOMContentLoaded', function() {
          // Scripts locais seguros
      });
    </script>
</div>
```

---

## Acessibilidade

1. **Imagens com descrição longa**: `alt=""` + `role="presentation"` + `aria-labelledby="figX-desc"`
2. **Imagens clicáveis**: `style="cursor: zoom-in;"` + `role="link"` + `tabindex="0"` + data-toggle modal
3. **VLibras**: Já incluso no Moodle globalmente
4. **Hierarquia de headings**: h1 → h2 → h3, sem pular níveis
5. **Formato de imagens**: Apenas PNG e JPEG (nunca WebP)
6. **Atributos obrigatórios em imagens**: `width`, `height`, `loading="lazy"`

---

## Regras de Segurança (Anti-Bloqueio)

1. ❌ **Nunca** incluir tags `<style>` ou `<link>` no HTML
2. ❌ **Nunca** usar `onclick=""` inline em elementos
3. ❌ **Nunca** usar caminhos fictícios em `src` de imagens (usar `src=""`)
4. ✅ Usar `addEventListener` dentro de `DOMContentLoaded`
5. ✅ Usar classes Bootstrap 4 nativas (`row`, `col-md-*`, etc.)
