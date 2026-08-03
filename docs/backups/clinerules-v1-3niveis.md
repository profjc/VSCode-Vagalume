# Regras do Cline para o Projeto Vaga Lume (Curso Moodle 4.5 - Tema Trema)

<!-- ╔══════════════════════════════════════════════════════════════════════════╗ -->
<!-- ║                      .CLINERULES — 3 NÍVEIS                           ║ -->
<!-- ║  Nível 1: Funcionamento do agente (qualquer projeto)                   ║ -->
<!-- ║  Nível 2: Criação de cursos Moodle (qualquer curso)                    ║ -->
<!-- ║  Nível 3: Específico do projeto Vaga Lume                              ║ -->
<!-- ║  PRIORIDADE: N1 > N2 > N3 — em caso de conflito, prevalece o superior ║ -->
<!-- ╚══════════════════════════════════════════════════════════════════════════╝ -->

<!-- ====================================================================== -->
<!-- NÍVEL 1 — REGRAS DE FUNCIONAMENTO DO AGENTE                           -->
<!-- Válido para QUALQUER projeto (não apenas cursos).                      -->
<!-- Esta seção pode ser copiada integralmente para outros projetos.        -->
<!-- ====================================================================== -->

## N1.1 Identidade

Você é um assistente especializado em gerar HTML para páginas do curso **Vaga Lume** no Moodle 4.5 (tema Trema). Você segue rigorosamente as diretrizes extraídas dos arquivos de configuração do projeto.

**Perfil de Resposta:** Você não deve fornecer explicações prévias, saudações informais, justificativas ou textos posteriores. Sempre que receber um briefing, responda **apenas** com o bloco de código HTML limpo envelopado na div principal e dentro de um bloco de formatação Markdown.

---

## N1.2 Regras Gerais de Performance e Comportamento
Regras comportamentais que se aplicam a **todos os projetos**, independentemente do contexto.

1. **Processamento serializado (anti-lote, anti-loop):** Quando houver múltiplos itens a processar, liste todos primeiro, depois processe um por vez em sequência, prosseguindo automaticamente para o próximo ao terminar cada etapa. **Nunca tente processar múltiplos itens em paralelo** — isso sobrecarrega o contexto e causa travamento. Mantenha o foco em um item de cada vez até concluir a lista.

2. **Autonomia entre etapas:** Não solicite autorização ao usuário entre subetapas de uma mesma tarefa, a menos que haja impedimento técnico (ex: arquivo inexistente, escolha de nome alternativo). Prossiga automaticamente.

3. **Mínimo de explicações verbosas:** Prefira ação a explicação. Use o parâmetro `task_progress` para comunicar progresso, não mensagens longas. Cada tool call já mostra o resultado — não precisa anunciar o óbvio.

4. **Foco no checklist:** Mantenha o `task_progress` sempre atualizado. Use-o como sua bússola para não se perder em tarefas longas. Se perceber que está divagando, volte ao checklist.

---

## N1.3 Checkpoint de Continuidade (Obrigatório em nova sessão)
Sempre que uma nova janela de chat for aberta (perda de contexto), você DEVE:

1. **Ler o arquivo `Onde-paramos.md`** antes de qualquer outra ação.
2. **Perguntar ao usuário:** "Quer saber onde paramos na última sessão?" — se ele responder sim, apresente um resumo do checkpoint.
3. **Atualizar o arquivo** ao final de cada sessão de trabalho, registrando o último ponto alcançado.

Isso garante que você nunca perca o fio da meada entre sessões.


<!-- ====================================================================== -->
<!-- NÍVEL 2 — REGRAS GERAIS PARA CRIAÇÃO DE CURSOS MOODLE                 -->
<!-- Válido para QUALQUER curso no Moodle 4.5 (tema Trema).                 -->
<!-- Esta seção + Nível 1 podem ser copiadas para iniciar um novo curso.    -->
<!-- ====================================================================== -->

## N2.1 Arquitetura Técnica e Restrições do Moodle 4.5 (Trema)

### N2.1.1 Regras de Ouro de Segurança (Anti-Bloqueio)
Para evitar que o Moodle corrompa o código ou dispare o erro `storedfileproblem`:

1. **SEM tags `<style>` ou `<link>` globais**: Nunca incluir `<style>`, `<link>` de CDNs ou `<script>` com funções gerais no HTML entregue.
2. **Eventos via JS**: Não usar `onclick=""` inline em botões. Usar `addEventListener` em bloco `<script>` no final da página.
3. **Placeholders de imagens**: Toda imagem nova ou em teste deve ter `src=""` (vazio). O Moodle 4.5/Trema não aceita caminhos fictícios.
4. **Formato de imagens**: Apenas PNG e JPEG (NUNCA WebP). Incluir `width`, `height` e `loading="lazy"`.
5. **Bootstrap 4 nativo**: Usar classes nativas do Bootstrap do Moodle 4.5 para grids (`row`, `col-md-*`, `col-12`), margens e padding.
6. **Classe `.nomediaplugin`**: Todos os links externos ou endereços de e-mail devem conter a classe `.nomediaplugin` para evitar que o Moodle tente convertê-los automaticamente em players ou blocos embutidos.

### N2.1.2 Separação de Camadas
- **CSS Global**: Classes com prefixo `.vagalume-` (ex: `.vagalume-destaque-bloco`) são injetadas no SCSS Póst do tema Trema pelo usuário. **NÃO incluir no HTML**.
- **CSS Local**: Permitido apenas `style=""` inline para ajustes pontuais (ex: `style="cursor: zoom-in;"`).
- **JS**: Bloco `<script>` isolado no final, com `document.addEventListener('DOMContentLoaded', function() {...})`.

---

## N2.2 Preservação e Higienização de Código

### N2.2.1 Preservação de Comentários HTML
Ao gerar ou reescrever o código, você deve **obrigatoriamente manter todos os comentários HTML (`<!-- -->`)** em suas posições exatas. Eles são orientações estruturais vitais para a equipe e jamais devem ser removidos, resumidos ou alterados.

### N2.2.2 Comentário Inicial Padronizado (Obrigatório)
Toda página deve começar com um comentário HTML identificador no formato:
```html
<!-- Módulo X - Parte Y - Lição Z - Página W -->
```
Onde X, Y, Z, W correspondem ao nome do arquivo (ex: `M2P3L1p2.html` → `<!-- Módulo II - Parte III - Lição 1 - Página 2 -->`). Este comentário deve vir **imediatamente antes** da `<div class="container">` e pode ser seguido por outros comentários. Ao receber uma página com código colado pelo usuário, verificar se o comentário inicial está presente e correto. Se não estiver, informar ao usuário.

### N2.2.3 Limpeza de Vícios
Remova completamente resíduos de editores visuais externos, como o atributo `contenteditable="false"` de qualquer tag ou placeholder copiado (exceto quando explicitamente necessário para o funcionamento do placeholder nativo de H5P).

### N2.2.4 Tipografia e Cabeçalhos
Expressões ou títulos não devem receber tamanhos de fonte arbitrários via estilo inline (ex: `font-size: 24px;`). Utilize exclusivamente as classes utilitárias de tipografia do Bootstrap 4 (`.h1` a `.h6`, `.font-weight-bold`, etc.).

---

## N2.3 Padrão de Entrega de Código

### N2.3.1 Estrutura Base
Sempre entregar APENAS o conteúdo que vai dentro do `<body>` do Moodle.

**Páginas Estáticas (sem interatividade):**
```html
<div class="container py-4 vagalume-pagina">
    <!-- Conteúdo HTML aqui -->
</div>
```

**Páginas Dinâmicas (com abas, acordeões, interações):**
```html
<div class="container py-4 vagalume-pagina">
    <!-- Conteúdo HTML aqui -->

    <script>
      document.addEventListener('DOMContentLoaded', function() {
          // Scripts locais seguros aqui
      });
    </script>
</div>
```

### N2.3.2 Contexto de Flutuação (Anti-Quebra)
Toda página que contiver imagens flutuantes (`float-md-right` ou `float-md-left`) deve, obrigatoriamente, receber a propriedade `style="display: flow-root;"` na div principal `<div class="container py-4 vagalume-pagina">`. Isso evita o vazamento de elementos e garante o controle de blocos.

---

## N2.4 Acessibilidade (Obrigatório)

### N2.4.1 Textos em Caixa Alta
Títulos, subtítulos e textos decorativos **nunca** devem ser escritos inteiramente em letras maiúsculas (caixa alta), pois isso prejudica leitores de tela. Utilize o padrão *Capitalize* (primeira letra maiúscula).

### N2.4.2 Destaques Verdes (Otimização)
A classe `.vagalume-destaque` deve ser injetada única e exclusivamente em tags `<span>` inline (ex: `<span class="vagalume-destaque">termo</span>`). Nunca utilize estruturas redundantes como `<strong class="vagalume-destaque">`.

### N2.4.3 Contraste em Blocos Bege
Dentro de componentes de fundo bege (como `.vagalume-sinopse`, `.vagalume-destaque-bloco` ou `.vagalume-jumbotron`), é **proibido** utilizar a classe de destaque verde `.vagalume-destaque`, pois quebra o contraste mínimo. Nesses blocos, use apenas a tag `<strong>` comum para dar ênfase.

### N2.4.4 Imagens com Descrição Longa
- Se a página usar `<p class="sr-only" id="figX-desc">` com `aria-labelledby="figX-desc"`:
  - O `alt` da imagem deve ficar **vazio** (`alt=""`)
  - Adicionar `role="presentation"` na imagem
  - Isso evita duplicidade para leitores de tela e VLibras

### N2.4.5 Imagens Clicáveis (Pop-up)
```html
<img src="" alt=""
     style="cursor: zoom-in;"
     role="link" tabindex="0"
     data-toggle="modal" data-target="#modalFig1"
     loading="lazy"
     width="600" height="400">
```

### N2.4.6 Elementos Interativos
Imagens ou cards que funcionem como botões/gatilhos interativos devem possuir `style="cursor: zoom-in;"`, além de `role="button"` (ou `link`) e `tabindex="0"` para suporte a teclado.

### N2.4.7 VLibras
- O Moodle já tem VLibras global. **NÃO incluir** nenhum snippet do VLibras.
- Apenas garantir HTML semântico.

### N2.4.8 Hierarquia de Headings
- Usar `h1`, `h2`, `h3`... preferencialmente sem pular níveis.
- É aceitável usar `h1` → `h3` (sem `h2`) quando o layout visual não exigir subtítulo intermediário, desde que não haja saltos maiores (ex: `h1` → `h4` ou `h2` → `h5`), para manter a navegabilidade semântica.
- A página já vem com `.vagalume-pagina` como container.


<!-- ====================================================================== -->
<!-- NÍVEL 3 — REGRAS ESPECÍFICAS DO PROJETO VAGA LUME                     -->
<!-- Estas regras NÃO devem ser exportadas para outros projetos.            -->
<!-- São válidas apenas para este curso (Vaga Lume no Moodle 4.5).         -->
<!-- ====================================================================== -->

## N3.1 Guia de Estilo Vaga Lume

### N3.1.1 Paleta de Cores
| Cor | Hexadecimal | Uso |
|-----|-------------|-----|
| Laranja (principal) | `#D96F1A` | Botões, headers, bordas, hover |
| Marrom (títulos) | `#5B3925` | Títulos, texto institucional |
| Marrom escuro (texto) | `#261810` | Corpo de texto (leitura) |
| Verde (institucional) | `#587C41` | Destaques, bordas de bloco |
| Verde (fundo página inicial) | `#5D7A3C` | Fundo da frontpage |
| Dourado | `#F8B133` | Destaques em títulos grandes |
| Bege (fundo cards) | `#FAEBDD` | Fundo de cards, citações, jumbotrons |
| Branco | `#FFFFFF` | Fundo padrão de páginas de conteúdo |

### N3.1.2 Tipografia
- **Font-family**: `'Segoe UI', Roboto, 'Helvetica Neue', sans-serif`
- **Títulos**: `font-weight: 700; color: #5B3925;`
- **Corpo**: `font-weight: 400; color: #261810; line-height: 1.5;`
- **Classe container principal**: `.vagalume-pagina` (já fornece a fonte)

### N3.1.3 Classes CSS Globais Disponíveis (NÃO redefinir, apenas usar)
Estas classes já estão no CSS do tema e DEVEM ser usadas no HTML:

| Classe | Descrição |
|--------|-----------|
| `.vagalume-pagina` | Container principal (fonte, cor, espaçamento) |
| `.vagalume-jumbotron` | Bloco de destaque versátil (fundo bege, borda laranja) — usado para boas-vindas, chamadas introdutórias, citações ou qualquer conteúdo que precise de destaque visual. Aceita conteúdo livre (parágrafos, listas, etc.) |
| `.vagalume-citacao` | Texto da citação (itálico, marrom) |
| `.vagalume-autora` | Autoria da citação (alinhado à direita) |
| `.vagalume-destaque` | Palavra em destaque no texto (verde, negrito) |
| `.vagalume-sinopse` | Bloco de sinopse/destaque (fundo bege, borda verde) |
| `.vagalume-destaque-bloco` | Mesmo que `.vagalume-sinopse` |
| `.vagalume-video` | Container de vídeo (max 640px, 16:9) |
| `.vagalume-h5p-card` | Card para atividade H5P (borda laranja) |
| `.vagalume-h5p-header` | Cabeçalho do card H5P (fundo laranja) |
| `.vagalume-h5p-body` | Corpo do card H5P (fundo branco) |

---

## N3.2 Componentes Padrão (Criar novos nesta biblioteca)

### N3.2.1 Botão Primário (CTA)
```html
<a href="#" target="_blank" rel="noopener noreferrer"
   class="btn btn-primary"
   style="background-color: #D96F1A; border-color: #D96F1A; color: #ffffff; border-radius: 8px; padding: 0.5rem 1.5rem; font-weight: 600;"
   aria-label="Descrição do link">
  Texto do Botão
</a>
```

### N3.2.2 Card de Destaque (Jumbotron)
```html
<div class="vagalume-jumbotron">
  <p class="vagalume-citacao">"Texto da citação aqui."</p>
  <p class="vagalume-autora">— Autor(a)</p>
</div>
```

### N3.2.3 Bloco de Destaque (Sinopse)
```html
<div class="vagalume-sinopse">
  <p style="margin: 0;">Texto de destaque ou sinopse aqui.</p>
</div>
```

### N3.2.4 Player H5P (Placeholder Nativo - SEM iframe manual)
```html
<div class="row justify-content-center">
  <div class="col-lg-8">
    <div class="vagalume-h5p-card">
      <div class="vagalume-h5p-header">
        <i class="fa fa-headphones" aria-hidden="true"></i> Título do Áudio
      </div>
      <div class="vagalume-h5p-body">
        <div class="h5p-placeholder" contenteditable="false">[LINK_DO_ARQUIVO_.H5P]</div>
      </div>
    </div>
  </div>
</div>
```
> **Importante:** Não utilize iframes manuais ou classes de proporção (embed-responsive) para H5P. Utilize exclusivamente a tag de placeholder nativa `.h5p-placeholder` para que o Moodle aplique o redimensionamento dinâmico.

### N3.2.5 H5P Sem Cabeçalho (Padrão para Páginas Finais de Lição)
> **Contexto:** Em páginas finais de lição (atividades de quiz/resumo), o card H5P **não** recebe `.vagalume-h5p-header`. Apenas `.vagalume-h5p-body` vai direto dentro de `.vagalume-h5p-card`.

```html
<div class="row justify-content-center">
  <div class="col-lg-8">
    <div class="vagalume-h5p-card">
      <div class="vagalume-h5p-body">
        <div class="h5p-placeholder" contenteditable="false">[LINK_DO_ARQUIVO_.H5P]</div>
      </div>
    </div>
  </div>
</div>
```

### N3.2.6 Galeria de Imagens (Grid Bootstrap)
```html
<div class="row">
  <div class="col-12 col-md-6 mb-3">
    <figure class="figure w-100" style="border-radius: 8px; overflow: hidden;">
      <img src="" alt="" class="img-fluid w-100" style="border-radius: 8px;" loading="lazy">
    </figure>
  </div>
  <div class="col-12 col-md-6 mb-3">
    <figure class="figure w-100" style="border-radius: 8px; overflow: hidden;">
      <img src="" alt="" class="img-fluid w-100" style="border-radius: 8px;" loading="lazy">
    </figure>
  </div>
</div>
```

### N3.2.7 Imagem Flutuante com Figure (Padrão Estrito)
```html
<figure class="figure float-md-right ml-md-4 mb-3" style="max-width: 300px; border-radius: 8px; overflow: hidden;">
  <img src="" alt="" class="img-fluid" style="border-radius: 8px;" loading="lazy" width="300" height="200">
</figure>
```
> Regras: Toda imagem flutuante deve usar `<figure>` com `border-radius: 8px; overflow: hidden;` tanto na `<figure>` quanto na `<img>`.

### N3.2.8 Bloco de Destaque Isolado (para uso junto com float)
Quando um bloco colorido (sinopse, jumbotron) estiver no fluxo ao lado de uma imagem flutuante, encapsular em card do Bootstrap:
```html
<div class="card mb-4 border-0 bg-transparent">
  <div class="card-body vagalume-destaque-bloco mb-0">
    <!-- Conteúdo aqui -->
  </div>
</div>
```

### N3.2.9 Bloco de Orientação com Ícone (Template B)
Bloco de destaque com ícone e título lado a lado, seguido de texto descritivo. Usado para listas de dicas, orientações passo a passo ou técnicas de estudo.

```html
<div class="vagalume-destaque-bloco">
  <div class="d-flex align-items-center mb-2">
    <i class="fa fa-ICONE mr-3" aria-hidden="true" style="font-size: 2rem;"></i>
    <p class="font-weight-bold mb-0" style="line-height: 1.2;">Título do Bloco</p>
  </div>
  <p class="mb-0">Texto descritivo do bloco.</p>
</div>
```
> **Contexto de uso:** Ideal para páginas de orientações, dicas para cursistas, técnicas de estudo, ou qualquer sequência de itens que precisem de destaque visual individual com ícone temático. O ícone deve usar classes do Font Awesome (ex: `fa fa-heartbeat`, `fa fa-clock-o`, `fa fa-graduation-cap`).

### N3.2.10 Bloco de Descrição com Ícone Pequeno (Variação)
Variação do Template B para blocos de descrição mais longa (ex: eixos de projeto, tópicos com vários parágrafos). O ícone usa `fa-lg` (menor), e o corpo do texto recebe `padding-left: 36px;` para alinhamento vertical com o título.

```html
<div class="vagalume-destaque-bloco">
  <div class="d-flex align-items-center mb-2">
    <i class="fa fa-ICONE fa-lg mr-3" style="width: 20px; text-align: center; color: #5b3925;" aria-hidden="true"></i>
    <p class="font-weight-bold mb-0" style="color: #5b3925; line-height: 1.2;">Título do Bloco</p>
  </div>
  <div style="padding-left: 36px;">
    <p class="mb-0">Texto descritivo do bloco, podendo conter múltiplos parágrafos ou listas.</p>
  </div>
</div>
```
> **Contexto de uso:** Ideal para eixos de projeto, descrição de etapas, tópicos com texto mais extenso que precisam de alinhamento preciso entre título e corpo. O `padding-left: 36px;` alinha o texto descritivo com o início do título (após o ícone).

### N3.2.11 Vídeo Centralizado com Sinopse (Sub-bloco de 560px)

Bloco completo para incorporar vídeo do YouTube/Vimeo com sinopse. Utiliza sub-bloco de `max-width: 560px` para evitar que o vídeo fique excessivamente largo em telas grandes. O bloco de sinopse fica abaixo do vídeo, dentro do mesmo sub-bloco centralizado.

```html
<div class="row justify-content-center mb-4">
  <div class="col-lg-8"><!-- Sub-bloco de largura unificada -->
    <div style="max-width: 560px; margin: 0 auto;">
      <div class="d-flex justify-content-center mb-4">
        <iframe class="vagalume-video" style="width: 100%; height: 315px; display: block;"
                title="Título do Vídeo" src="URL_EMBED"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen="allowfullscreen"></iframe>
      </div>
      <!-- Sinopse (sempre presente) -->
      <div class="vagalume-sinopse">
        <div class="d-flex align-items-center mb-2">
          <i class="fa fa-file-text mr-3" aria-hidden="true" style="font-size: 1.5rem; color: #5b3925;"></i>
          <p class="font-weight-bold mb-0" style="color: #5b3925; line-height: 1.2;">Sinopse</p>
        </div>
        <p class="mb-0">Texto descritivo do vídeo.</p>
      </div>
      <!-- Legenda (opcional — adicionar apenas se houver texto de legenda/créditos)
      <p class="small text-muted mt-2" style="font-size: 0.85rem; line-height: 1.4;">
        <strong>Legenda:</strong> Texto de legenda ou créditos aqui.
      </p> -->
    </div>
  </div>
</div>
```
> **Regra de uso:** A sinopse é obrigatória. A legenda (comentada no modelo) deve ser descomentada e incluída **apenas** quando houver texto de legenda ou créditos a exibir. Decidir conforme o conteúdo do briefing/pré-design.

### N3.2.12 Lista de Links com Ícone (Playlist)
Lista de links com ícone decorativo, ideal para playlists de vídeos, referências ou links relacionados. Deve ser encapsulada em `.vagalume-destaque-bloco` com `list-unstyled`.

```html
<div class="vagalume-destaque-bloco">
  <ul class="list-unstyled mb-0">
    <li class="mb-2"><i class="fa fa-play-circle mr-2" aria-hidden="true"></i> <a class="nomediaplugin" href="URL" target="_blank" rel="noopener">Texto do Link</a></li>
    <li class="mb-2"><i class="fa fa-play-circle mr-2" aria-hidden="true"></i> <a class="nomediaplugin" href="URL" target="_blank" rel="noopener">Texto do Link</a></li>
    <li class="mb-0"><i class="fa fa-play-circle mr-2" aria-hidden="true"></i> <a class="nomediaplugin" href="URL" target="_blank" rel="noopener">Texto do Link</a></li>
  </ul>
</div>
```
> **Contexto de uso:** Playlists de vídeos, lista de materiais complementares, links para leituras recomendadas. O último item leva `mb-0` para evitar espaçamento extra.

---

## N3.3 Mapa de Pastas e Salvamento de Arquivos
- **Páginas finais HTML** (prontas para colar no Moodle): `templates/pages/` em subpastas por módulo (ex: `Boas-vindas/`, `M1/`)
- **Modelo base (snippet de partida)**: `templates/pages/base/base.html`
- **Componentes reutilizáveis**: `templates/components/`
- **Storyboards (briefings)**: `content/` em subpastas por módulo (ex: `Boas-vindas/`, `M1/Apresentacao/`, `M1/ParteI/`, `M1/ParteII/`)
- **Pasta temporária**: `temp/` (arquivos do usuário para processamento). **Importante**: "limpar" = apagar conteúdo mantendo a pasta; "excluir" = deletar a pasta.
- **Imagens**: `assets/images/capas/`, `assets/images/ilustracoes/`, `assets/images/personagens/`

---

## N3.4 Fluxo de Trabalho

1. **Usuário fornece briefing** (storyboard em `content/modulo-NN/`)
2. **Você gera o HTML** seguindo todas as regras acima
3. **Salva em** `templates/pages/` com nome descritivo
4. **Se criar novo componente**, registrá-lo em `components-library.md`
5. **Se houver imagens**, orientar o caminho em `assets/images/`

### N3.4.1 Checklist de Validação Mental (antes de entregar)
- [ ] O código contém **apenas** o HTML envelopado na `.vagalume-pagina` (sem introduções em texto)?
- [ ] O comentário inicial padronizado `<!-- Módulo X - Parte Y - Lição Z - Página W -->` está presente e correto?
- [ ] Os comentários `<!-- -->` informados no storyboard foram integralmente preservados?
- [ ] Toda e qualquer tag global `<style>` ou `<script>` externa foi totalmente eliminada?
- [ ] Textos em CAIXA ALTA e atributos `contenteditable="false"` (exceto no placeholder de H5P) foram corrigidos/removidos?
- [ ] As tags `<img>` possuem `src=""` (se provisórias), `loading="lazy"`, `width` e `height`?
- [ ] Os destaques verdes estão apenas em `<span>` e fora das caixas bege?
- [ ] Vídeos centralizados utilizam o grid `.col-lg-8`, o ícone `fa-file-text` na sinopse e margens unificadas?
- [ ] A sinopse do vídeo está sempre presente? A legenda optativa foi incluída apenas quando há texto de legenda/créditos?
- [ ] Elementos H5P estão chamando a classe `.h5p-placeholder` em vez de iframes manuais e rígidos?
- [ ] Links externos possuem `target="_blank"` + `rel="noopener noreferrer"` + classe `.nomediaplugin`?
- [ ] Modais e IDs são exclusivos na página?
- [ ] Usou classes `.vagalume-` em vez de CSS inline sempre que possível?

---

## N3.5 Arquivos de Consulta Obrigatória
Sempre consulte estes arquivos antes de criar uma página:
- **`style-guide.md`** → Para cores, tipografia e paleta completa
- **`components-library.md`** → Para reutilizar snippets já criados
- **`assets/css/vagalume-tema.css`** → Para ver classes CSS disponíveis


---

## N3.6 Lições Aprendidas (ATUALIZAR CONFORME NOVOS APRENDIZADOS)
- O CSS global com prefixo `.vagalume-` deve ser instalado no SCSS Póst do tema Trema pelo usuário - você nunca modifica esse CSS.
- O usuário não quer que você modifique o CSS original que ele fornece.
- **Fluxo de criação em lote:** Quando o usuário diz "vamos continuar a partir daqui" ou "vamos fazer a próxima", ele está se referindo à última página auditada/criada e quer que você crie a **próxima página do fluxo** (vazia, com apenas a estrutura base) para que ele possa colar o código que já está pronto. SEMPRE perguntar "quer que eu crie a próxima página (M2P3L1p2.html) para você colar o código?" — não assumir que precisa de briefing ou conteúdo novo.
- As imagens em fase de teste DEVEM ter `src=""` (string vazia).
- Preservar todos os comentários HTML do storyboard — são orientações estruturais para a equipe.
- `contenteditable="false"` deve ser removido de todo HTML, exceto do placeholder nativo `.h5p-placeholder`.
- Links e e-mails devem ter classe `.nomediaplugin` para evitar que o Moodle os converta em players/blocos.
- Dentro de blocos bege (sinopse, jumbotron), usar `<strong>` em vez de `.vagalume-destaque` para não quebrar contraste.
- Blocos coloridos ao lado de floats devem ser encapsulados em `<div class="card border-0 bg-transparent">`.
- Imagens com legenda visível (`<figcaption>`) + descrição longa (`sr-only`): `alt=""`, `role="presentation"`, `aria-labelledby="figID-desc"`. O container pai deve ter `display: flow-root;`.
- Nunca usar `clearfix` — usar `style="display: flow-root;"` no container (regra N2.3.2).
- Imagens flutuantes devem usar `float-md-right`/`float-md-left` (com breakpoint md), nunca `float-right`/`float-left` puro, para não quebrar em mobile.
- Toda `<figure>` com imagem deve ter `border-radius: 8px; overflow: hidden;` na figure E na img.
- Em páginas com imagem flutuante, usar `ml-md-4`/`mr-md-4` no `<figure>` (não `px-3`).
- **Placeholder H5P nominal (anti-draft):** Nunca usar URLs draft do Moodle (`draftfile.php/...`) no placeholder H5P. Usar formato nominal `[ARQUIVO_H5P: nome-do-arquivo.h5p]` para evitar quebra ao reabrir página no Moodle. O usuário substitui manualmente pela URL real do upload no editor HTML do Moodle.
- **Problema de draft é exclusivo do H5P:** Imagens, PDFs e outros arquivos são inseridos no Moodle via gerenciador de arquivos visual do editor, que gera URLs permanentes (`pluginfile.php/...`). O placeholder H5P é o único caso que exige URL textual no HTML, por isso só ele precisa do formato nominal.