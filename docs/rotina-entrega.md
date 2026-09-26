# 📋 Rotina de Entrega — Projeto Vaga Lume

<!-- ╔══════════════════════════════════════════════════════════════════════════╗ -->
<!-- ║  ARQUIVO DE LEITURA OBRIGATÓRIA — N3.0 / N1.7                         ║ -->
<!-- ║  Criado em 24/09/2026 — precedente: erros recorrentes de nomeação,     ║ -->
<!-- ║  rotina entre sessões e entrega no chat que exigiam correção do        ║ -->
<!-- ║  mestre a cada ciclo. Consolida regras dispersas de lições aprendidas. ║ -->
<!-- ╚══════════════════════════════════════════════════════════════════════════╝ -->

> **Leitura obrigatória:** no início de TODA sessão (junto com `Onde-paramos.md`)
> e antes de TODA entrega no chat (ciclo concluído). Não é gaveta sob demanda (N3.4).

---

## §1 — Rotina de Ciclo (PLAN → ACT → entrega)

### 1.1 PLAN mode
- Ler briefing do DI + **confrontar com a página canônica real** do projeto (nunca reconstruir de memória).
- Consultar as gavetas exigidas pela tarefa (N3.4) — nunca ler todas por reflexo.
- Registrar o plano em `Onde-paramos.md`.
- **Nunca mutar arquivos em PLAN** (comandos incluídos) — aguardar ACT.

### 1.2 ACT mode
- **UMA página/arquivo por vez** — nunca em lote.
- Gerar o HTML fiel ao texto do autor (N2.5).
- **Validar contra `docs/checklist-entrega.md`** (todos os grupos: estrutural, higienização, identidade visual, acessibilidade, flutuação, funcionamento no Moodle).
- **`code -r <caminho>`** como ÚLTIMA ação (nunca seguido de atualizações de checkpoint ou outros comandos).
- **INTERROMPER** e aguardar validação do mestre no Moodle.

### 1.3 Entrega no chat
Assim que o ciclo terminar, fornecer o **quadro abaixo** (§3) com os nomes corretos para o Moodle.

---

## §2 — Tabela de Nomes no Moodle

> **Fonte única da verdade:** o nome configurado no Moodle é o "source of truth".
> O comentário HTML (`<!-- -->`) DEVE espelhar esse nome (N2.2.2).

| Tipo de página no Moodle | Nome a configurar | Exemplo |
|---|---|---|
| **Fórum** | `Compartilhando Ideias` (sempre — exceto fórum de Boas-vindas) | (não muda; a pergunta vai no título descritivo do HTML) |
| **Atividade H5P** | prefixo `Atividade:` seguido do título do autor | `Atividade: Pensando um espaço para as infâncias` |
| **Página de conteúdo** | título do autor, sem prefixo extra | `Livros ao alcance das mãozinhas` |
| **Abertura de módulo** | `Apresentação do Módulo N` (decimal, sem romano) | `Apresentação do Módulo 3` |
| **Síntese de módulo** | título descritivo sem "Lição" | `Síntese do Módulo 2` |
| **Referências** | `Referências Bibliográficas` | `Referências Bibliográficas` |
### Observações

- **Numeração sempre decimal** (Módulo 1, Parte 2, Lição 4, Página 3) — nunca romano (Módulo I).
- **Título do fórum no Moodle = `Compartilhando Ideias`** (fixo). O título descritivo ("Fórum: Olhando a Biblioteca Comunitária…") fica APENAS no HTML da página.
- **Atividade H5P começa com "Atividade:"** no nome da página do Moodle e no comentário HTML (N2.4.16).
- **Lições no Moodle** seguem o nome do autor no DI (ex.: "Um Ambiente que Acolhe as Infâncias").
- **Comentário HTML de abertura/fechamento** espelha o título do Moodle, não o nome do arquivo (N2.2.2).
- **Nunca dois comentários consecutivos** (`<!-- -->\n\n<!-- -->` sem HTML entre eles).
- **Título de card/caixa** dentro do HTML usa `<p class="font-weight-bold">` (herda cor do contexto). Exceção: "Para participar" do fórum (mantém `span.h5` + cor explícita).

---

## §3 — Template de Entrega no Chat

Ao finalizar cada ciclo, entregar um quadro como este:

    ### 📋 Página para o Moodle

    | Item | Valor |
    |------|-------|
    | **Nome da página (no Moodle)** | … |
    | **Lição a criar** (se houver) | … (omitir se a lição já existe) |
    | **Arquivo HTML** | `templates/pages/…/…html` |
    | **H5P placeholder** | `[ARQUIVO_H5P: …h5p]` (ou "Nenhum") |
    | **Observações** | posicionamento, colagens pendentes, etc. |

> **NÃO devolver o código HTML na janela do chat (26/09/2026 — decisão do mestre):** a entrega no chat é **apenas o quadro** acima (nome da página, lição, arquivo e H5P). O HTML fica no repositório e é aberto no VS Code com `code -r <caminho>` como **última ação do ACT**; o mestre copia direto do editor. Precedente: ciclo da página `M3P3L1p1` (26/09/2026).

---

## §4 — Checklist de Conferência Pré-Entrega

> Antes de postar o quadro acima no chat, verificar RAPIDAMENTE:

### Nomes (30s)
- [ ] **Nome da página no Moodle** confere com a tabela §2 (fórum = "Compartilhando Ideias", H5P = "Atividade:", etc.)
- [ ] **Comentário HTML** (`<!-- -->`) espelha o nome no Moodle
- [ ] **Nome da lição** (se houver) usa o título do autor no DI

### Código (2 min — contra checklist-entrega.md)
- [ ] **Estrutura e segurança**: sem `<html>`/`<head>`/`<body>`/`<style>`/`<link>`/`onclick`/CDN
- [ ] **Container**: `<div class="container py-4 vagalume-pagina">` (flow-root se houver float)
- [ ] **Acessibilidade**: `aria-hidden="true"` em ícones FA; `sr-only` com `<p>` (nunca `<span>`); hierarquia de headings; `width`/`height`/`loading="lazy"` em imagens; sem VLibras
- [ ] **Higienização**: FA5 (`fa fa-*`, nunca `fa-solid`); travessões `—` (nunca `--`/`–`); sem CAIXA ALTA; negritos herdam cor; title card = `p.font-weight-bold`
- [ ] **Funcionamento no Moodle**: `.h5p-placeholder` (não iframe); grid Bootstrap 4; links com `target="_blank"` + `rel="noopener noreferrer"` + `.nomediaplugin` + cor §6.1; vídeos com `col-lg-8`; legendas §4.14/§4.15
- [ ] **Último elemento**: `mb-0` no container final (S1)

### Procedimento (1 min)
- [ ] **Um arquivo por ciclo** — não lotei páginas
- [ ] **`code -r` foi a ÚLTIMA ação** (ou é N/A)
- [ ] **`Onde-paramos.md` atualizado** com o checkpoint
- [ ] **Fórum** (se pertence a uma Parte): é a última atividade da Parte (N3.5.3)
---

## §5 — Erros Já Cometidos (Consultar Rapidamente)

> Se envolver qualquer um destes tópicos, pare e confira antes de entregar.
> Consulte `docs/regras-licoes-aprendidas.md` para detalhes e precedentes.

| # | Tópico | Regra/Procedimento |
|---|---|---|
| 1 | **Nome do fórum no Moodle** | SEMPRE "Compartilhando Ideias" (exceto Boas-vindas). O título descritivo vai só no HTML. |
| 2 | **H5P** | Eu (agente) NUNCA edito `.h5p`. Só indico parte/lição/página + correção exata; mestre edita no Moodle e sincroniza. |
| 3 | **Renomeação de página com H5P** | Alinhar 4 elementos: (1) nome do HTML, (2) comentários `<!-- -->`, (3) arquivo `.h5p` em `assets/h5p/`, (4) placeholder no HTML. |
| 4 | **Placeholder de imagem** | Copiar o bloco real de `M2P4L3p1.html` (nunca reconstruir de cabeça). `src=""` vazio + quadradinho 40×40 + marcador "⚠️ APAGAR ESTE BLOCO" + imagem oficial. APENAS imagens (H5P/vídeos fora do padrão). |
| 5 | **Ícones FA5** | Sempre `fa fa-*` (nunca `fa-solid`, `fa-regular`, sintaxe FA6). |
| 6 | **Travessões** | No texto visível: travessão verdadeiro `—` (nunca `--` nem `–`). Hífen `-` só em comentários. |
| 7 | **Links externos** | Completos: `target="_blank"` + `rel="noopener noreferrer"` + `.nomediaplugin` + `font-weight-bold` + `color: #944b11` + `text-decoration: underline`. |
| 8 | **Mutação em PLAN** | Nenhum comando que altere arquivos em PLAN MODE (terminal inclusive). Só leitura e análise. |
| 9 | **Título do fórum (vagalume-destaque)** | NÃO se migra para `<strong>` — é elemento fixo do template canônico (verde `#587C41` no fórum). |
| 10 | **Foco ao VS Code** | `code -r <caminho>` é a ÚLTIMA ação do ACT — nunca seguido de checkpoint update, chat ou outros comandos. |
| 11 | **Commit+push** | Só com autorização explícita do mestre. Sequência anti-travamento: diagnóstico → `git commit -m` (uma linha) → `git push origin master` → verificação. |
| 12 | **Vídeo padrão** | TODO vídeo é embedado por padrão (iframe YouTube). Só fallback (thumb + link) se o mestre avisar que NÃO é autorizado. |

---

## Histórico

| Data | Mudança |
|---|---|
| 24/09/2026 | Criação do arquivo — consolidando regras dispersas de lições aprendidas e rotina de entrega no chat. |
| **Label de parte** | `Parte N — Título` | `Parte 3 — Territórios do cuidado e bem-estar` |