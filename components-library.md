# 🧩 Biblioteca de Componentes - Vaga Lume

> Componentes HTML reutilizáveis para páginas do curso Moodle 4.5
> **Sempre usar dentro de:** `<div class="container py-4 vagalume-pagina">...</div>`

---

## 1. Botão Primário (CTA)

### Simples
```html
<a href="#" target="_blank" rel="noopener noreferrer"
   class="btn btn-primary"
   style="background-color: #D96F1A; border-color: #D96F1A; color: #ffffff; border-radius: 8px; padding: 0.5rem 1.5rem; font-weight: 600;"
   aria-label="Descrição do link">
  Texto do Botão
</a>
```

### Centralizado
```html
<div class="text-center">
  <a href="#" target="_blank" rel="noopener noreferrer"
     class="btn btn-primary"
     style="background-color: #D96F1A; border-color: #D96F1A; color: #ffffff; border-radius: 8px; padding: 0.5rem 1.5rem; font-weight: 600;"
     aria-label="Descrição do link">
    Texto do Botão
  </a>
</div>
```

---

## 2. Card de Destaque (Jumbotron)

```html
<div class="vagalume-jumbotron">
  <p class="vagalume-citacao">"Texto da citação aqui."</p>
  <p class="vagalume-autora">— Autor(a)</p>
</div>
```

---

## 3. Bloco de Destaque (Sinopse)

```html
<div class="vagalume-sinopse">
  <p style="margin: 0;">Texto de destaque ou sinopse aqui.</p>
</div>
```

---

## 4. Player H5P

### Áudio/Podcast
```html
<div class="vagalume-h5p-card">
  <div class="vagalume-h5p-header">
    <i class="fa fa-headphones" aria-hidden="true"></i> Título do Áudio
  </div>
  <div class="vagalume-h5p-body">
    <!-- Código H5P embed aqui -->
  </div>
</div>
```

### Vídeo
```html
<div class="vagalume-h5p-card">
  <div class="vagalume-h5p-header">
    <i class="fa fa-video-camera" aria-hidden="true"></i> Título do Vídeo
  </div>
  <div class="vagalume-h5p-body">
    <!-- Código H5P embed aqui -->
  </div>
</div>
```

### Quiz/Atividade
```html
<div class="vagalume-h5p-card">
  <div class="vagalume-h5p-header">
    <i class="fa fa-puzzle-piece" aria-hidden="true"></i> Título da Atividade
  </div>
  <div class="vagalume-h5p-body">
    <!-- Código H5P embed aqui -->
  </div>
</div>
```

---

## 5. Galeria de Imagens

### 2 colunas (desktop) / 1 coluna (mobile)
```html
<div class="row">
  <div class="col-12 col-md-6 mb-3">
    <figure class="figure w-100">
      <img src="" alt=""
           class="img-fluid w-100"
           style="border-radius: 16px;"
           loading="lazy">
    </figure>
  </div>
  <div class="col-12 col-md-6 mb-3">
    <figure class="figure w-100">
      <img src="" alt=""
           class="img-fluid w-100"
           style="border-radius: 16px;"
           loading="lazy">
    </figure>
  </div>
</div>
```

### 3 colunas (desktop)
```html
<div class="row">
  <div class="col-12 col-md-4 mb-3">
    <figure class="figure w-100">
      <img src="" alt=""
           class="img-fluid w-100"
           style="border-radius: 16px;"
           loading="lazy">
    </figure>
  </div>
  <div class="col-12 col-md-4 mb-3">
    <figure class="figure w-100">
      <img src="" alt=""
           class="img-fluid w-100"
           style="border-radius: 16px;"
           loading="lazy">
    </figure>
  </div>
  <div class="col-12 col-md-4 mb-3">
    <figure class="figure w-100">
      <img src="" alt=""
           class="img-fluid w-100"
           style="border-radius: 16px;"
           loading="lazy">
    </figure>
  </div>
</div>
```

---

## 6. Imagem Clicável (Modal Pop-up)

```html
<!-- Miniatura clicável -->
<img src="" alt=""
     style="cursor: zoom-in;"
     role="link" tabindex="0"
     data-toggle="modal" data-target="#modalFig1"
     loading="lazy"
     width="600" height="400">

<!-- Modal -->
<div class="modal fade" id="modalFig1" tabindex="-1" role="dialog" aria-labelledby="modalFig1Label" aria-hidden="true">
  <div class="modal-dialog modal-lg modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="modalFig1Label">Título da Imagem</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Fechar">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body text-center">
        <img src="" alt=""
             class="img-fluid"
             style="border-radius: 8px;"
             loading="lazy">
      </div>
    </div>
  </div>
</div>
```

---

## 7. Imagem com Descrição Longa (Acessibilidade)

```html
<p class="sr-only" id="fig1-desc">Descrição detalhada da imagem para leitores de tela.</p>

<img src="" alt=""
     role="presentation"
     aria-labelledby="fig1-desc"
     class="img-fluid w-100"
     style="border-radius: 16px;"
     loading="lazy"
     width="800" height="500">
```

---

## 8. Container de Vídeo

```html
<figure class="figure w-100">
  <div class="vagalume-video">
    <!-- Embed do vídeo (YouTube, Vimeo, etc.) -->
    <iframe src="" class="w-100 h-100" frameborder="0" allowfullscreen></iframe>
  </div>
</figure>
```

---

## 9. Título com Destaque

```html
<h1>Palavra <span class="vagalume-destaque">Destacada</span> no Texto</h1>
```

---

## 10. Texto com Destaque no Parágrafo

```html
<p>Este é um texto normal com uma <span class="vagalume-destaque">palavra em destaque</span> no meio do parágrafo.</p>
```

---

## 11. Aviso/Nota (utilizando sinopse)

```html
<div class="vagalume-sinopse">
  <p style="margin: 0;"><strong>💡 Importante:</strong> Texto do aviso ou nota aqui.</p>
</div>
```

---

## 12. Grid de Texto 2 Colunas

```html
<div class="row">
  <div class="col-12 col-md-6">
    <p>Texto da coluna esquerda...</p>
  </div>
  <div class="col-12 col-md-6">
    <p>Texto da coluna direita...</p>
  </div>
</div>
```

---

## Templates de Página

### Página de Conteúdo Padrão
```html
<div class="container py-4 vagalume-pagina">
  <h1>Título do Módulo</h1>

  <div class="vagalume-sinopse">
    <p style="margin: 0;">Descrição geral do conteúdo desta página.</p>
  </div>

  <!-- Conteúdo principal aqui -->

  <div class="vagalume-jumbotron">
    <p class="vagalume-citacao">"Citação de destaque."</p>
    <p class="vagalume-autora">— Autor(a)</p>
  </div>
</div>
```

---

> 📝 **Para adicionar novo componente:** Edite este arquivo seguindo o padrão dos exemplos acima.
