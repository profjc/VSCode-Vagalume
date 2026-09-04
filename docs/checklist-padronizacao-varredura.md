# 📋 Checklist de Varredura — Padronização de Todas as Páginas do Curso

> Firmado em **04/09/2026** (sessão de consolidação de padronizações de cor/ênfase).
> **Método:** aplicar **página por página**, ciclo PLAN → ACT → validação com o mestre. **Nunca em lote** (N1.3.3, N1.4.1).
> **Propósito:** guia de varredura para deixar todas as páginas existentes em conformidade, e referência para geração de páginas novas (M3/M4 já nascem no padrão).

---

## 1. Negritos e ênfase (regra §6.2 / N2.4.13)
- [ ] **Converter todo `.vagalume-destaque` usado como ênfase** (verde, em fundo branco) → `<strong>` puro, **sem cor manual** *(padrão: herda cor do contexto; já migrado em `M1P1L1p1`, `M1P1L1p2`)*
- [ ] **EXCEÇÃO — NÃO migrar: título verde do fórum.** O título discreto do fórum (`<span class="vagalume-destaque">Fórum: ...</span>`) é **elemento FIXO do template canônico** `templates/components/forum.html` (linha 8) e deve permanecer verde. **Não é ênfase em texto corrido** — é identidade visual do fórum. Sempre confrontar páginas de fórum com `forum.html` antes de decidir.
- [ ] **Remover cor manual de todo `<strong>`** (nem `style`, nem classe de cor)
- [ ] **Caixas creme** (`.vagalume-destaque-bloco`, `.vagalume-sinopse`, `.vagalume-jumbotron`): texto/`<strong>` deve ser **marrom institucional `#5B3925`** — remover qualquer `color: #261810` manual dentro desses blocos
- [ ] **Títulos com classe `.h5`/`.h6` em `<span>`/`<p>` dentro de caixas**: fixar `color: #5b3925;` explícito (a classe `.h5` **não herda** o marrom do CSS global — só tags reais `h1`–`h5`)

## 2. Links externos (regra 6.1 — versão final 04/09/2026)
- [ ] Todo `<a>` externo: `color: **#944b11**` + `font-weight-bold` + `text-decoration: underline` + `class="nomediaplugin"` + `target="_blank"` + `rel="noopener noreferrer"`
- [ ] Substituir os padrões antigos: laranja `#D96F1A` sobre branco **e** marrom `#5B3925` sobre bege → todos para **`#944B11`**
- [ ] **Links-botão** (`.btn btn-primary`): **manter** laranja `#D96F1A` + texto branco `#FFFFFF` (não alterar)
- [ ] **Legendas de figuras** com link azul (caso Módulo 2): padrão → `#944B11`

## 3. Legenda de vídeo (regra §4.14)
- [ ] Migrar formato antigo `Título: Canal: Nome (YouTube): 00min00s` → **`Título (minutagem); canal: nome do canal`**
- [ ] Confirmar: sem "(YouTube)", sem ":" redundante após o título, sem "|" (§4.13)
- [ ] Páginas já identificadas com formato antigo: `M1P4L1p2`, `M2P2L1p1`, `M2P4L2p1`, `M2P4L4p3`, `M2P4L4p4` **(+ varrer todos os vídeos)**
- [ ] Verificar também legendas do padrão thumbnail + botão "Assistir no YouTube" (embed não autorizado)

## 3b. Fonte em legenda de imagem sem link (regra §4.15)
- [ ] Fonte de imagem/ilustração na `.figure-caption` deve ser **texto puro, sem `<a>`** (não linkada)
- [ ] Converter legendas de imagem que hoje têm link → texto puro: `M2P3L2p1`, `M2P4L4p1`, `M2P4L4p2` (fonte `tudosobreleitura` / `minadehq.com.br`) — **exceto** se o mestre indicar que fiquem clicáveis
- [ ] Padrão de referência: `M2P1L1p1.html`, `M2P1L1p2.html` (`Fonte: pipipum.com.br`)

## 4. Outros itens de conformidade (varredura geral)
- [ ] `aria-hidden="true"` em ícones decorativos (`fa-*`)
- [ ] **Atributos de imagem** completos: `width`, `height`, `loading="lazy"`, `alt` (ou sr-only sem duplicidade — §4.7)
- [ ] **Legendas de figuras** centralizadas (`figure-caption text-center mt-2`); legendas de vídeo à esquerda
- [ ] **Zero "|"** em qualquer texto visível (§4.13)
- [ ] **Zero palavras em inglês** residuais (N2.5.6)
- [ ] Headings: hierarquia sem saltos (preferir **tags reais** `h1`–`h6` às classes, salvo com cor explícita)
- [ ] Comentários decimais de abertura/fechamento com título do DI (N2.2.2)
- [ ] Último elemento visível sem margem inferior (`mb-0`) — S1

---

## ✅ Já conformes (referências / concluídos)
- **Padrão de negrito (referência do mestre):** `templates/pages/Boas-vindas/Boas-vindas_Apresentacao.html`
- **Negritos migrados:** `M1P1L1p1.html`, `M1P1L1p2.html`
- **Fórum `M1P1F1.html`:** corrigido (Para participar `#5b3925`; mensagem final herda cor)
- **Template canônico do fórum:** `templates/components/forum.html` (corrigido 04/09)
- **Legenda de vídeo:** `M1P1L1p2.html` já no padrão novo (§4.14)
- **Links (regra/S2/templates):** padronizados para `#944B11` (04/09/2026)

---

## ⏭️ Ordem sugerida da varredura
1. **Boas-vindas** (4 páginas)
2. **Módulo 1** (Partes 1–4)
3. **Módulo 2** (Apresentação + Partes 1–6 + fóruns)
4. **Frontpage/capas** (`frontpage/`)
5. **M3/M4** (quando chegarem — já nascem no padrão novo)

---

## ⏳ Pendências externas à varredura
Registradas em `docs/pendencias-projeto.md` (ícones dos cards, imagem Acervo M2P4L3p1, Parte 5 do M1, referências M2) — não fazem parte desta varredura de padronização.