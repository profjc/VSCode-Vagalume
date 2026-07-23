# 📋 Fluxo de Trabalho - Projeto Vaga Lume

## Visão Geral do Ecossistema

O processo de produção de páginas HTML para o curso Vaga Lume segue um fluxo de **4 etapas**, envolvendo 3 ferramentas distintas:

```
NotebookLM ──→ Briefing Pedagógico (Storyboard)
      │
      ▼
 Gemini/IA ──→ Código HTML do body
      │
      ▼
 Moodle 4.5 ──→ Colar no editor de texto
      │
      ▼
  Validação ──→ Checklist antes de publicar
```

## Papéis no Ecossistema

| Papel | Ferramenta | Responsabilidade |
|-------|-----------|-----------------|
| **Gestor/Designer Instrucional** | Você | Fornece o briefing pedagógico |
| **Operário Padrão** | Gemini Customizado (AI Studio) | Gera HTML das páginas cotidianas |
| **Engenheiro de Suporte** | Cline (aqui) | Resolve problemas complexos, depura erros, cria soluções |

## Fluxo Detalhado

### 1. Recebimento do Briefing
- O storyboard chega de um arquivo em `content/modulo-NN/`
- Contém: texto, referências de imagens, citações, estrutura pedagógica

### 2. Produção do HTML
Com base no briefing:

1. **Estruturar** → `<div class="container py-4 vagalume-pagina">`
2. **Verificar flutuação** → Se houver imagens flutuantes, adicionar `style="display: flow-root;"` ao container
3. **Adicionar conteúdo** → Textos, imagens (`src=""`), citações, H5P
4. **Aplicar classes** → `.vagalume-jumbotron`, `.vagalume-sinopse`, etc.
5. **Imagens flutuantes** → Usar `<figure>` com `border-radius: 8px; overflow: hidden;`
6. **Blocos junto com float** → Encapsular sinopse/jumbotron em `<div class="card border-0 bg-transparent">`
7. **Vídeos** → Centralizar com `.col-lg-8`, usar `.vagalume-video`, sinopse com `fa-file-text`
8. **H5P** → Usar `.h5p-placeholder` (NUNCA iframe manual)
9. **Links** → Adicionar `.nomediaplugin` em links externos e e-mails
10. **Acessibilidade** → Descrições longas, imagem clicável, headings, contraste em blocos bege
11. **Salvar** → `templates/pages/nome-descritivo.html`

### 3. Validação (Checklist)
Antes de entregar ao usuário, consulte o arquivo completo em `docs/checklist-entrega.md`.

**Verificações rápidas:**
- [ ] Apenas elementos do `<body>`?
- [ ] Sem `<style>` ou `<link>`?
- [ ] Comentários do storyboard preservados?
- [ ] `contenteditable="false"` removido (exceto H5P)?
- [ ] Textos em Capitalize (sem CAIXA ALTA)?
- [ ] Destaques verdes em `<span>` e fora de blocos bege?
- [ ] Blocos bege com `<strong>` em vez de `.vagalume-destaque`?
- [ ] `flow-root` no container se há floats?
- [ ] Imagens flutuantes com `<figure>` e `overflow: hidden`?
- [ ] H5P com `.h5p-placeholder`?
- [ ] Links com `.nomediaplugin`?
- [ ] Modais com IDs únicos?
- [ ] Imagens com `src=""`, `width`, `height`, `loading="lazy"`?
- [ ] Usou classes `.vagalume-` sempre que possível?

### 4. Entrega
- Arquivo HTML salvo em `templates/pages/`
- Se houver novas imagens: salvar em `assets/images/(capas|ilustracoes|personagens)/`
- Se criar novo componente: registrar em `components-library.md`

## Tratamento de Erros Comuns

### storedfileproblem
**Causa**: Caminho inválido em `src` de imagem, tag `<style>` no HTML, ou link sem `.nomediaplugin`.
**Solução**: Garantir `src=""` para placeholders, remover qualquer `<style>` e adicionar `.nomediaplugin` em links.

### Quebra de layout
**Causa**: Uso de classes CSS não existentes no tema Trema.
**Solução**: Usar apenas classes Bootstrap 4 nativas ou classes `.vagalume-`.

### Vazamento de float
**Causa**: Container sem `flow-root` e blocos coloridos sem encapsulamento.
**Solução**: Adicionar `style="display: flow-root;"` no container e encapsular blocos bege em `<div class="card border-0 bg-transparent">`.

### H5P não redimensiona
**Causa**: Uso de iframe manual ou `embed-responsive` em vez do placeholder nativo.
**Solução**: Substituir por `<div class="h5p-placeholder" contenteditable="false">[LINK]</div>`.

## Convenções

### Nomenclatura de Arquivos
- **Páginas**: `modulo-NN-titulo-descritivo.html`
- **Componentes**: `componente-nome.html`
- **Storyboards**: `modulo-NN-storyboard.md`
- **Imagens**: `modulo-NN-descritivo.png`

### Imagens
- Formatos: Apenas PNG e JPEG
- Atributos obrigatórios: `width`, `height`, `loading="lazy"`
- Placeholder: `src=""`
- Flutuantes: `<figure>` com `border-radius: 8px; overflow: hidden;`
- Organização: `assets/images/capas/`, `assets/images/ilustracoes/`, `assets/images/personagens/`
