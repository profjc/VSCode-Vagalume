# PLANO DE AÇÃO — PARTE 2 DO MÓDULO 2 (Lição 1 + Atividade 1)

> **ARQUIVO TEMPORÁRIO de retomada** — criado em 08/08/2026 antes da execução.
> Se a sessão travar, ler este arquivo + `Onde-paramos.md` para saber onde paramos.

## Contexto
- Fonte: `temp/Ajustes_Módulo 2.md` (linhas 257–299) — instruções do autor para a Parte 2.
- Ponto de partida: Lição 1 da Parte 2 — "Leitura com a Primeira Infância".
- Objetivo: unificar a Lição 1 em 1 página (p1 + vídeo da p2) e ajustar a Atividade 1.

## Decisões confirmadas pelo mestre (esta sessão)
1. **Título da atividade** (nos comentários HTML, pois o título no Moodle é inserido pelo mestre):
   `Atividade: Ler para bebês: o que essa prática nos revela?`
   — Padrão de acessibilidade: sem caixa alta, dois pontos no lugar da barra. ✅ confirmado.
2. **Texto introdutório "Já vimos até aqui..." permanece** no topo da página unificada (autor não pediu remoção). ✅
3. **Legenda do vídeo**: TODAS as barras "|" do autor são substituídas por ":" (regra de acessibilidade):
   `Ler para bebê: a importância da leitura na primeira infância: Canal: Ler é uma Viagem (YouTube): 22min07s` ✅
4. **Remoção do título do card H5P é EXPERIMENTAL** — não vira regra nova até o mestre avaliar se ficou bom.
5. **Checkpoint obrigatório antes de ações longas/complexas** — registrar estado antes de executar (regra nova do mestre).

## Páginas envolvidas
| Arquivo | Ação |
|---|---|
| `templates/pages/M2/ParteII/Licao1/M2P2L1p1.html` | **REESCREVER** — página unificada (passo 1) |
| `templates/pages/M2/ParteII/Licao1/M2P2L1p2.html` | **EXCLUIR** após validação da fusão no Moodle (passo 3) |
| `templates/pages/M2/ParteII/Licao1/M2P2L1p3.html` | **EDITAR** — atividade (passo 2); depois **RENOMEAR** → `M2P2L1p2.html` (passo 3) |

## Passos (um por vez, aguardando validação do mestre)

### PASSO 1 ✅ CONCLUÍDO E VALIDADO — Página unificada `M2P2L1p1.html`
- Reescrita em 08/08/2026 e **VALIDADA pelo mestre** ("Ficou bom. Estamos evoluindo.").
- Conteúdo final: texto "Já vimos até aqui..." + parágrafo do vídeo (nome SEM negrito, trecho completo EM NEGRITO conforme autor) + vídeo centralizado (iframe `bz0WYDtpR5g`) + legenda `Ler para bebê: a importância da leitura na primeira infância: Canal: Ler é uma Viagem (YouTube): 22min07s` + rodapé.
- ⚠️ **LIÇÃO DO MESTRE:** "Cuidado para não perder negritos novamente" — atenção redobrada aos `<strong>` ao reescrever páginas.

### PASSO A ✅ CONCLUÍDO — Editar a antiga Página 3 `M2P2L1p3.html` (atividade H5P)
- Reescrita com comentários "Página 2", parágrafo inicial FORA do BOX, BOX "Colocando em prática" (ícone `fa-pencil-square`), parágrafo final FORA do BOX, card H5P **sem cabeçalho** (experimental), rodapé criado.
- `<strong>` da comanda preservados: "duas afirmações são verdadeiras", "uma é falsa", "Sua tarefa é identificar as duas afirmações verdadeiras em cada tema."

### PASSO B ✅ CONCLUÍDO — Excluir a antiga Página 2
- `git rm templates/pages/M2/ParteII/Licao1/M2P2L1p2.html` — executado com sucesso.

### PASSO C ✅ CONCLUÍDO — Renomear a atividade para nova Página 2
- `git mv M2P2L1p3.html M2P2L1p2.html` — executado. `git status`: `M M2P2L1p1.html`, `MM M2P2L1p2.html`, `D M2P2L1p3.html`, `M Onde-paramos.md`, `?? temp/`.

### PASSO D ✅ CONCLUÍDO — Devolver foco ao VS Code
- `code templates/pages/M2/ParteII/Licao1/M2P2L1p2.html` — executado.

### ESTADO ATUAL (aguardando validação do mestre no Moodle)
- Lição 1 da Parte 2 agora tem **2 páginas** no repositório:
  - `M2P2L1p1.html` — página unificada (texto + vídeo + legenda) ✅ validada
  - `M2P2L1p2.html` — atividade H5P (nova p2) ⏳ **aguarda validação**
- No Moodle, o mestre deverá: colar a nova p2 (substituindo a antiga p3) e remover a antiga p2.
- ⚠️ A lógica do exercício H5P (2 verdadeiras) será ajustada pelo mestre no **Lumi**.

### PASSO 4 ⏳ — Registros (com autorização)
- `Onde-paramos.md`: pendência M1 (`M1P1L1p3.html` — remover sinopse) + nova regra de vídeo (sem sinopse, apenas legenda).
- `components-library.md`: componente 23 (vídeo com sinopse → vídeo com legenda apenas).
- `.clinerules` N3.2.11: atualizar quando o padrão for definitivo.

## Pendência mapeada no MÓDULO 1 (apenas anotar, NÃO executar)
- **`M1P1L1p3.html`** — ÚNICA página do M1 com vídeo + BOX de sinopse → afetada pela nova regra.
- `M1P3L1p4.html` — tem `vagalume-sinopse` mas NÃO é vídeo (bloco "Para refletir") → não afetada.
- `M1P2L1p2.html`, `M1P4L1p3.html`, `M1P4F1.html` — vídeos/link sem sinopse → não afetadas.

## Checklist de validação mental (antes de entregar cada página)
- [ ] Comentário de abertura correto (decimal + título)
- [ ] Rodapé de fechamento presente
- [ ] Sem comentário não padrão "Estrutura alinhada ao Manual da Marca Vaga Lume"
- [ ] SEM `<style>`, `<link>` ou `<script>` globais
- [ ] Acessibilidade: alt, aria-hidden, contraste, hierarquia de headings
- [ ] `display: flow-root` no container
- [ ] Legenda centralizada (`text-center`)
- [ ] Links externos com `nomediaplugin` + `target="_blank"` + `rel="noopener noreferrer"`