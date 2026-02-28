# ⌨️ VSCode Vim — Himan's Cheat Sheet

> `SPC` = Space (leader) · `C-x` = Ctrl+x · `A-x` = Alt+x · 🆕 = custom binding · 🔵 = native vim · ⚡ = plugin

---

## 🪟 Split Navigation

### Move Between Splits — `Normal`

| Key | Action |
|-----|--------|
| `C-h` | Focus **left** split 🆕 |
| `C-j` | Focus **below** split 🆕 |
| `C-k` | Focus **above** split 🆕 |
| `C-l` | Focus **right** split 🆕 |

### Move Buffer to a Split — `Normal`

| Key | Action |
|-----|--------|
| `SPC H` | Move buffer to **far left** 🆕 |
| `SPC J` | Move buffer to **bottom** 🆕 |
| `SPC K` | Move buffer to **top** 🆕 |
| `SPC L` | Move buffer to **far right** 🆕 |
| `SPC x` | **Swap** with next split 🆕 |

### Resize Splits — `Normal`

| Key | Action |
|-----|--------|
| `SPC =` | **Equalize** all splits 🆕 |
| `SPC +` | Increase **height** 🆕 |
| `SPC -` | Decrease **height** 🆕 |
| `SPC >` | Increase **width** 🆕 |
| `SPC <` | Decrease **width** 🆕 |

### Native Split Commands — `Normal`

| Key | Action |
|-----|--------|
| `C-w v` | **Vertical** split 🔵 |
| `C-w s` | **Horizontal** split 🔵 |
| `C-w r` | **Rotate** splits clockwise 🔵 |
| `C-w R` | **Rotate** counter-clockwise 🔵 |
| `C-w x` | **Swap** with next window 🔵 |
| `C-w o` | **Close** all other splits 🔵 |

---

## 📑 Tabs & Buffers

### Insert Mode

| Key | Action |
|-----|--------|
| `C-t t` | **New** tab 🆕 |
| `C-t n` | **Next** tab 🆕 |
| `C-t p` | **Prev** tab 🆕 |
| `C-t o` | **Close** other tabs 🆕 |

### Normal Mode

| Key | Action |
|-----|--------|
| `gt` | Next tab 🔵 |
| `gT` | Prev tab 🔵 |
| `:tabnew` | Open new tab 🔵 |
| `:tabo` | Close other tabs 🔵 |

---

## ✍️ Insert Mode

| Key | Action |
|-----|--------|
| `jk` | Exit to **Normal** mode 🆕 |
| `A-h` | Focus **left** split 🆕 |
| `A-j` | Focus **below** split 🆕 |
| `A-k` | Focus **above** split 🆕 |
| `A-l` | Focus **right** split 🆕 |

---

## 🚀 EasyMotion ⚡

| Key | Action |
|-----|--------|
| `SPC SPC w` | Jump to **word start** forward |
| `SPC SPC b` | Jump to **word start** backward |
| `SPC SPC s` | **2-char** search jump |
| `SPC SPC j` | Jump to **line below** |
| `SPC SPC k` | Jump to **line above** |

---

## 👟 Sneak ⚡

| Key | Action |
|-----|--------|
| `s xy` | Sneak **forward** to 3 chars |
| `S xy` | Sneak **backward** to 2 chars |
| `;` | Next sneak match |
| `,` | Prev sneak match |

> `sneakReplacesF` is on — so `f` and `F` also use sneak

---

## 🐪 CamelCase Motion ⚡

| Key | Action |
|-----|--------|
| `SPC w` | Next **camel/snake** segment |
| `SPC b` | Prev **camel/snake** segment |
| `SPC e` | End of **camel/snake** segment |

---

## 🎯 Targets / Text Objects ⚡

| Key | Action |
|-----|--------|
| `ci n(` | Change inside **next** parens |
| `da l"` | Delete around **last** quote |
| `yi a` | Yank inside **argument** |
| `ci b` | Change inside **block** `{}` |
| `ci n[` | Change inside **next** brackets |

---

## 💡 Essential Normal Mode

| Key | Action |
|-----|--------|
| `gg` | Top of file 🔵 |
| `G` | Bottom of file 🔵 |
| `C-d` | Half-page **down** 🔵 |
| `C-u` | Half-page **up** 🔵 |
| `zz` | Center cursor on screen 🔵 |
| `%` | Jump to matching bracket 🔵 |
| `*` | Search **word** under cursor 🔵 |
| `.` | Repeat last change 🔵 |
| `ci w` | Change inner word 🔵 |
| `ys iw"` | Surround word with `"` 🔵 |
| `gr` | Replace with register ⚡ |
| `qa` → `@a` | Record & replay macro 🔵 |
| `~` | Toggle case 🔵 |
| `C-a` | Increment number 🔵 |
| `C-x` | Decrement number 🔵 |
| `g;` | Jump to last **edit** position 🔵 |
| `gi` | Insert at last **insert** position 🔵 |
| `''` | Jump back to last position 🔵 |

---

## 📋 Registers & Marks

| key | action |
|-----|--------|
| `"ay` | yank into register `a` 🔵 |
| `"ap` | paste from register `a` 🔵 |
| `"+y` | yank to **system clipboard** 🔵 |
| `"+p` | paste from **system clipboard** 🔵 |
| `ma` | set mark `a` 🔵 |
| `` `a `` | jump to mark `a` (exact position) 🔵 |
| `'a` | jump to Mark `a` (line) 🔵 |

---

## 🔍 Search & Replace

| Key | Action |
|-----|--------|
| `/pattern` | Search forward 🔵 |
| `?pattern` | Search backward 🔵 |
| `n` / `N` | Next / prev match 🔵 |
| `*` / `#` | Search word under cursor fwd/bwd 🔵 |
| `:%s/old/new/g` | Replace all in file 🔵 |
| `:%s/old/new/gc` | Replace with **confirmation** 🔵 |
| `:s/old/new/g` | Replace in **current line** 🔵 |
