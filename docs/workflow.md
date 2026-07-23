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
2. **Adicionar conteúdo** → Textos, imagens (`src=""`), citações, H5P
3. **Aplicar classes** → `.vagalume-jumbotron`, `.vagalume-sinopse`, etc.
4. **Acessibilidade** → Descrições longas, imagem clicável, headings
5. **Salvar** → `templates/pages/nome-descritivo.html`

### 3. Validação (Checklist)
Antes de entregar ao usuário:
- [ ] Apenas elementos do `<body>`?
- [ ] Sem `<style>` ou `<link>`?
- [ ] Modais com IDs únicos?
- [ ] Imagens com `src=""`?
- [ ] Acessibilidade aplicada?
- [ ] Usou classes `.vagalume-`?

### 4. Entrega
- Arquivo HTML salvo em `templates/pages/`
- Se houver novas imagens: salvar em `assets/images/`
- Se criar novo componente: registrar em `components-library.md`

## Tratamento de Erros Comuns

### storedfileproblem
**Causa**: Caminho inválido em `src` de imagem ou tag `<style>` no HTML.
**Solução**: Garantir `src=""` para placeholders e remover qualquer `<style>`.

### Quebra de layout
**Causa**: Uso de classes CSS não existentes no tema Trema.
**Solução**: Usar apenas classes Bootstrap 4 nativas ou classes `.vagalume-`.

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
- Organização: `assets/images/capas/`, `assets/images/ilustracoes/`, `assets/images/personagens/`
