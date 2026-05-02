# 🎬 Klip Animation DB

**Drama Farm stilidagi 2D animatsiyalar bazasi**
Claude AI tomonidan 24/7 avtomatik to'ldiriladi.

## 📊 Maqsadli hajm

| Kategoriya | Maqsad | Hozir |
|------------|--------|-------|
| 👤 Inson harakatlari | 300+ | 0 |
| 😊 Emotsiyalar | 60+ | 0 |
| 🐕 Hayvonlar | 120+ | 0 |
| 🌿 Tabiat | 80+ | 0 |
| 📦 Buyumlar | 100+ | 0 |
| 🏔️ Fonlar | 60+ | 0 |

## 🚀 GitHub'ga yuklash (BIR MARTA)

### 1. Repo yaratish
```
GitHub.com → New repository → klip-animation-db → Public → Create
```

### 2. Fayllarni yuklash
```bash
git clone https://github.com/SИЗNING_USERNAME/klip-animation-db
# bu fayllarni ko'chiring
git add .
git commit -m "🚀 Baza yaratildi"
git push
```

### 3. API Key qo'shish (SECRET)
```
GitHub Repo → Settings → Secrets → Actions → New secret
Name: ANTHROPIC_API_KEY
Value: sk-ant-xxxxx (sizning API kalitingiz)
```

### 4. Workflow yoqish
```
GitHub Repo → Actions → Enable workflows
```

**Shu bilan tayyor!** Har 6 soatda Claude yangi animatsiyalar yozadi.

## ⚡ Qo'lda ishga tushirish

```
GitHub → Actions → 🎬 Animation DB Generator → Run workflow
```

## 🔗 Klip Studio bilan ulash

`db_loader.py` ni `klip-pro-v6/` papkasiga ko'chiring:
```python
# app.py ichida:
import db_loader
db_loader.GITHUB_USER = "СИЗNING_USERNAME"

# HTML generatsiyada:
anim_js = db_loader.build_animation_map_js(scenes)
```

## 📁 Fayl strukturasi

```
db/
├── index.json              ← Asosiy katalog (avtomat yangilanadi)
├── humans/
│   ├── humans_walking_slowly.json
│   ├── humans_running_joyfully.json
│   └── ...
├── emotions/
│   ├── emotions_pure_joy.json
│   └── ...
├── animals/
│   └── ...
├── nature/
│   └── ...
├── objects/
│   └── ...
└── backgrounds/
    └── ...
```

## 🎨 Animatsiya formati

Har JSON fayl:
```json
{
  "id": "humans_walking_slowly",
  "category": "humans",
  "topic": "walking slowly and thoughtfully",
  "tags": ["walking", "slowly", "thoughtfully"],
  "created": "2026-04-27T10:00:00",
  "draw": "function draw(ctx, t, W, H) { ... }"
}
```

`draw(ctx, t, W, H)` — Canvas 2D funksiyasi:
- `ctx` — Canvas context
- `t` — vaqt (soniya, loop uchun)
- `W` = 1280, `H` = 720

## 🎬 Uslub

Barcha animatsiyalar **Drama Farm stilida**:
- ✅ Beige/cream fon
- ✅ Qalin qora konturlar
- ✅ Stick figure odamlar
- ✅ Qo'l chizgandek tuyg'u
- ❌ Tayyor internet animatsiyalar yo'q
- ❌ External resurslar yo'q

## 📈 Monitoring

Baza to'lishi jarayonini kuzating:
```
GitHub → Actions → oxirgi ishga tushish → loglar
```

---
*Klip Studio PRO v6.3 bilan ishlash uchun mo'ljallangan*
