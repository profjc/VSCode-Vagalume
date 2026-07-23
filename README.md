# 🌟 Vaga Lume - Curso Moodle 4.5

> Projeto de produção de páginas HTML para o curso **Vaga Lume** no Moodle 4.5 (tema **Trema**)

---

## 📁 Estrutura do Projeto

```
VSCode-Vagalume/
├── .clinerules              # Regras para o Cline (IA assistente)
├── style-guide.md           # Guia de estilo visual (cores, tipografia, classes)
├── components-library.md    # Biblioteca de componentes HTML reutilizáveis
├── moodle-config.json       # Metadados e configurações do projeto
├── README.md                # Este arquivo
│
├── assets/
│   ├── css/
│   │   └── vagalume-tema.css    # CSS Global do tema (injetado via SCSS Póst)
│   └── images/
│       ├── capas/               # Imagens de capa/banner
│       ├── ilustracoes/         # Ilustrações do curso
│       └── personagens/         # Personagens do curso
│
├── content/
│   └── modulo-01/               # Storyboards/briefings dos módulos
│
├── templates/
│   ├── components/              # Componentes reutilizáveis (arquivos .html)
│   └── pages/                   # Páginas finais prontas para colar no Moodle
│
├── docs/
│   ├── workflow.md              # Fluxo de trabalho documentado
│   └── checklist-entrega.md     # Checklist de validação pré-entrega
│
├── temp/                        # Caixa de entrada para novos arquivos
│
└── scripts/                     # Scripts de automação (se houver)
```

---

## 🎨 Identidade Visual

| Cor | Hexadecimal | Uso |
|-----|-------------|-----|
| Laranja | `#D96F1A` | Principal (botões, bordas, headers) |
| Marrom | `#5B3925` | Títulos |
| Marrom escuro | `#261810` | Texto corrido |
| Verde | `#587C41` | Destaques |
| Dourado | `#F8B133` | Títulos grandes |
| Bege | `#FAEBDD` | Fundo de cards |
| Verde frontpage | `#5D7A3C` | Fundo da página inicial |

---

## 🚀 Fluxo de Trabalho

1. **Briefing** → NotebookLM gera o roteiro pedagógico
2. **Produção** → Cline ou Gemini Customizado gera o HTML
3. **Validação** → Verificar checklist (sem `<style>`, `src=""`, acessibilidade)
4. **Publicação** → Colar o HTML no editor de texto do Moodle

---

## 🔒 Regras Importantes

- **Nunca** colocar `<style>` ou `<link>` dentro do HTML
- **Nunca** usar `src` com caminhos fictícios em imagens
- **Sempre** usar classes Bootstrap 4 nativas para grids
- **Sempre** colocar imagens em formato PNG ou JPEG
- **Prefixo**: `.vagalume-` para todas as classes personalizadas

---

## 📚 Documentação

- `.clinerules` → Regras para a IA
- `style-guide.md` → Guia visual completo
- `components-library.md` → Snippets de componentes

---

> Projeto Vaga Lume V3 - Moodle 4.5 / Tema Trema
