# Regras de Implementação HTML no Moodle 4.5 (Tema Trema)

<!-- ╔══════════════════════════════════════════════════════════════════════════╗ -->
<!-- ║  GAVETA DE CONSULTA SOB DEMANDA                                         ║ -->
<!-- ║  Origem: detalhamento das seções N2.1–N2.6 do .clinerules              ║ -->
<!-- ║  (migrado em 14/08/2026 na reestruturação em camadas).                  ║ -->
<!-- ║  O .clinerules (núcleo) referencia este arquivo quando necessário.      ║ -->
<!-- ╚══════════════════════════════════════════════════════════════════════════╝ -->

**Regra de uso:** consultar este arquivo ao gerar ou revisar qualquer página HTML. O núcleo `.clinerules` contém apenas as regras-chave; aqui estão os detalhes completos de implementação.

---

## 1. Arquitetura Técnica e Restrições do Moodle 4.5 (Trema)

### 1.1 Regras de Ouro de Segurança (Anti-Bloqueio)
Para evitar que o Moodle corrompa o código ou dispare o erro `storedfileproblem`:

1. **SEM tags `<style>`, `<link>` ou `<script>` globais**: Nunca incluir `<style>` ou `<link>` de CDNs no HTML entregue. `<script>` apenas quando estritamente necessário para interação específica da página, sempre no final com `addEventListener`, mantendo o código leve e rápido. Páginas de leitura e apresentação de conteúdo são **estáticas por princípio** — não devem conter scripts de efeitos visuais (animações são nativas pelo CSS global do tema Trema).
2. **Eventos via JS**: Não usar `onclick=""` inline em botões. Usar `addEventListener` em bloco `<script>` no final da página.
3. **Placeholder de imagem via arquivo único no Moodle (solução definitiva para TinyMCE 4.5/Trema)**: O TinyMCE do Moodle 4.5/Trema **não aceita `src=""`** (não exibe marcador clicável) nem `@@PLUGINFILE@@` no `<img>` (rejeita como URL inválida). A solução válida é usar uma **imagem temporária com a URL fixa do placeholder único do Moodle** ao lado da imagem oficial a preencher, com marcador textual e comentários delimitando o bloco a ser apagado após o upload:

   ```
   PLACEHOLDER_TEMP_URL = https://vagalume.educagir.com.br/pluginfile.php/104/mod_resource/content/1/placeholder-800x600.jpeg
   ```

   ```
   <!-- ===== INÍCIO DA IMAGEM TEMPORÁRIA (APAGAR APÓS SUBIR A IMAGEM REAL) ===== -->
   <span style="display: inline-block; background-color: #ffcccc; color: #990000; font-weight: bold; padding: 2px 8px; border-radius: 4px; font-size: 12px; margin-bottom: 4px;">⚠️ APAGAR ESTE BLOCO</span><br>
   <img src="PLACEHOLDER_TEMP_URL" alt="Upload temporario no TinyMCE" width="40" height="40" style="border-radius: 4px; flex-shrink: 0;"><br>
   <!-- ===== FIM DA IMAGEM TEMPORÁRIA ===== -->
   ```

   **Fluxo de uso no Moodle:** colar HTML → clicar na imagem temporária (o Moodle reconhece o arquivo único já existente no servidor, sem criar duplicatas) → o TinyMCE abre o gerenciador de arquivos → selecionar o arquivo real → o Tiny substitui o `src` da imagem temporária pelo `pluginfile.php` real → **copiar o `src` gerado** (via botão `<>` Exibir HTML) → **colar no `src="[cole a imagem aqui]"` da imagem oficial** ao lado → **apagar o bloco temporário** (do marcador "⚠️ APAGAR ESTE BLOCO" até o comentário `FIM`, localizável via Ctrl+F "APAGAR"). A imagem oficial mantém `alt` descritivo, dimensões, `sr-only` e `style` de exibição intactos — sem diálogo de descrição forçado, sem URL inválida, sem redimensionamento indevido. **IMPORTANTE:** usar SEMPRE a mesma URL fixa do placeholder único (nunca data URI variável) para evitar acúmulo de drafts temporários no servidor.
4. **Formato de imagens**: Apenas PNG e JPEG (NUNCA WebP). Incluir `width`, `height` e `loading="lazy"`. Exceção: imagens em galerias fluidas com `img-fluid w-100` podem omitir `width`/`height`, mantendo `alt` e `loading="lazy"` para acessibilidade.
5. **Bootstrap 4 nativo e Font Awesome**: Usar classes nativas do Bootstrap do Moodle 4.5 para grids (`row`, `col-md-*`, `col-12`), margens e padding. Ícones via Font Awesome do tema Trema (classes `fa-*`).
6. **Classe `.nomediaplugin`**: Todos os links externos ou endereços de e-mail devem conter a classe `.nomediaplugin` para evitar que o Moodle tente convertê-los automaticamente em players ou blocos embutidos. Ver seção 6 (Links Externos).
7. **Vídeo com embed não autorizado pelo YouTube (01/09/2026)**: Antes de gerar uma página com vídeo, verificar se o `iframe` de embed funciona para aquele vídeo. Quando o embed NÃO é autorizado, usar o padrão de **thumbnail + botão**: container centralizado (max-width 560px), imagem de thumbnail do projeto (`assets/images/ilustracoes/...`, NUNCA `draftfile`), botão de texto "Assistir no YouTube" sobreposto e centralizado (fundo `#D96F1A`, texto branco, link `nomediaplugin` + `target="_blank"` + `rel="noopener noreferrer"`, `aria-label` completo) e legenda de créditos abaixo com ":" (sem "|"). A imagem segue o padrão canônico do placeholder (bloco "⚠️ APAGAR ESTE BLOCO — INÍCIO/FIM" delimitando APENAS o placeholder clicável + imagem oficial `src="[cole a imagem aqui]"` fora do bloco). Precedente: "O que é Parentalidade" (M1P4L1p2).

### 1.2 Separação de Camadas
- **CSS Global**: Classes com prefixo `.vagalume-` são definidas no CSS global do tema Trema (SCSS Póst, injetado pelo usuário). **NÃO incluir as definições destas classes no HTML** (nem `<style>`, nem `<link>`). Usar as classes livremente nos elementos, e usar classes Bootstrap nativas para o restante do layout.
- **CSS Local**: Permitido apenas `style=""` inline para ajustes pontuais (ex: `style="cursor: zoom-in;"`).
- **JS**: Bloco `<script>` isolado no final, com `document.addEventListener('DOMContentLoaded', function() {...})`.

---

## 2. Preservação e Higienização de Código

### 2.1 Preservação de Comentários HTML
Ao gerar ou reescrever o código, você deve **obrigatoriamente manter todos os comentários HTML (`<!-- -->`)** em suas posições exatas. Eles são orientações estruturais vitais para a equipe e jamais devem ser removidos, resumidos ou alterados.

### 2.2 Comentários de Abertura, Fechamento e Internos (Obrigatório)
Toda página deve começar com um comentário HTML identificador de ABERTURA no formato:
```html
<!-- Módulo X - Parte Y - Lição Z - Página W -->
```
E terminar com um comentário de FECHAMENTO:
```html
<!-- FIM: Módulo X - Parte Y - Lição Z - Página W -->
```
Onde X, Y, Z, W correspondem ao nome do arquivo (ex: `M2P3L1p2.html` → `<!-- Módulo 2 - Parte 3 - Lição 1 - Página 2 -->`). A sequência **Lição Z é opcional** — deve ser usada apenas quando a página pertence a uma lição. Páginas de síntese e referências (que têm Parte mas não Lição) usam apenas `Módulo X - Parte Y - [título descritivo]` (ex: `M1P5P1.html` → `<!-- Módulo 1 - Parte 5 - O que aprendemos no Módulo 1 -->`). **Páginas de fórum** usam o formato `Módulo X - Parte Y - Fórum Z - [título completo da página]`, onde `Fórum Z -` é o identificador do tipo de atividade (análogo a `Lição Z -`) e o título completo entra em seguida, incluindo o prefixo `Fórum: ` se o título da página o tiver (ex: `M2P1F1.html` → `<!-- Módulo 2 - Parte 1 - Fórum 1 - Fórum: Quando começa a história de um leitor ou leitora? -->`). Confirmado em 08/08/2026. O comentário de abertura deve vir **imediatamente antes** da `<div class="container py-4 vagalume-pagina">`; o de fechamento após o `</div>` final da container. Entre eles, manter todos os comentários internos de seção fornecidos pelo storyboard — são boas práticas de documentação de código. Ao receber uma página com código colado pelo usuário, verificar se os comentários de abertura e fechamento estão presentes e corretos. Se não estiverem, informar ao usuário.

**Título da página nos comentários (opcional):** Se houver título para a página (mesmo que não entre no HTML, pois é inserido pelo usuário diretamente no Moodle), incluí-lo nos comentários de abertura e fechamento para facilitar a localização (ex: `<!-- Módulo 2 - Parte 1 - Lição 1 - Página 1 - Quando começamos a ler? -->`). Se **não houver** título, o DI **deve lembrar o usuário** disso no planejamento da página e aguardar confirmação: se fica apenas com a numeração ou se terá algum título.

### 2.3 Limpeza de Vícios
Remova completamente resíduos de editores visuais externos, como o atributo `contenteditable="false"` de qualquer tag ou placeholder copiado (exceto quando explicitamente necessário para o funcionamento do placeholder nativo de H5P).

### 2.4 Tipografia e Cabeçalhos
Expressões ou títulos não devem receber tamanhos de fonte arbitrários via estilo inline (ex: `font-size: 24px;`). Utilize exclusivamente as classes utilitárias de tipografia do Bootstrap 4 (`.h1` a `.h6`, `.font-weight-bold`, etc.).

### 2.5 Comportamento do TinyMCE no Moodle 4.5
O TinyMCE do Moodle 4.5 tem comportamentos específicos que DEVEM ser considerados ao gerar HTML:

1. **Ícones Font Awesome estão seguros**: O TinyMCE NÃO sobrescreve `class` ou `style` de elementos `<i>`. Portanto, `<i class="fa fa-ICONE" style="...">` pode ser usado sem risco.
2. **Imagens podem ser alteradas**: O TinyMCE PODE sobrescrever `class` e `style` de `<img>`. Para elementos que dependem de tamanho fixo (como figuras em layout de float), encapsular a `<img>` dentro de uma `<div>` ou `<figure>` com `style` de tamanho no container, não na imagem.
3. **Ícones vazios em tabelas são removidos**: O TinyMCE remove elementos `<i>` vazios (sem conteúdo de texto) dentro de `<td>`. Se precisar de ícone em tabela, usar `<span class="fa fa-ICONE" aria-hidden="true">&nbsp;</span>` — o `&nbsp;` dá conteúdo ao elemento e o editor preserva.
4. **NUNCA gerar dois comentários HTML consecutivos**: O TinyMCE insere `<p>&nbsp;</p>` vazios indesejáveis entre comentários consecutivos. Sempre separar comentários por código HTML entre eles, ou fundir comentários consecutivos em um único bloco de comentário.

---

## 3. Padrão de Entrega de Código

### 3.1 Estrutura Base
Sempre entregar APENAS o conteúdo que vai dentro do `<body>` do Moodle. A página já vem com `.vagalume-pagina` como container principal.

**Títulos de página**: O usuário insere títulos (lição, página, atividade) diretamente no Moodle, onde tem acesso à configuração. Não incluir heading de título da página no HTML, a menos que o briefing explicite que a página precisa de um título próprio no corpo do conteúdo. Usar `h1`→`h3` apenas para headings de conteúdo dentro da página.

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

### 3.2 Contexto de Flutuação (Anti-Quebra)
Toda página que contiver imagens flutuantes (`float-md-right` ou `float-md-left`) deve, obrigatoriamente, receber a propriedade `style="display: flow-root;"` na div principal `<div class="container py-4 vagalume-pagina">`. Isso evita o vazamento de elementos e garante o controle de blocos.

---

## 4. Acessibilidade (Obrigatório)

### 4.1 Responsividade Mobile-First
Use sempre classes de grid Bootstrap (`col-12`, `col-md-*`, etc.) partindo do menor dispositivo. Toda página deve ser projetada para funcionar em telas de 320px. Teste mentalmente o layout em mobile antes de gerar.

### 4.2 Leitores de Tela
- Todo elemento não textual (ícones, imagens decorativas) deve ter `aria-hidden="true"` ou `aria-label` descrevendo seu propósito.
- Ícones puramente decorativos usam `aria-hidden="true"`; ícones informativos usam texto descritivo.
- Links e botões devem ter texto descritivo — nunca use apenas "clique aqui".
- Mantenha uma hierarquia lógica de headings (ver 4.10).

### 4.3 Contraste Mínimo
Garanta que a relação de contraste entre texto e fundo atenda no mínimo **4.5:1** para texto normal. Use as cores da paleta já aprovadas no `style-guide.md` (ver N3.1.1 do núcleo). Para elementos específicos do projeto Vagalume, ver 4.5 (blocos bege).

### 4.4 Textos em Caixa Alta
Títulos, subtítulos e textos decorativos **nunca** devem ser escritos inteiramente em letras maiúsculas (caixa alta), pois isso prejudica leitores de tela. Utilize o padrão *Capitalize* (primeira letra maiúscula).

### 4.5 Destaques Verdes (Otimização)
A classe `.vagalume-destaque` deve ser injetada única e exclusivamente em tags `<span>` inline (ex: `<span class="vagalume-destaque">termo</span>`). Nunca utilize estruturas redundantes como `<strong class="vagalume-destaque">`.

### 4.6 Contraste em Blocos Bege
Dentro de componentes de fundo bege (como `.vagalume-sinopse`, `.vagalume-destaque-bloco` ou `.vagalume-jumbotron`), é **proibido** utilizar a classe de destaque verde `.vagalume-destaque`, pois quebra o contraste mínimo. Nesses blocos, use apenas a tag `<strong>` comum para dar ênfase.

### 4.7 Imagens com Descrição Longa
- Se a página usar `<p class="sr-only" id="figX-desc">` com `aria-labelledby="figX-desc"`:
  - O `alt` da imagem deve ficar **vazio** (`alt=""`)
  - Adicionar `role="presentation"` na imagem
  - Isso evita duplicidade para leitores de tela e VLibras

### 4.8 Imagens Clicáveis (Pop-up)
```html
<img src="" alt=""
     style="cursor: zoom-in;"
     role="link" tabindex="0"
     data-toggle="modal" data-target="#modalFig1"
     loading="lazy"
     width="600" height="400">
```

### 4.9 Elementos Interativos
Imagens ou cards que funcionem como botões/gatilhos interativos devem possuir `style="cursor: zoom-in;"`, além de `role="button"` (ou `link`) e `tabindex="0"` para suporte a teclado.

### 4.10 VLibras
- O Moodle já tem VLibras global. **NÃO incluir** nenhum snippet do VLibras.
- Apenas garantir HTML semântico e acessível para que o widget global funcione (headings corretos, aria-label, sr-only).

### 4.11 Hierarquia de Headings
- Usar `h1`, `h2`, `h3`... preferencialmente sem pular níveis.
- É aceitável usar `h1` → `h3` (sem `h2`) quando o layout visual não exigir subtítulo intermediário, desde que não haja saltos maiores (ex: `h1` → `h4` ou `h2` → `h5`), para manter a navegabilidade semântica.

### 4.12 Verificação de Acessibilidade Obrigatória em TODAS as Páginas (10/08/2026)
Toda página **gerada futuramente** ou **revisada** deve passar pela verificação de acessibilidade, com os ajustes corretamente indicados e feitos desde o início — não como correção posterior. Itens obrigatórios:
- **Descrição longa de imagens** no padrão 4.7: `<p class="sr-only" id="figX-desc">` + `alt=""` na imagem + `role="presentation"` + `aria-labelledby="figX-desc"` — **sem duplicidade de leitura** (nunca `sr-only` **e** `alt` preenchidos ao mesmo tempo; nunca `<span class="sr-only">` ou `<div class="sr-only">` — usar sempre `<p class="sr-only" id="figX-desc">`).
- **Atributos completos de imagem** (item 1.1.4): `width`, `height` e `loading="lazy"` em todas as imagens.
- **Hierarquia de headings** (4.11), `aria-hidden="true"` em ícones decorativos, `title` acessível em vídeos, sem snippet VLibras (4.10).
- **Legendas de figuras** centralizadas (`figure-caption text-center mt-2`).
- Precedente: auditoria de acessibilidade do Módulo 2 (10/08/2026) — 36 páginas auditadas, 7 pendências corrigidas (padrão 4.7 + atributos de imagem).

### 4.13 Proibição do caractere "|" em títulos e legendas (13/08/2026)
O caractere **"|" (barra vertical) NUNCA deve ser usado** em títulos, legendas de vídeo, legendas de figuras ou qualquer texto visível — inclusive em páginas novas e revisões. Por razões de acessibilidade, o separador padrão entre blocos informativos é **":" (dois-pontos)**. Exemplo: `O que é Primeira Infância?: Canal: Fundação Maria Cecilia Souto Vidigal (YouTube): 01min29s`. Ao revisar páginas existentes, substituir todo "|" pelo padrão ":". Firmado em 13/08/2026 pelo mestre (regra permanente).

---

## 5. Fidelidade ao Texto do Autor

### 5.1 Texto do autor é intocável
Reproduza o texto do autor exatamente como está no conteúdo-fonte (`.docx` convertido para `.md`). NUNCA adicione formatação que o autor não colocou — isso inclui aspas, itálico (`<em>`), negrito extra (`<strong>`), marcações ou qualquer adornamento tipográfico. Se o texto-fonte não tem aspas, não coloque aspas. Se não está em itálico, não coloque em itálico. A única exceção é a formatação estrutural de componentes visuais (ex.: nome em negrito no cabeçalho do H5P, conforme o template do componente).

### 5.2 Instruções entre colchetes
Instruções entre colchetes no texto-base do autor DEVEM ser respeitadas literalmente. Ex.: `[Sem legenda]` significa NÃO incluir legenda ou texto abaixo da imagem. `[Inserir imagem X]` significa usar exatamente a imagem X. `[Fim de texto de capítulo]` delimita o escopo exato da página. Não invente conteúdo além do que está entre os marcadores de início/fim da seção.

### 5.3 Blocos meta [* ... *]
Blocos delimitados por `[*` e `*]` são instruções META e devem ser COMPLETAMENTE IGNORADOS na geração do HTML. Tudo que estiver entre `[*` e `*]` — seja em uma única linha ou abrangendo múltiplas linhas — é uma orientação interna para o DI (você) e NÃO faz parte do conteúdo visível da página. Exemplos:
- `[*Atividade: Será feita em outra página; não inserir nesta página]` → instrução curta em linha única.
- `[* ... Início da atividade ... template ... enunciado ... Fim da atividade *]` → bloco multilinha descrevendo uma atividade que será criada separadamente.

Sempre que encontrar `[*`, LOCALIZE o `*]` de fechamento correspondente, LEIA a instrução para entender o que fazer, mas NÃO INCLUA nenhum conteúdo desse bloco no HTML gerado. O conteúdo entre `[*` e `*]` é estritamente não renderizável.

### 5.4 Zero inércia criativa
Você auxilia como DI, mas NÃO é o autor do conteúdo. Nunca invente legendas, títulos, textos, ícones ou qualquer elemento que não esteja explicitamente solicitado no texto-base do autor. Se o autor não pediu, não coloque. O criativo é o autor; você implementa e, como DI, sugere estrutura — mas nunca inventa conteúdo.

### 5.5 Fluxo de trabalho com fonte .docx
O texto-base chega em `.docx` (documento do autor com instruções `[ ]` do designer inicial). Você converte para `.md` para trabalhar melhor. O arquivo `.md` é a versão de trabalho que contém o texto extraído e estruturado. O `.docx` é o original recebido do autor, mantido como backup/referência. Após converter, atue como DI: **pense** o storyboard (plano de trabalho) mentalmente e entregue a página HTML pronta — não criamos arquivos separados de storyboard.

### 5.6 Verificação de palavras em inglês/discrepantes (obrigatória no planejamento)
Ao revisar qualquer página, verificar **ativamente** se o texto contém **palavras escritas em inglês** ou termos que **divirjam do conteúdo original do autor** (ex: "memory" em vez de "memória", "protection" em vez de "proteção", espaçamentos indevidos). Caso encontre:
- se a **correção for evidente** (equivalente em português inequívoco no contexto), corrigir para o português e registrar a correção;
- se houver **dúvida** sobre a palavra correta, **reportar ao mestre** antes de alterar.
Isso garante a fidelidade ao texto do autor (5.1) de forma **ativa** durante o planejamento da página. Firmado em 09/08/2026 — precedentes: "memory" (M2P4L4p4) e "protection" (M2P5L1p1).

---

## 6. Links Externos
Todo link (`<a>`) externo ou endereço de e-mail deve seguir estas regras cumulativas:

1. **`target="_blank"`**: abrir em nova aba, exceto quando explicitamente solicitado que abra na mesma aba.
2. **`rel="noopener noreferrer"`**: segurança e privacidade.
3. **Classe `.nomediaplugin`**: evita que o Moodle tente converter o link automaticamente em player ou bloco embutido.

### 6.1 Estilização visual padrão dos links (22/08/2026)
Todo link externo deve ser visualmente **negrito + sublinhado + colorido**, destacando-se do texto comum. As classes/estilos seguem o contexto de fundo onde o link aparece:

- **Fundo branco** (texto comum / cards brancos): cor **laranja `#d96f1a`** — `class="nomediaplugin font-weight-bold" style="color: #d96f1a; text-decoration: underline;"` (contraste ~4,9:1 sobre branco).
- **Boxes/cards bege** (`vagalume-destaque-bloco`, `vagalume-sinopse`, `vagalume-jumbotron`, fundo `#faebdd`): cor **marrom `#5b3925`** — `class="nomediaplugin font-weight-bold" style="color: #5b3925; text-decoration: underline;"` (contraste ~8,8:1 sobre bege; laranja sobre bege reprova o mínimo de 4,5:1 — N2.4.3/4.6).

Exemplo (em box bege):
```html
<a class="nomediaplugin font-weight-bold" style="color: #5b3925; text-decoration: underline;" href="URL" target="_blank" rel="noopener noreferrer">Texto descritivo do link</a>
```

Firmado em 22/08/2026 — precedente: link da BBC na `M1P3L1p2.html` inicialmente entregue sem estilização; corrigido para o padrão marrom sobre bege.

---

## 7. Exemplo completo de link externo
```html
<a class="nomediaplugin font-weight-bold" style="color: #5b3925; text-decoration: underline;" href="URL" target="_blank" rel="noopener noreferrer">Texto descritivo do link</a>