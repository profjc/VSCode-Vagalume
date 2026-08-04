# Onde paramos

## Sessão 03/08/2026 — Reorganização e atualização do `.clinerules`

### Trabalho realizado
- **Reorganização do `.clinerules` em 3 níveis (N1, N2, N3) com prioridade N1 > N2 > N3:**
  - N1 expandido de 3 para 9 seções (incorporado do PSG: Regra Suprema, Modos PLAN/ACT, Nunca Extrapolar, Memória Persistente, Git, Prevenção de Travamento)
  - N1.1 Identidade atualizada com persona de Designer Instrucional (DI) + fluxo `.docx` → `.md` → storyboard → páginas + tom de comunicação
  - N2 expandido de 4 para 6 seções (Acessibilidade expandida com mobile-first + leitores de tela + contraste 4.5:1, Fidelidade ao Texto do Autor, Links Externos, Comportamento do TinyMCE)
  - N3 com contexto-first, instrução pré-H5P, fluxo de navegação, foco VS Code, biblioteca de componentes referenciada
  - 8 backups criados em `docs/backups/` (v1 a v8)
- **Nenhum template de página foi alterado nesta sessão**

### Limpeza de estrutura
- **Pasta `templates/pages/modulo-01/`**: excluída (vazia, resíduo de nomeação antiga)
- **`M1/ParteIV/`**: padrão híbrido registrado como pendência — não movido por segurança

### Decisões registradas
- **Sem storyboards**: não manteremos mais arquivos separados de storyboard — apenas o HTML final (você "pensa" o storyboard como DI e entrega a página pronta)
- **N3.5 atualizada**: fluxo de trabalho agora parte da conferência Moodle × repositório
- **N2.5.5 atualizada**: texto reflete que o DI pensa o storyboard mentalmente, sem criar arquivo separado

---

## 📋 Próxima sessão — Conferência e alinhamento Moodle × repositório

### Diretrizes
1. **Revisar todas as páginas** — conferir quais páginas existem no Moodle vs quais temos arquivos locais
2. **Incluir as que faltam** — criar estrutura base vazia para páginas do Moodle ausentes no repositório (fluxo em lote)
3. **Excluir o que não interessa mais** — páginas antigas/obsoletas sem correspondência no Moodle
4. **Modificar quando solicitado** — substituir páginas antigas pelas revisadas (quando o usuário pedir)
5. **Sem storyboards** — quando existirem storyboards para páginas já criadas, **apagar** (manter apenas o HTML)

### Status atual da auditoria
| Pasta/Seção | Status |
|---|---|
| `templates/pages/Boas-vindas/` | ⚠️ **Em revisão** — Páginas 1-3 concluídas, Página 4 pendente |
| `templates/pages/M1/` | ✅ **Completo** |
| `templates/pages/M2/` | ⚠️ **Incompleto** — último arquivo: `M2P3L1p3.html` |
| `M2/ParteIII/Licao2/` | ⚠️ Pasta vazia |
| `M2/ParteIV/Licao1/` | ⚠️ Pasta vazia |
| `M2/ParteV/` | ⚠️ Pasta vazia |
| `M1/ParteIV/` | 🟡 Híbrido (pendência) |

### Divergência
- **Moodle**: Módulo 2 **completo** (5 partes, incluindo M2P5L2)
- **Repositório local**: Módulo 2 **incompleto** (até M2P3L1p3)
- **Faltam no repositório**: Parte III Lição 2, Parte IV, Parte V do Módulo 2
- **[Pendente]** Módulo 3 — iniciar

---

## Última página revisada
- **Arquivo:** `templates/pages/Boas-vindas/Boas-vindas_Parceria_Van_Leer_e_Vagalume.html`
- **Módulo:** Módulo de Boas-vindas
- **Página:** 4 — Parceria Van Leer e Vagalume (revisada em 03/08/2026)
- **Última página no repositório (M2):** `templates/pages/M2/ParteIII/Licao1/M2P3L1p3.html`

## Próxima página a revisar
- **Módulo de Boas-vindas:** ✅ Concluído (4/4 páginas revisadas)
- **Próximo módulo:** Módulo 2 — a definir pelo usuário (M2P3L1p3 é a última no repositório, mas M2P5L2 existe no Moodle)

## Sessão 03/08/2026 (noite) — Atualização do CSS Global
- **Novo CSS recebido via `temp/Vagalume_curso.css.txt`** (803 linhas, arquivo já excluído após processamento)
- **Principal adição:** Bloco "ESTILIZAÇÃO DOS TÍTULOS DAS SEÇÕES - FORMATO TILES" (25 linhas) — estiliza `.sectiontitle` no formato Tiles com fundo bege e cor marrom
- **Arquivos atualizados:**
  - `assets/css/vagalume-tema.css` — substituído pelo novo CSS (803 linhas, era 386)
  - `docs/diretrizes/Vagalume_curso.css.md` — substituído pelo novo CSS (formato `.md`, era 1198 linhas com escapes)
- **Backup:** `docs/backups/vagalume-tema-v1-antes-tiles-2026-03-08.css` (versão antiga de 386 linhas)
- **Impacto no HTML das páginas:** Nenhum — mudanças são apenas em elementos do Moodle/Tema Trema/Formato Tiles, não afetam classes `.vagalume-*` usadas nas páginas

## Novas diretrizes estabelecidas nesta sessão
- **Solução de placeholder de imagem via SVG data URI** — imagem temporária (40×40, quadrado laranja "img") ao lado da imagem oficial; fluxo: clicar na imagem temporária → subir → copiar src → colar na oficial → apagar bloco temporário.
- **PLAN mode planeja, ACT mode apenas executa** — ao salvar um arquivo no modo ACT, NÃO replanejar; simplesmente executar o que foi definido no PLAN.
- **NUNCA avançar para a próxima página sem autorização** — registrado como precedente por violação em 03/08/2026.
- **Sempre devolver foco ao VS Code** ao concluir a revisão de uma página — reforçado em 03/08/2026.

## Git/GitHub
- Último commit: `b99849c` — `docs: expande clinerules com N1 N2 e N3 completos 7 backups`
- Pendências desta sessão serão commitadas no encerramento

## VSCode-PSG
- `.clinerules` do PSG também atualizado com as mesmas 4 regras gerais
- Ambos os repositórios comitados e enviados ao GitHub